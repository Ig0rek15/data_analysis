import csv

from typing import List, Dict


def load_data(files: List[str]) -> List[Dict[str, str]]:
    '''
    Загружает данные из CSV-файлов.
    '''
    rows: List[Dict[str, str]] = []

    for file_path in files:
        with open(file_path, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                rows.append(row)

    return rows


# print(*load_data(['data/economic1.csv', 'data/economic2.csv']), sep='\n')
