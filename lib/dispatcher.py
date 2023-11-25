import datetime

import settings

from .designations import Designation


def dispatch(date: datetime.date = None):
    date = date or datetime.date.today()
    for edugroup, baseurl in settings.DESIGNATION_CONFIG.items():
        if (d := Designation(date, baseurl, edugroup)).exists():
            print(d.as_markdown)
