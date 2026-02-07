from collections import defaultdict
from typing import List, Dict, Any

from app.reports.base import BaseReport


class AverageGDPReport(BaseReport):
    '''
    Отчёт, рассчитывающий средний ВВП по странам.
    '''

    name = 'average-gdp'

    @property
    def headers(self) -> List[str]:
        '''
        Заголовки таблицы отчёта.
        '''
        return ['country', 'gdp']

    def generate(self, data: List[Dict[str, str]]) -> List[List[Any]]:
        '''
        Формирует отчёт среднего ВВП по странам.
        '''
        gdp_by_country: Dict[str, List[float]] = defaultdict(list)

        for row in data:
            country = row['country']
            gdp = float(row['gdp'])
            gdp_by_country[country].append(gdp)

        result: List[List[Any]] = []

        for country, gdps in gdp_by_country.items():
            average_gdp = sum(gdps) / len(gdps)
            result.append([country, round(average_gdp, 2)])

        result.sort(key=lambda item: item[1], reverse=True)
        return result
