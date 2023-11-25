import datetime

import requests


class Designation:
    def __init__(self, date: datetime.date, baseurl: str, edugroup: str):
        self.date = date
        self.url = self.build_url(baseurl)
        self.edugroup = edugroup

    def build_url(self, baseurl: str):
        return baseurl.format(date=self.local_date(sep='-', long_year=False))

    def exists(self):
        return requests.get(self.url).status_code == 200

    def local_date(self, sep: str = '/', long_year: bool = True) -> str:
        year_format = 'Y' if long_year else 'y'
        return self.date.strftime(f'%d{sep}%m{sep}%{year_format}')

    @property
    def as_markdown(self):
        return f'{self.local_date()} #Personal #NombramientosDiarios [Nombramiento de {self.edugroup}]({self.url})'

    def __str__(self):
        return f'NOMBRAMIENTO {self.edugroup}: {self.url}'
