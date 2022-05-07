import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPageBody(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    '''body'''

    # кнопка "Что почитать: выбор редакции"
    what_to_read_button = WebElement(xpath='//*[@id="right-inner"]/div[1]/div[1]/a')
    # названия книг на странице "Что почитать: выбор редакции"
    products_titles_large = ManyWebElements(xpath='//span[@class="product-title large-name"]')
    # заголовок страницы
    page_title = WebElement(xpath='//h1')
    # кнопка "Лучшая покупка дня"
    best_buy_button = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/div/div[1]/div[2]/div/h2/a')
    # карточка книг на странице
    products_carts = ManyWebElements(xpath='//a[@class="product need-watch watched"]')
    # кнопка "Больше книг со скидками"
    discounts_button = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/div/div[1]/div[2]/a')
    # описание скидки на книгу в результатах поиска
    discounts_books = ManyWebElements(xpath='//a[contains(@class, "card-label_profit")]')
    # кнопка "Читатели выбирают сегодня"
    today_button = WebElement(xpath='//*[@id="bottom"]/div[3]/div[1]/a')
    # карточки книг в результатах поиска
    products_books = ManyWebElements(xpath='//div[@class="product need-watch watched" and @data-dir="books"]')
    # кнопка "Лабиринт. Сейчас"
    now_button = WebElement(xpath='//*[@id="bottom"]/div[4]/div[1]/noindex/a')
    # активный пункт горизонтального меню, который соответсвует содержанию открывшейся страницы
    active_menu_item = WebElement(xpath='//a[@class="mm-link mm-link-big mm-link-big-m-sub active"]')
    # кнопка "Детский навигатор — что читать детям и с детьми"
    kids_button = WebElement(xpath='//*[@id="bottom"]/div[5]/div[1]/noindex/a')
    # кнопка "Книжные лидеры продаж"
    leaders_button = WebElement(xpath='//*[@id="bottom"]/div[11]/div[1]/a')
    # кнопка "Книги: новинки 2022"
    novelties_books_button = WebElement(xpath='//*[@id="bottom"]/div[13]/div[1]/a')
    # кнопка "Книжные обзоры и рецензии"
    reviews_button = WebElement(xpath='//*[@id="bottom"]/div[16]/a')
    # заголовок на открывшейся странице "Книжные обзоры и рецензии"
    heading_reviews = WebElement(xpath='//div[@class="ratingh h1"]')
    # кнопка "Правила" в разделе "Вам подарок!"
    regulations_button = WebElement(xpath='//*[@id="left"]/div[1]/form/div[1]/p/a')


