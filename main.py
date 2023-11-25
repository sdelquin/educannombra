import datetime

from lib import dispatcher

date = datetime.date(year=2023, month=11, day=24)
dispatcher.dispatch(date)
