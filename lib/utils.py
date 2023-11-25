import datetime
import functools
from pathlib import Path

import jinja2

import settings


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
