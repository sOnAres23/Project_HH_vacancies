from src.hh_api import HeadHunterAPI
from src.hh_work_with_file import JSONSaver
from src.hh_work_with_vacancies import Vacancy
from src.utils import top_n_vacancies, filter_by_word, sorting_of_salary, result_for_user


def main():
    """Главная функция для работы с пользователем"""
    print("Добро пожаловать на сервис по поиску вакансий с сайта hh.ru!\n")
    answer = input("Введите запрос по слову или вакансии, которое интересует: ")
    answer_page = int(input("Введите страницу № для вывода 100 вакансий в файл: "))

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(keyword=answer, page=answer_page)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    print("Введите имя файла на английском для добавления в него вакансий: ")
    f_name = input()
    json_saver = JSONSaver(filename=f_name)
    json_saver.add_vacancies(vacancies_list)
    print(f'Cписок всех вакансий добавлен в файл "{f_name}"')

    # Сортировка Топ N вакансий по зарплате
    top_n = int(input("Введите количество вакансий для вывода в топ с наибольшей ЗП: "))
    result_top_n = top_n_vacancies(vacancies_list, top_n)

    # Фильтрация вакансии по заданному слову в описании
    filter_word = input("Введите слово интересующее Вас связанное с вакансией или пропустите: ").replace(" ", "").lower()
    result_filter_words = filter_by_word(result_top_n, filter_word)

    # Сортировка по диапазону цен пользователя
    print("Введите диапазон ЗП: ")
    _salary_from = int(input("От: "))
    _salary_to = int(input("До: "))
    result_sort_salary = sorting_of_salary(result_filter_words, _salary_from, _salary_to)

    # Обрабатываем для удобного чтения пользователю
    print(f"\nНайдено {len(result_sort_salary)} вакансий:\n")

    result_vacancies = result_for_user(result_sort_salary)

    return result_vacancies


if __name__ == "__main__":
    main()
