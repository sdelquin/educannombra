import datetime
import re
import shelve
import tempfile

import PyPDF2
import requests
from logzero import logger

import settings
from lib.notification import TelegramBot

from . import utils


class Resolution:
    archive = shelve.open(settings.ARCHIVE_DB_PATH)
    tgbot = TelegramBot()

    def __init__(self, date: datetime.date, baseurl: str, edugroup: str):
        self.date = date
        self.url = self.build_url(baseurl)
        self.edugroup = edugroup

    @property
    def as_markdown(self):
        return utils.render_message(
            settings.RESOLUTION_TMPL_NAME, resolution=self, hashtag=settings.NOTIFICATION_HASHTAG
        )

    @property
    def id(self) -> str:
        return self.url

    @property
    def num_designations(self) -> int:
        logger.debug('🍿 Getting number of designations')
        pdf = PyPDF2.PdfReader(self.resolution)
        last_page = pdf.pages[-1]
        contents = last_page.extract_text()
        if m := re.search(r'N[uú]mero total de nombramientos:\s*(\d+)', contents, re.I):
            num_entries = int(m[1])
        else:
            num_entries = 0
        return num_entries

    def already_dispatched(self) -> bool:
        return self.archive.get(self.id) is not None

    def build_url(self, baseurl: str):
        return baseurl.format(date=self.format_published_date(sep='-', long_year=False))

    def format_published_date(self, sep: str = '/', long_year: bool = True) -> str:
        year_format = 'Y' if long_year else 'y'
        return self.date.strftime(f'%d{sep}%m{sep}%{year_format}')

    def save(self) -> None:
        logger.debug('💾 Saving designation into the database')
        self.archive[self.id] = True

    def notify(self, telegram_chat_id: str = settings.TELEGRAM_CHAT_ID) -> None:
        self.tgbot.send(telegram_chat_id, self.as_markdown)

    def download_resolution(self) -> bool:
        logger.debug('⭐ Downloading resolution for designations')
        if (response := requests.get(self.url)).status_code == 200:
            self.resolution = tempfile.NamedTemporaryFile().name
            with open(self.resolution, 'wb') as f:
                f.write(response.content)
            return True
        return False

    def __str__(self):
        return f'Nombramiento de {self.edugroup}: {self.url}'
