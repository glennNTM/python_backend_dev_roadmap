import logging
from pathlib import Path

def setup_logging():
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "comptes.json"
LOG_FILE = BASE_DIR / "kwizipay.log"