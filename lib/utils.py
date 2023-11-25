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
