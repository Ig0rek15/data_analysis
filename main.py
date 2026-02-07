import logging

from tabulate import tabulate

from app.cli import parse_args
from app.loader import load_data
from app.reports import REPORTS


logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)


def main() -> None:
    try:
        files, report_name = parse_args()
        logging.info('Запуск отчёта: %s', report_name)

        if report_name not in REPORTS:
            raise ValueError(f'Неизвестный отчёт: {report_name}')

        data = load_data(files)
        logging.info(f'Загружено строк данных: {len(data)}')

        report = REPORTS[report_name]
        table = report.generate(data)

        print(tabulate(table, headers=report.headers, tablefmt='github'))

    except FileNotFoundError as exc:
        logging.error(f'Файл не найден: {exc}')
    except ValueError as exc:
        logging.error(f'{exc}')
    except Exception as exc:
        logging.error(f'Неожиданная ошибка: {exc}')


if __name__ == '__main__':
    main()

# py main.py --files data/economic1.csv data/economic2.csv --report average-gdp
