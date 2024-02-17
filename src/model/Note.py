from datetime import datetime


class Note:
    """
    Класс представляющий собой заметку.
    :param title: заголовок заметки
    :param description: текст заметки
    :param note_id: идентификатор заметки
    :param date: дата создания заметки
    """
    id = 0

    def __init__(self, title, description, note_id=None, date=None):
        Note.id += 1
        self.__id = int(note_id) or Note.id
        self.__title = title
        self.__description = description
        self.__date = date or datetime.today().strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return f"{self.__id}. {self.__date}. {self.__title}\n{self.__description}"

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def update(self, title, description):
        """
        Метод обновления заметки.
        :param title: новый заголовок
        :param description: новый текст
        """
        self.__title = title
        self.__description = description
        self.__date = datetime.today().strftime('%d.%m.%Y %H:%M')
