import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "comptes.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
LOG_FILE = BASE_DIR / "kwizipay.log"


def setup_logging():
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')



