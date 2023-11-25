import datetime

import settings

from .designations import Designation


def dispatch(date: datetime.date = None):
    date = date or datetime.date.today()
    for edugroup, baseurl in settings.DESIGNATION_CONFIG.items():
        d = Designation(date, baseurl, edugroup)
        if d.already_dispatched:
            print('Already dispatched')
        elif d.is_published:
            print(d.as_markdown)
            d.save()
        else:
            print('Not published')
