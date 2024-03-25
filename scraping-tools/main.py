import argparse
import sys

from scraping_tools.profootballfocus.Driver import Driver as PFFDriver
from scraping_tools.ras_football.Driver import Driver as RasDriver


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='python main.py',
        description='Something here',
        epilog='Good luck!')
    parser.add_argument('task', help='The task to execute')
    args = parser.parse_args()
    task = args.task

    if task == 'pff':
        PFFDriver().execute()
    if task == 'ras':
        RasDriver().execute()
    return 0


if __name__ == '__main__':
    sys.exit(main())
