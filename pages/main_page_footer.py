import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPageFooter(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/search/'
        super().__init__(web_driver, url)

    '''footer'''

    # триггер скроллинга - Лабиринт в кармане
    scroll = WebElement(xpath='// *[@id="body-top"]/div[5]/div[2]/div/div[1]/div[1]/div[1]')
    # кнопка AppStore
    app_store = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[1]/div[2]/a[1]')
    # кнопка GooglePlay
    google_play = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[1]/div[2]/a[2]')
    # кнопка AppGallery
    app_gallery = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[1]/div[2]/a[3]')
    # кнопка Вконтакте
    vk = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[1]/a')
    # кнопка Вконтакте. Дети
    vk_kids = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[2]/a')
    # кнопка Ютьуб
    youtube = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[3]/a')
    # кнопка Одноклассники
    ok = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[4]/a')
    # кнопка Яндекс.Дзен
    dzen = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[5]/a')
    # кнопка Телеграм
    telegram = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[6]/a')
    # кнопка ТикТок
    tik_tok = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[1]/div[2]/div[2]/ul/li[7]/a')
    # кнопка Все книги
    all_books = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]/a')
    # кнопка Школа
    school = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[2]/a')
    # кнопка Журналы
    magazines = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[3]/a')
    # кнопка Игрушки
    games = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[4]/a')
    # кнопка Канцтовары
    office_supplies = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[5]/a')
    # кнопка CD/DVD
    cd_dvd = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[5]/a')
    # кнопка Сувениры
    souvenirs = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[6]/a')
    # кнопка Товары для дома
    household_goods = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[2]/div[1]/div[2]/ul/li[7]/a')
    # кнопка Акции
    sales = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/a')
    # кнопка Главные книги
    main_books = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]/a')
    # кнопка Бонус за рецензию
    bonus = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[3]/a')
    # кнопка Сертификаты
    certificates = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[4]/a')
    # кнопка Только у нас
    exclusive = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[5]/a')
    # кнопка Предзаказы
    pre_order = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[6]/a')
    # кнопка Лабиринт.Сейчас
    lab_now = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[1]/a')
    # кнопка Детский навигатор
    child_now = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[2]/a')
    # кнопка Рецензии читателей
    reviews = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[3]/a')
    # кнопка Книжные обзоры
    book_reviews = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[4]/a')
    # кнопка Подборки читателей
    recommendations = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[5]/a')
    # кнопка Тесты
    lit_tests = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[6]/a')
    # кнопка Новости Л.
    news = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[7]/a')
    # кнопка Конкурсы
    contests = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[8]/a')
    # кнопка Спепцпроекты
    club = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[1]/div[2]/ul/li[9]/a')
    # кнопка Партнерам
    partner = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[2]/div[2]/ul/li[1]/a')
    # кнопка Наши вакансии
    job = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[3]/div[2]/div[2]/ul/li[2]/a')
    # кнопка Войти по коду скидки или через соцсеть
    login_1 = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[4]/div[1]/div[2]/ul/li[1]/a')
    # кнопка Вход и регистрация
    login_2 = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[4]/div[1]/div[2]/ul/li[2]/a')
    # кнопка Вы смотрели
    visited = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[4]/div[1]/div[2]/ul/li[3]/a')
    # кнопка Кабинет
    cabinet = WebElement(xpath='//*[@id="body-top"]/div[4]/div[2]/div/div[4]/div[1]/div[2]/ul/li[3]/a')
    # окно авторизации
    login = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    # кнопка Как сделать заказ
    order_help = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[1]/a')
    # кнопка Оплата
    payment = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[2]/a')
    # кнопка Курьерская доставка
    delivery = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[3]/a')
    # кнопка Поддержка
    support = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[4]/a')
    # кнопка Напишите нам
    mailto = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[5]/a')
    # кнопка Вся помощь
    help = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[6]/a')
    # кнопка Пользовательское соглашение
    agreement = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[7]/a')
    # кнопка СтопКовид
    stop_covid = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[3]/div[2]/div[2]/ul/li[3]/a')
    # кнопка Акит
    akit = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[3]/div[2]/div[2]/ul/li[4]/a')
    # кнопка Холдинг «Лабиринт»
    lab_hold = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[3]/div/div/a[1]')
    # кнопка 8 800 600-95-25
    contacts = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[3]/div/div/a[1]')
