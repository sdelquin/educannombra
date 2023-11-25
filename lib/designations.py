import datetime
import shelve

import requests
from logzero import logger

import settings
from lib.notification import TelegramBot

from . import utils


class Designation:
    archive = shelve.open(settings.ARCHIVE_DB_PATH)
    tgbot = TelegramBot()

    def __init__(self, date: datetime.date, baseurl: str, edugroup: str):
        self.date = date
        self.url = self.build_url(baseurl)
        self.edugroup = edugroup

    @property
    def as_markdown(self):
        return utils.render_message(
            settings.APPOINTMENT_TMPL_NAME, designation=self, hashtag=settings.NOTIFICATION_HASHTAG
        )

    @property
    def id(self) -> str:
        return self.url

    @property
    def is_published(self) -> bool:
        logger.debug('❓ Checking if designation is published')
        return requests.get(self.url).status_code == 200

    @property
    def already_dispatched(self) -> bool:
        return self.archive.get(self.id) is not None

    def build_url(self, baseurl: str):
        return baseurl.format(date=self.local_date(sep='-', long_year=False))

    def local_date(self, sep: str = '/', long_year: bool = True) -> str:
        year_format = 'Y' if long_year else 'y'
        return self.date.strftime(f'%d{sep}%m{sep}%{year_format}')

    def save(self) -> None:
        logger.debug('💾 Saving designation into the database')
        self.archive[self.id] = True

    def notify(self, telegram_chat_id: str = settings.TELEGRAM_CHAT_ID) -> None:
        self.tgbot.send(telegram_chat_id, self.as_markdown)

    def __str__(self):
        return f'Nombramiento de {self.edugroup}: {self.url}'
