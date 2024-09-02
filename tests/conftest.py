import pytest

from src.hh_work_with_vacancies import Vacancy


@pytest.fixture
def info_api():
    return [{
        "id": "105394925",
        "premium": False,
        "name": "Junior Backend разработчик (Python)",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {
            "id": "1",
            "name": "Москва",
            "url": "https://api.hh.ru/areas/1"
        },
        "salary": {
            "from": 110000,
            "to": 200000,
            "currency": "RUR",
            "gross": True
        },
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": {
            "city": "Москва",
            "street": "улица Ефремова",
            "building": "10с1к4/5",
            "lat": 55.725118,
            "lng": 37.572836,
            "description": None,
            "raw": "Москва, улица Ефремова, 10с1к4/5",
            "metro": None,
            "metro_stations": [],
            "id": "2699685"
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-08-22T14:23:08+0300",
        "created_at": "2024-08-22T14:23:08+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=105394925",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/105394925?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/105394925",
        "relations": [],
        "employer": {
            "id": "4046921",
            "name": "Tevian (ООО Технологии видеоанализа)",
            "url": "https://api.hh.ru/employers/4046921",
            "alternate_url": "https://hh.ru/employer/4046921",
            "logo_urls": {
                "original": "https://img.hhcdn.ru/employer-logo-original/1071177.png",
                "240": "https://img.hhcdn.ru/employer-logo/5905338.png",
                "90": "https://img.hhcdn.ru/employer-logo/5905337.png"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4046921",
            "accredited_it_employer": True,
            "trusted": True
        },
        "snippet": {
            "requirement": "Знание <highlighttext>Python</highlighttext> 3.8+ (junior). Знание одного из фреймворков: Django, Flask, AIOHTTP, FastAPI. Знание SQL. Работа в среде Linux. ",
            "responsibility": "Разработка новых сервисов компьютерного зрения с применением нейронных сетей. Интеграция продуктов компании с системами партнеров. Поддержка и развитие существующих web..."
        },
        "contacts": None,
        "schedule": {
            "id": "fullDay",
            "name": "Полный день"
        },
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [
            {
                "id": "96",
                "name": "Программист, разработчик"
            }
        ],
        "accept_incomplete_resumes": False,
        "experience": {
            "id": "between1And3",
            "name": "От 1 года до 3 лет"
        },
        "employment": {
            "id": "full",
            "name": "Полная занятость"
        },
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None
    }]


@pytest.fixture
def first_vacancy():
    return Vacancy("Frontend-разработчик", "Москва", "Иви", 110000, 200000,
                   "Базовые знания Python. Умение конфигурировать Webpack, TypeScript",
                   "От 1 года до 3 лет", "https://hh.ru/vacancy/104970095")


@pytest.fixture
def second_vacancy():
    return Vacancy("Специалист по тестированию/Тестировщик", "Москва", "БУРГЕР КИНГ РОССИЯ",
                   110000, 0, "Опыт работы в тестировании от 2-х лет.",
                   "От 1 года до 3 лет", "https://hh.ru/vacancy/99565999")


@pytest.fixture
def third_vacancy():
    return Vacancy("DevOps Engineer", "Москва", "RUTUBE", 100000, 160000,
                   "Умение и желание автоматизировать рутинные операции (Bash / Python / Go).",
                   "От 3 до 6 лет", "https://hh.ru/vacancy/85312568")


@pytest.fixture
def list_of_vacancies(first_vacancy, second_vacancy, third_vacancy):
    return [first_vacancy, second_vacancy, third_vacancy]
