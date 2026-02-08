import pytest


@pytest.fixture
def gdp_data():
    '''
    Тестовые данные для отчёта среднего ВВП.
    '''
    return [
        {'country': 'A', 'gdp': '100'},
        {'country': 'A', 'gdp': '300'},
        {'country': 'B', 'gdp': '200'},
    ]


@pytest.fixture
def csv_file(tmp_path):
    '''
    Временный CSV-файл для тестирования загрузчика.
    '''
    file_path = tmp_path / 'data.csv'
    file_path.write_text(
        'country,gdp\n'
        'A,100\n'
        'B,200\n'
    )
    return file_path
