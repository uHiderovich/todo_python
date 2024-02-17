from src.model.FileService import FileService
from src.model.NotesModel import NotesModel

base_file_name = 'notes.csv'


class NotesFileBehaviourDecorator(NotesModel):
    """
    Класс NotesFileBehaviourDecorator
    Представляет собой модель заметок с сохранением в файл формата csv.
    Он содержит методы для добавления, обновления, удаления и получения заметок.
    """
    def __init__(self):
        super().__init__()
        self.__file_service = FileService(base_file_name, ['id', 'title', 'description', 'date'])
        self.fill_notes()

    def add_note(self, title, description, note_id=None, date=None):
        """
        Метод добавления заметки
        :param title: заголовок заметки
        :param description: текст заметки
        :param note_id: id заметки
        :param date: дата создания/изменения заметки
        :return Note: экземпляр добавленной заметки
        """
        note = super().add_note(title, description, note_id, date)
        self.save_note(note)

    def update_note(self, note, title, description):
        """
        Метод обновления заметки
        :param Note: экземпляр заметки
        :param title: заголовок заметки
        :param description: текст заметки
        """
        super().update_note(note, title, description)
        self.save_notes()

    def delete_note(self, note_id):
        """
        Метод удаления заметки
        :param note_id: id заметки
        :raise FindNoteError: если заметка с указанным id не найдена
        """
        super().delete_note(note_id)
        self.save_notes()

    def save_note(self, note):
        """
        Метод сохранения заметки в файл
        :param Note: экземпляр заметки
        """
        self.__file_service.write(self.get_note_save_data(note))

    def save_notes(self):
        """
        Метод сохранения всех заметок в файл
        """
        result_list = list()
        for note in super().get_all():
            result_list.append(self.get_note_save_data(note))
        self.__file_service.rewrite(result_list)

    def fill_notes(self):
        """
        Метод заполнения заметок из файла
        """
        for line in self.__file_service.read():
            super().add_note(line['title'], line['description'], line['id'], line['date'])

    def get_note_save_data(self, note):
        """
        Метод получения данных заметки для сохранения в файл
        :param Note: экземпляр заметки
        :return dict: данные заметки id, title, description, date
        """
        return {
            'id': note.get_id(),
            'title': note.get_title(),
            'description': note.get_description(),
            'date': note.get_date()
        }
