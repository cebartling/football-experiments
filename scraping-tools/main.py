import sys

from scraping_tools.profootballfocus.Driver import Driver


def main() -> int:
    Driver().execute()
    return 0


if __name__ == '__main__':
    sys.exit(main())
