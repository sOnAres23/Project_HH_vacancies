import re

from src.hh_api import HeadHunterAPI
from src.hh_work_with_file import JSONSaver
from src.hh_work_with_vacancies import Vacancy
from src.utils import top_n_vacancies, filter_by_word, sorting_of_salary, work_with_user


def main():
    """Главная функция для работы с пользователем"""
    answer = input("Введите запрос по слову или вакансии, которое интересует: ")
    answer_page = int(input("Введите страницу № для вывода 100 вакансий: "))

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(keyword=answer, page=answer_page)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver("vacancies")
    json_saver.add_vacancies(vacancies_list)
    print('Список всех вакансий добавлен в файл "vacancies"')

    # Сортировка Топ N вакансий по зарплате
    top_n = int(input("Введите количество вакансий для вывода в топ с наибольшей ЗП: "))
    result_top_n = top_n_vacancies(vacancies_list, top_n)

    # Фильтрация вакансии по заданному слову в описании
    filter_word = input("Введите слово интересующее Вас связанное с вакансией или пропустите: ").replace(" ", "").lower()
    result_filter_words = filter_by_word(result_top_n, filter_word)
    print(result_filter_words)
    # Сортировка по диапазону цен пользователя
    print("Введите диапазон ЗП: ")
    _salary_from = int(re.sub(r"[^\d]", "", input("От: ")))
    _salary_to = int(re.sub(r"[^\d]", "", input("До: ")))
    result_sort_salary = sorting_of_salary(result_filter_words, _salary_from, _salary_to)

    # Обрабатываем для удобного чтения пользователю
    result_vacancies = work_with_user(result_sort_salary)

    # print(f"\nНайдено {len(result_vacancies)} вакансий:\n")
    return result_vacancies


if __name__ == "__main__":
    main()
