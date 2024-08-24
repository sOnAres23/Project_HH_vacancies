import json
import logging


from abc import ABC, abstractmethod

# """Создаем логгер для логирования методов и записываем логи в директорию logs"""
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
#                     filename='../logs/hh_work_with_file.log',  # Запись логов в файл
#                     filemode='w')  # Перезапись файла при каждом запуске
logger = logging.getLogger("hh_work_with_file.py")


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


class JSONSaver(BaseWorkWithFile):
    """
    Класс для работы с JSON файлом:
    записи, получения и удаления информации по вакансиям.
    Наследуется от класса BaseWorkWithFile, который является родительским.
    """

    def __init__(self, filename):
        self._filename = filename

    def add_vacancies(self, hh_list: list[object, ...]) -> None:
        """Метод, который принимает список объектов класса и записывает их в файл JSON"""
        list_vacancies = []
        logger.info("Перебираем и сортируем вакансии по нужным атрибутам...")
        for vac in hh_list:
            if vac.salary_from == 0 and vac.salary_to == 0:
                vacancies = {
                    "name": vac.name,
                    "city": vac.city,
                    "employer": vac.employer,
                    "salary": "Зарплата не указана",
                    "description": vac.description,
                    "experience": vac.experience,
                    "link": vac.link
                }
                list_vacancies.append(vacancies)

            else:
                vacancies = {
                    "name": vac.name,
                    "city": vac.city,
                    "employer": vac.employer,
                    "salary_from": vac.salary_from,
                    "salary_to": vac.salary_to,
                    "description": vac.description,
                    "experience": vac.experience,
                    "link": vac.link
                }
                list_vacancies.append(vacancies)

        with open(f"../data/{self._filename}.json", "w", encoding="cp1251", errors='replace') as f:
            json.dump(list_vacancies, f, ensure_ascii=False, indent=4)
            logger.info("Вакансии в файл успешно добавлены")

    def print_vacancies(self) -> None:
        """Метод, который получает данные из файла JSON который в нём есть"""
        with open(f"../data/{self._filename}.json", "r", encoding="cp1251", errors='replace') as f:
            data = json.load(f)
            print(data)

    def del_vacancies(self) -> None:
        """Метод, который удаляет содержимое файла JSON"""
        with open(f"../data/{self._filename}.json") as f:
            pass
