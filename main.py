import datetime
import glob
import os

import typer

import settings
from lib import dispatcher, utils

logger = utils.init_logger()
app = typer.Typer(add_completion=False)


@app.command()
def run(
    date: str = typer.Argument(datetime.date.today(), help='Designation date in format YYYY-MM-DD'),
    disable_notifications: bool = typer.Option(
        False, '--disable-notifications', '-x', help='Disable notifications'
    ),
    disable_persist: bool = typer.Option(
        False, '--disable-persist', '-w', help='Disable persist in DB'
    ),
    loglevel: str = typer.Option(
        'DEBUG', '--loglevel', '-l', help='Log level (debug, info, error)'
    ),
):
    """Notify educational designations."""
    dispatcher.dispatch(
        utils.build_date_from_str(date), not disable_notifications, not disable_persist
    )


@app.command()
def clean(force: bool = typer.Option(False, '--force', '-f', help='Force clean. No confirmation!')):
    """Clean archive database."""
    if force or typer.confirm('Are you sure to delete archive database?'):
        for file_path in glob.glob(str(settings.ARCHIVE_DB_PATH) + '*'):
            os.remove(file_path)
        logger.info('🧽 DB is clean!')


if __name__ == '__main__':
    try:
        app()
    except Exception as err:
        logger.exception(err)
