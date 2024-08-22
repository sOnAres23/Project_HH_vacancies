import json
import logging
import re

from src.base_hh_work import BaseWorkWithFile
from src.hh_api import HeadHunterAPI
from src.hh_work_with_vacancies import Vacancy

# """Создаем логгер для логирования методов и записываем логи в директорию logs"""
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
#                     filename='../logs/hh_work_with_file.log',  # Запись логов в файл
#                     filemode='w')  # Перезапись файла при каждом запуске
logger = logging.getLogger("hh_work_with_file.py")


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
            # text = '<highlighttext>Python</highlighttext>'
            # for i in data:
            #     if text in i["description"]:
            #         cleaned_text = re.sub(r'<.*?>', '', text)
            #         i["description"].replace(text, cleaned_text)
            print(data)

    def del_vacancies(self) -> None:
        """Метод, который удаляет содержимое файла JSON"""
        with open(f"../data/{self._filename}.json") as f:
            pass


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies(keyword="Python", page=1)
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

json_saver = JSONSaver("vacancies")
# json_saver.add_vacancies(vacancies_list)
json_saver.print_vacancies()
