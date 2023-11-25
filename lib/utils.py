import datetime
import functools
from pathlib import Path

import jinja2
import logzero

import settings


def init_logger():
    logformat = (
        '%(asctime)s '
        '%(color)s'
        '[%(levelname)-8s] '
        '%(end_color)s '
        '%(message)s '
        '%(color)s'
        '(%(filename)s:%(lineno)d)'
        '%(end_color)s'
    )

    console_formatter = logzero.LogFormatter(fmt=logformat)
    file_formatter = logzero.LogFormatter(fmt=logformat, color=False)
    logzero.setup_default_logger(formatter=console_formatter)
    logzero.logfile(
        settings.LOGFILE,
        maxBytes=settings.LOGFILE_SIZE,
        backupCount=settings.LOGFILE_BACKUP_COUNT,
        formatter=file_formatter,
    )
    return logzero.logger


@functools.cache
def init_jinja():
    loader = jinja2.FileSystemLoader(settings.MSG_TEMPLATES_DIR)
    return jinja2.Environment(loader=loader)


def render_message(template_name: Path, **args) -> str:
    jinja_env = init_jinja()
    template = jinja_env.get_template(template_name)
    return template.render(**args)


def build_date_from_str(date_input: str) -> datetime.date:
    return datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
