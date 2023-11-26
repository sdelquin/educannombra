import datetime

from logzero import logger

import settings

from .designations import Designation


def dispatch(date: datetime.date = None, notify: bool = True, persist: bool = True):
    date = date or datetime.date.today()
    logger.info(f'👷‍♂️ Dispatching designations for {date}')
    for edugroup, baseurl in settings.DESIGNATION_CONFIG.items():
        d = Designation(date, baseurl, edugroup)
        logger.info(f'🟣 {d}')
        if d.already_dispatched():
            logger.debug('👋 Designation was already dispatched. Discarding!')
        elif d.download_resolution():
            if notify:
                d.notify()
            else:
                logger.debug('🛑 Notification is disabled by user')
            if persist:
                d.save()
            else:
                logger.debug('🛑 Persistence is disabled by user')
        else:
            logger.debug('💤 Designation is not yet published')
