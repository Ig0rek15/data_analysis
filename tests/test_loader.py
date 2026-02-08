from app.loader import load_data


def test_load_data(csv_file):
    '''
    Проверяет корректность чтения CSV-файла.
    '''
    result = load_data([str(csv_file)])

    assert result == [
        {'country': 'A', 'gdp': '100'},
        {'country': 'B', 'gdp': '200'},
    ]
