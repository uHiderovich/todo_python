from datetime import datetime


class Note:
    def __init__(self, title, description, date=None):
        self.__title = title
        self.__description = description
        self.__date = date or datetime.today().strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return f"{self.__date}. {self.__title}\n{self.__description}"

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def update(self, title, description):
        self.__title = title
        self.__description = description
        self.__date = datetime.today().strftime('%Y-%m-%d-%H:%M')
