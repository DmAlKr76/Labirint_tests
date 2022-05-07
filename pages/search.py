import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class Search(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/search/'
        super().__init__(web_driver, url)

    '''search'''

    # поле основного поиска на главной странице
    search = WebElement(id='search-field')
    # кнопка основного поиска
    search_run_button = WebElement(xpath='//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]')
    # названия книг в результатах поиска
    products_titles = ManyWebElements(xpath='//a[@class="product-title-link"]')
    # сообщение об ошибке поиска на главной странице
    msg_search_er = WebElement(xpath='//*[@id="search"]/div[1]/h1')
    # тип товара в результатах поиска
    products_types = ManyWebElements(xpath='//span[@class="card-label__text card-label__text_inversed"]')

    # кнопка Прочие товары
    without_others_products_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Прочие")]')
    # кнопка Бумажные книги
    without_paper_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Бумажные")]')
    # кнопка Электронные книги
    without_electronic_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Электронные")]')
    # кнопка Предзаказ
    sort_products_by_type_order = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Предзаказ")]')
    # кнопка Ожидаются
    sort_products_by_type_waiting = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Ожидаются")]')
    # кнопка Нет в продаже
    sort_products_by_type_out_of_stock = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Нет в продаже")]')
    # кнопка В наличии
    sort_products_by_type_in_stock_is = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"В наличии")]')

    # кнопка ТИП ТОВАРА
    product_type = WebElement(xpath='//span[@class="navisort-item__content" and contains(text(),"ТИП ТОВАРА")]')
    # в выпадающем списке - строка Бумажные книги
    paper_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Бумажные")]')
    # в выпадающем списке - строка Другие товары
    other_goods = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Другие")]')
    # кнопка Показать
    show_button = WebElement(xpath='//input[@class="w100p show-goods__button" and @value="Показать"]')
    # в выпадающем списке - строка Электронные книги
    electronic_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Электронные")]')


    # кнопка НАЛИЧИЕ
    product_stock = WebElement(xpath='//span[@class="navisort-item__content" and contains(text(),"НАЛИЧИЕ")]')
    # в выпадающем списке - строка В наличии
    in_stock = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"В наличии")]')
    # в выпадающем списке - строка Предзаказ
    pre_order = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Предзаказ")]')
    # кнопка Показать
    show_button_stock = WebElement(xpath='//input[@class="w100p show-goods__button" and @value="Показать"]')
    # в выпадающем списке - строка Ожидаются
    waiting = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Ожидаются")]')
    # в выпадающем списке - Нет в продаже
    out_of_stock = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Нет в продаже")]')



    # кнопка Авторы
    authors_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[2]/a/span[1]')
    # список авторов в результатах поиска
    authors_names = ManyWebElements(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]')  # /a/span[1]
    # кнопка выбора первого автора
    our_author_button = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[1]')

    # кнопка Изд-ва
    publishing_offices_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[3]/a/span[1]')
    # список издательств в результатах поиска
    publishing_offices = ManyWebElements(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]')    # /a/span[1]
    # кнопка выбора издательста "Эком"
    publishing_office_button = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a/span[1]')

    # кнопка Серии
    product_series_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[4]/a/span[1]')
    # список серий товаров в результатах поиска
    product_series = ManyWebElements(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]')    # /a/span[1]
    # кнопка выбора первой из списка серии "Marvel — Избранное Parallel Comics"
    product_part_button = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[1]/span[1]')

    # кнопка Видео
    video_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[9]/a/span[1]')
    # список видео в результатах поиска
    video_products = ManyWebElements(
        xpath='//a[@class="rubric-list-item videobloc-carousel-item js-videoblock-video-show"]')
    # кнопка выбора первого из списка видео
    product_video_button = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[1]/span')

    # кнопка Темы
    themes_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[3]/a/span[1]')
    # список тем в результатах поиска
    themes_products = ManyWebElements(xpath='//a[@class="rubric-list-item"]')
    # кнопка выбора первой темы
    theme_button = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[1]')

    # кнопка Обзоры
    reviews_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[4]/a/span[1]')
    # список обзоров в результатах поиска
    reviews_products = ManyWebElements(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]')
    # # кнопка выбора первого обзора
    # review_button = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[1]')

    # кнопка Новости
    news_button = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[6]/a/span[1]')
    # список новостей в результатах поиска
    news_products = ManyWebElements(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]')

