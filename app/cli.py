import argparse

from typing import List, Tuple


def parse_args() -> Tuple[List[str], str]:
    '''
    Разбирает аргументы командной строки.
    '''
    parser = argparse.ArgumentParser(
        description='Скрипт для анализа макроэкономических данных'
    )

    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к CSV-файлам с экономическими данными'
    )

    parser.add_argument(
        '--report',
        required=True,
        help='Название отчёта'
    )

    args = parser.parse_args()
    return args.files, args.report
