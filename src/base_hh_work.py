from abc import ABC, abstractmethod


class BaseWorkWithFile(ABC):
    """Абстрактный класс, для класса работы с файлом JSON"""
    @abstractmethod
    def add_vacancies(self, file):
        """Абстрактный метод добавление вакансий в файл"""
        pass

    @abstractmethod
    def print_vacancies(self):
        """Абстрактный метод для получения данных о вакансиях из файла"""
        pass

    @abstractmethod
    def del_vacancies(self):
        """Абстрактный метод удаления информации о вакансиях из файла"""
        pass
