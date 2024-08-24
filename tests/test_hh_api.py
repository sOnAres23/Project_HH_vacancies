import pytest
from unittest.mock import Mock, patch

from src.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


@patch('requests.get')
def test_get_vacancies_success(mock_get, hh_api):
    """Тест, который имитирует ответ от API с примером по слову 'программист'"""
    mock_get.return_value.json.return_value = {
        'items': [
            {'name': 'Программист', 'employer': {'name': 'Компания'},
             'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'}}
        ]
    }

    # Вызовем метод get_vacancies и проверим его результат
    vacancies = hh_api.get_vacancies(keyword='программист')
    assert len(vacancies) == 1
    assert vacancies[0]['name'] == 'Программист'
