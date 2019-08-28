from PageObject.FormPage import FormPage


def test_guest_should_see_login_and_registry_form(browser):
    """
    Проверка заполнения всех полей и отправки формы
    :param browser:
    :return:
    """
    # открываем страницу с формой
    page = FormPage(browser)
    page.get_form_page()

    # вводим имя и фамилию
    page.input_first_name()
    page.input_last_name()

    # выбираем дату рождения
    page.select_month()
    page.select_day()
    page.select_year()

    # выбираем интсрумент и день недели
    page.select_instrument()
    page.select_days_for_classes()

    # вводим дату и время занятий
    page.select_month_to_start()
    page.select_day_to_start()
    page.select_year_to_start()

    page.select_hour()
    page.select_minutes()
    page.select_am_pm()

    # заполняем комментарий и отправляем форму нажатием кнопки
    page.input_comments()
    page.click_submit()

    # проверяем сообщение об отправленной форме
    assert page.check_thank_message() is True

