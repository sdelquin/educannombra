import datetime

from logzero import logger

import settings

from .resolution import Resolution


def dispatch(date: datetime.date = None, notify: bool = True, persist: bool = True):
    date = date or datetime.date.today()
    logger.info(f'🍕 Dispatching designation resolutions for {date}')
    for edugroup, baseurl in settings.DESIGNATION_CONFIG.items():
        res = Resolution(date, baseurl, edugroup)
        logger.info(f'🟣 {res}')
        if res.already_dispatched():
            logger.debug('👋 Resolution was already dispatched. Discarding!')
        elif res.download_resolution():
            if notify:
                res.notify()
            else:
                logger.debug('🛑 Notification is disabled by user')
            if persist:
                res.save()
            else:
                logger.debug('🛑 Persistence is disabled by user')
        else:
            logger.debug('💤 Resolution is not yet published')
