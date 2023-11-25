import datetime

import settings

from .designations import Designation


def dispatch(date: datetime.date = None, notify: bool = True, persist: bool = True):
    date = date or datetime.date.today()
    for edugroup, baseurl in settings.DESIGNATION_CONFIG.items():
        d = Designation(date, baseurl, edugroup)
        if d.already_dispatched:
            print('Already dispatched')
        elif d.is_published:
            if notify:
                print(d.as_markdown)
            if persist:
                d.save()
        else:
            print('Not published')
