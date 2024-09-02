from src.utils import top_n_vacancies, filter_by_word, sorting_of_salary, result_for_user


def test_top_vacancies(list_of_vacancies):
    assert len(top_n_vacancies(list_of_vacancies, 1)) == 1


def test_filter_words(list_of_vacancies):
    assert len(filter_by_word(list_of_vacancies, "Опыт")) == 1


def test_sorting_of_salary(list_of_vacancies):
    assert len(sorting_of_salary(list_of_vacancies, 0, 200000)) == 3
    assert len(sorting_of_salary(list_of_vacancies, 0, 160000)) == 2
    assert len(sorting_of_salary(list_of_vacancies, 120000, 150000)) == 0


def test_result_for_user_1(capsys, third_vacancy):
    result_for_user([third_vacancy])

    captured = capsys.readouterr()

    expected_output_for_3 = (f"Вакансия №: 1\n"
                             f"Название вакансии: DevOps Engineer\nГород вакансии: Москва\n"
                             f"Работодатель: RUTUBE\nЗарплата: от 100000 до 160000\n"
                             f"Описание: Умение и желание автоматизировать рутинные операции (Bash / Python / Go).\n"
                             f"Нужный опыт: От 3 до 6 лет\n"
                             f"Ссылка на вакансию: https://hh.ru/vacancy/85312568").strip()

    # Проверка соответствия захваченного вывода и ожидаемого результата
    assert captured.out.strip() == expected_output_for_3


def test_result_for_user_2(capsys, second_vacancy):
    result_for_user([second_vacancy])

    captured = capsys.readouterr()

    expected_output_for_2 = (f"Вакансия №: 1\n"
                             f"Название вакансии: Специалист по тестированию/Тестировщик\nГород вакансии: Москва\n"
                             f"Работодатель: БУРГЕР КИНГ РОССИЯ\nЗарплата: от 110000\n"
                             f"Описание: Опыт работы в тестировании от 2-х лет.\n"
                             f"Нужный опыт: От 1 года до 3 лет\n"
                             f"Ссылка на вакансию: https://hh.ru/vacancy/99565999").strip()

    assert captured.out.strip() == expected_output_for_2
