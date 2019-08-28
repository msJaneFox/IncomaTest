import random
from selenium.common.exceptions import NoSuchElementException
from random import choice
from string import ascii_uppercase
from datetime import datetime
from selenium.webdriver.support.select import Select



class FormPage():
    """
    Методы для работы с элементами страницы
    """

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = 'https://form.jotformeu.com/92373687741367'
        self.browser.implicitly_wait(timeout)

    # Элементы на странице
    FIRST_NAME = '[name="q3_name[first]"]'
    LAST_NAME = '[name="q3_name[last]"]'
    MONTH = '#input_4_month'
    DAY = '#input_4_day'
    YEAR = '#input_4_year'
    CHOICE_INSTRUMENT = '[name="q5_choiceOf"]'
    DAYS_CHECKBOX = '.form-checkbox-item:nth-child(3)'
    START_MONTH = '#month_7'
    START_DAY = '#day_7'
    START_YEAR = '#year_7'
    START_HOUR = '#hour_7'
    START_MINUTES = '#min_7'
    AM_PM = '#ampm_7'
    COMMENTS = '[name="q8_comments"]'
    SUBMIT = '#input_2'
    THANK = '.thankyou'

    @staticmethod
    def generate_text(size=12):
        """
        Генерирует случайную строку с заданным размером
        :param size: Длина строки. По умолчанию 12
        :return:
        """
        return (''.join(choice(ascii_uppercase) for i in range(size)))

    def get_form_page(self):
        """
        Переходит на страницу
        :return:
        """
        self.browser.get(self.url)

    def input_first_name(self):
        """
        Вводит имя
        :return:
        """
        first_name_field = self.browser.find_element_by_css_selector(self.FIRST_NAME)
        first_name_field.send_keys(self.generate_text())

    def input_last_name(self):
        """
        Вводит фамилию
        :return:
        """
        last_name_field = self.browser.find_element_by_css_selector(self.LAST_NAME)
        last_name_field.send_keys(self.generate_text())

    def select_month(self):
        """
        Выбирает случайный месяц рождения
        :return:
        """
        month = Select(self.browser.find_element_by_css_selector(self.MONTH))
        month.select_by_index(random.randint(1, 12))

    def select_day(self):
        """
        Выбирает случайный день рождения
        :return:
        """
        day = Select(self.browser.find_element_by_css_selector(self.DAY))
        day.select_by_index(random.randint(1, 28))

    def select_year(self):
        """
        Выбирает случайный год рождения
        :return:
        """
        year = Select(self.browser.find_element_by_css_selector(self.YEAR))
        year.select_by_index(random.randint(2, 100))

    def select_instrument(self):
        """
        Выбирает случайный инструмент
        :return:
        """
        instrument = Select(self.browser.find_element_by_css_selector(self.CHOICE_INSTRUMENT))
        instrument.select_by_index(random.randint(1, 5))

    def select_days_for_classes(self):
        """
        Выбирает случайный день недели для посещения
        :return:
        """
        day_checkbox = self.browser.find_element_by_css_selector(self.DAYS_CHECKBOX.format(random.randint(1, 7)))
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 1000)")
        day_checkbox.click()

    def select_month_to_start(self):
        """
        Выбирает случайный месяц начала
        :return:
        """
        month_start = self.browser.find_element_by_css_selector(self.START_MONTH)
        month_start.clear()
        month_start.send_keys(random.randint(1, 12))

    def select_day_to_start(self):
        """
        Выбирает случайный день начала
        :return:
        """
        day_start = self.browser.find_element_by_css_selector(self.START_DAY)
        day_start.clear()
        day_start.send_keys(random.randint(1, 28))

    def select_year_to_start(self):
        """
        Выбирает случайный год начала
        :return:
        """
        year_now = datetime.now().year
        day_start = self.browser.find_element_by_css_selector(self.START_YEAR)
        day_start.clear()
        day_start.send_keys(random.randint(year_now+1, year_now+10))

    def select_hour(self):
        """
        Выбирает случайный час занятий
        :return:
        """
        hour = Select(self.browser.find_element_by_css_selector(self.START_HOUR))
        hour.select_by_index(random.randint(1, 12))

    def select_minutes(self):
        """
        Выбирает случайную минуту занятий
        :return:
        """
        minutes = Select(self.browser.find_element_by_css_selector(self.START_MINUTES))
        minutes.select_by_index(random.randint(1, 6))

    def select_am_pm(self):
        """
        Выбирает случайную часть дня
        :return:
        """
        am_pm = Select(self.browser.find_element_by_css_selector(self.AM_PM))
        am_pm.select_by_index(random.randint(0, 1))

    def input_comments(self):
        """
        Заполняет поле комментарии
        :return:
        """
        about_field = self.browser.find_element_by_css_selector(self.COMMENTS)
        about_field.send_keys(self.generate_text())

    def click_submit(self):
        """
        Нажимает кнопку submit
        :return:
        """
        submit = self.browser.find_element_by_css_selector(self.SUBMIT)
        submit.click()

    def check_thank_message(self):
        """
        Проверяет наличие сообщение об успешной отправке формы
        :return:
        """
        try:
            self.browser.find_element_by_css_selector(self.THANK)
        except NoSuchElementException:
            return False
        return True

