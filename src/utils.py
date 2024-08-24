def top_n_vacancies(vacancies: list[object, ...], value: int) -> list:
    """Функция, которая принимает список с вакансиями и выводит количетсов вакансий с самой высокой ЗП"""

    sort_list = sorted(vacancies, key=lambda v: v.salary_from, reverse=True)
    return sort_list[0:value]


def filter_by_word(vacancies: list[object, ...], word: str) -> list:
    """Функция, которая принимает список с вакансиями и фильтрует по заданному слову в описании"""
    new_list_filter = []
    for vacancy in vacancies:
        if word in vacancy.description:
            new_list_filter.append(vacancy)

    return new_list_filter


def sorting_of_salary(vacancies: list[object, ...], salary_from: int, salary_to: int) -> list:
    """Функция, которая принимает список с вакансиями и два аргумента ЗП от и до и сортирует список"""
    list_salary = []
    for vacancy in vacancies:
        if salary_from <= vacancy.salary_from and salary_to >= vacancy.salary_to:
            list_salary.append(vacancy)

    return list_salary


def result_for_user(list_vacancies: list):
    """Функция, которая выводит итоговый список вакансий для пользователя"""
    if list_vacancies is not None:
        for num, vac in enumerate(list_vacancies, 1):
            if vac.salary_from >= vac.salary_to:
                vacancy_1 = (f"Вакансия №: {num}\n"
                             f"Название вакансии: {vac.name}\nГород вакансии: {vac.city}\n"
                             f"Работодатель: {vac.employer}\nЗарплата: от {vac.salary_from}\n"
                             f"Описание: {vac.description}\nНужный опыт: {vac.experience}\n"
                             f"Ссылка на вакансию: {vac.link}\n")
                print(vacancy_1)
            elif vac.salary_from <= vac.salary_to:
                vacancy_2 = (f"Вакансия №: {num}\n"
                             f"Название вакансии: {vac.name}\nГород вакансии: {vac.city}\n"
                             f"Работодатель: {vac.employer}\nЗарплата: от {vac.salary_from} до {vac.salary_to}\n"
                             f"Описание: {vac.description}\nНужный опыт: {vac.experience}\n"
                             f"Ссылка на вакансию: {vac.link}\n")
                print(vacancy_2)
    else:
        print("Вакансий по такому запросу не найдено!")
