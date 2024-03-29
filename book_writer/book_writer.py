from abc import ABC, abstractmethod

from book.book import Book


class BookWriter(ABC):
    @abstractmethod
    def write(self, book: Book, dirname: str):
        pass



