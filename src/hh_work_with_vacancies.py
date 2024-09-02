import re
from typing import Any


class Vacancy:
    """
    Класс для работы с вакансиями.
    Обрабатывает вакансии из списка словарей по заданным атрибутам.
    Добавляет отсортированные вакансии в новый список, а также сравнивает
        вакансии между собой по зарплате.
    """
    __slots__ = ("name", "city", "employer", "salary_from", "salary_to", "currency", "description", "experience", "link")
    name: str
    city: str
    employer: str
    salary_from: int
    salary_to: int
    currency: str
    description: str
    experience: str
    link: str

    def __init__(self, name, city, employer, salary_from, salary_to, currency, description, experience, link):
        self.name = name
        self.city = city
        self.employer = employer
        if isinstance(salary_from, int):
            self.salary_from = salary_from
        else:
            self.salary_from = 0
        if isinstance(salary_to, int):
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        if isinstance(currency, str):
            self.currency = currency
        else:
            self.currency = 0
        self.description = description
        self.experience = experience
        self.link = link

    def __lt__(self, other) -> bool:
        """Магический метод который проверяет, какоая из зарплат меньше"""
        return self.salary_from < other.salary_from

    def __gt__(self, other) -> bool:
        """Магический метод который проверяет, какоая из зарплат больше"""
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list[object, Any]:
        """Класс-метод, который принимает список словарей с вакансиями,
        отбирает необходимы данные по атрибутам и добавляет объекты класса в список"""
        class_list_vacancies = []
        for vacancy in vacancies:
            name = vacancy["name"]
            city = vacancy["area"]["name"]
            employer = vacancy["employer"]["name"]
            if vacancy.get('salary'):
                salary_from = vacancy.get('salary').get('from')
            else:
                salary_from = 0

            if vacancy.get('salary'):
                salary_to = vacancy.get('salary').get('to')
            else:
                salary_to = 0

            if vacancy.get('salary'):
                currency = vacancy.get('salary').get('currency')
            else:
                currency = 0

            if vacancy.get('snippet').get('requirement'):
                description = re.sub(r'<.*?>', '', vacancy["snippet"]["requirement"])
            else:
                description = "Не указано"
            experience = vacancy["experience"]["name"]
            link = vacancy["alternate_url"]

            class_list_vacancies.append(cls(name, city, employer, salary_from, salary_to, currency, description, experience, link))

        return class_list_vacancies
