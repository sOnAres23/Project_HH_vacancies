from src.hh_work_with_vacancies import Vacancy


def test_vacancy(first_vacancy):
    assert first_vacancy.name == "Frontend-разработчик"
    assert first_vacancy.city == "Москва"
    assert first_vacancy.employer == "Иви"
    assert first_vacancy.salary_from == 110000
    assert first_vacancy.salary_to == 200000
    assert first_vacancy.description == "Базовые знания Python. Умение конфигурировать Webpack, TypeScript"
    assert first_vacancy.experience == "От 1 года до 3 лет"
    assert first_vacancy.link == "https://hh.ru/vacancy/104970095"


def test_cast_to_object_list(info_api):
    vac = Vacancy.cast_to_object_list(info_api)
    assert len(vac) == 1
    assert vac[0].name == "Junior Backend разработчик (Python)"
    assert vac[0].city == "Москва"
    assert vac[0].employer == "Tevian (ООО Технологии видеоанализа)"
    assert vac[0].salary_from == 110000
    assert vac[0].salary_to == 200000
    assert vac[0].description == ("Знание Python 3.8+ (junior). Знание одного из фреймворков: Django, Flask, AIOHTTP, "
                                  "FastAPI. Знание SQL. Работа в среде Linux. ")
    assert vac[0].experience == "От 1 года до 3 лет"
    assert vac[0].link == "https://hh.ru/vacancy/105394925"


def test_lt_(first_vacancy, third_vacancy):
    assert Vacancy.__lt__(first_vacancy, third_vacancy) is False
    assert Vacancy.__gt__(first_vacancy, third_vacancy) is True
