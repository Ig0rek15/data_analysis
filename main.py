from app.cli import parse_args
from app.loader import load_data
from app.reports import REPORTS

from tabulate import tabulate


def main() -> None:
    files, report_name = parse_args()

    if report_name not in REPORTS:
        raise ValueError(f'Неизвестный отчёт: {report_name}')

    data = load_data(files)
    report = REPORTS[report_name]

    table = report.generate(data)
    print(tabulate(table, headers=report.headers, tablefmt='grid'))


if __name__ == '__main__':
    main()

# py main.py --files data/economic1.csv data/economic2.csv --report average-gdp
