import json
import logging

import requests

from src.base_hh_api import BaseHeadHunterAPI

"""Создаем логгер для логирования методов и записываем логи в директорию logs"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(name)s %(funcName)s - %(levelname)s - %(message)s',
                    filename='../logs/hh_api.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске
logger = logging.getLogger("hh_api.py")


class HeadHunterAPI(BaseHeadHunterAPI):
    """
    Класс для работы с API HeadHunter.
    Наследуется от класса BaseHeadHunterAPI, который является родительским.
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        self.filename = "../data/for_work_with.json"

    def get_vacancies(self, keyword):
        """Метод получающий информацию по заданной вакансии, в противном случае выводит все вакансии"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            try:
                logger.info("Делаем запрос...")
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            except requests.RequestException as e:
                logger.error(f"Ошибка при запросе списка ваканский: {e}")
            else:
                vacancies = response.json()['items']
                logger.info("Запрос корректный, возвращаем данные...")
                self.vacancies.extend(vacancies)
                self.__params['page'] += 1

                return self.vacancies


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies(keyword="Python")

with open("../data/for_work_with.json", 'w', encoding='utf-8') as file:
    logger.info("Записываем данные в JSON файл, для дальнейшей работы")
    json.dump(hh_vacancies, file, ensure_ascii=False, indent=4)
