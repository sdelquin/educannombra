from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent
PROJECT_NAME = PROJECT_DIR.name
DATA_DIR = PROJECT_DIR / 'data'

DESIGNATION_CONFIG = {
    'Maestros y maestras de la provincia de Las Palmas': 'https://www.gobiernodecanarias.org/educacion/DGPer/NombraDiarios/Docs/NDPLP{date}.PDF',
    'Maestros y maestras de la provincia de Santa Cruz de Tenerife': 'https://www.gobiernodecanarias.org/educacion/DGPer/NombraDiarios/Docs/NDPTF{date}.PDF',
    'Profesorado de otros cuerpos: ambas provincias': 'https://www.gobiernodecanarias.org/educacion/DGPer/NombraDiarios/Docs/NDS{date}.PDF',
}

ARCHIVE_DB_PATH = config('ARCHIVE_DB_PATH', default=DATA_DIR / 'archive.dbm', cast=Path)
ARCHIVE_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = config('TELEGRAM_CHAT_ID')

MSG_TEMPLATES_DIR = config('MSG_TEMPLATES_DIR', default=PROJECT_DIR / 'templates', cast=Path)
APPOINTMENT_TMPL_NAME = config('APPOINTMENT_TMPL_NAME', default='designation.jinja')

NOTIFICATION_HASHTAG = config('NOTIFICATION_HASHTAG', default='#Personal #NombramientosDiarios')

LOGFILE = config('LOGFILE', default=PROJECT_DIR / (PROJECT_NAME + '.log'), cast=Path)
LOGFILE_SIZE = config('LOGFILE_SIZE', cast=float, default=1e6)
LOGFILE_BACKUP_COUNT = config('LOGFILE_BACKUP_COUNT', cast=int, default=3)
