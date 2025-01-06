from codecs import namereplace_errors


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def author(self):
        return self._author

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._name = name
        self._author = author
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, npages):
        if type(npages) != int:
            raise TypeError("Не соответствует int")
        elif npages <= 0:
            raise ValueError("Не может быть отрицательным")
        else:
            self._pages = npages

    def __str__(self):
        return (super().__str__() + f" Страницы {self._pages}")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._name = name
        self._author = author
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, nduration):
        if type(nduration) != float:
            raise TypeError("Не соответствует float")
        elif nduration <= 0:
            raise ValueError("Не может быть отрицательным")
        else:
            self._duration = nduration

    def __str__(self):
        return (super().__str__() + f" Продолжительность {self._duration}")
