import logging

from exceptions import KwiziPayError
from config import setup_logging

logger = logging.getLogger(__name__)  


def main():
    setup_logging()


if __name__=="__main__":
    main()