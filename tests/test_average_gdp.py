from app.reports.average_gdp import AverageGDPReport


def test_average_gdp_report(gdp_data):
    '''
    Проверяет корректность расчёта среднего ВВП и сортировку.
    '''
    report = AverageGDPReport()
    result = report.generate(gdp_data)

    assert result == [
        ['A', 200.0],
        ['B', 200.0],
    ]
