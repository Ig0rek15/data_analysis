from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseReport(ABC):
    '''
    Базовый класс для всех отчётов.
    '''

    name: str

    @abstractmethod
    def generate(self, data: List[Dict[str, str]]) -> List[List[Any]]:
        '''
        Формирует данные отчёта.
        '''
        pass

    @property
    @abstractmethod
    def headers(self) -> List[str]:
        '''
        Заголовки таблицы отчёта.
        '''
        pass
