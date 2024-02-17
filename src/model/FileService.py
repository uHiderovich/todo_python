from csv import DictReader, DictWriter
from os.path import exists


class FileService:
    """
    Класс для работы с файлами
    :param file_name: наименование файла
    :param fieldnames: список полей
    """
    def __init__(self, file_name, fieldnames):
        self.__file_name = file_name
        self.__fieldnames = fieldnames

        if not self.is_file_exists():
            self.create()

    def create(self):
        """
        Метод создания файла
        """
        with open(self.__file_name, 'w', encoding='utf-8') as data:
            f_writer = DictWriter(data, fieldnames=self.__fieldnames)
            f_writer.writeheader()

    def read(self):
        """
        Метод чтения файла
        :return: список словарей(строк)
        """
        with open(self.__file_name, 'r', encoding='utf-8') as data:
            f_reader = DictReader(data)
            return list(f_reader)

    def write(self, text):
        """
        Метод записи в файл
        :param text: текст для записи
        """
        res = self.read()
        with open(self.__file_name, 'w', encoding='utf-8', newline='') as data:
            res.append(text)
            f_writer = DictWriter(data, fieldnames=self.__fieldnames)
            f_writer.writeheader()
            f_writer.writerows(res)

    def rewrite(self, data_list):
        """
        Метод перезаписи файла
        :param data_list: список словарей(строк)
        """
        with open(self.__file_name, 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=self.__fieldnames)
            f_writer.writeheader()
            f_writer.writerows(data_list)

    def is_file_exists(self):
        """
        Метод проверки существования файла
        :return: True, если файл существует, иначе False
        """
        return exists(self.__file_name)
