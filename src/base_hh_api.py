from abc import ABC, abstractmethod


class BaseHeadHunterAPI(ABC):
    """Абстрактный класс, для класса получения API с hh.ru"""
    pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass
