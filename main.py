import datetime

import requests

import settings

# date = datetime.date.today()
date = datetime.date(year=2023, month=11, day=24)
for edugroup, durl in settings.DESIGNATION_URLS.items():
    durl = durl.format(date=date.strftime('%d-%m-%y'))
    if (response := requests.get(durl)).status_code == 200:
        print('ok')
