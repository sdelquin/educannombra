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
