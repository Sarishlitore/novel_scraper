import time
from abc import abstractmethod, ABC

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from book.book import Book


class Source(ABC):
    def __init__(self, book_url: str, book_title_xpath: str, book_author_xpath: str):
        self._book_url = book_url
        self.__book_title_xpath = book_title_xpath
        self.__book_author_xpath = book_author_xpath

    @classmethod
    @abstractmethod
    def form_source(cls, book_url: str, first_chapter_url: str, last_chapter_url: str):
        pass

    def _form_book(self, driver: uc, sleep_time) -> Book:
        driver.get(self._book_url)
        time.sleep(sleep_time)
        book_title = driver.find_element(By.XPATH, self.__book_title_xpath).text
        book_author = driver.find_element(By.XPATH, self.__book_author_xpath).text
        return Book(_title=book_title, _author=book_author)
