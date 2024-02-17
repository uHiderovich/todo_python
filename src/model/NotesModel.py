from src.model.Note import Note
from src.model.exeptions.AddNoteError import AddNoteError
from src.model.exeptions.FindNoteError import FindNoteError


class NotesModel:
    """
    Класс NotesModel
    Представляет собой модель заметок. Он содержит методы для добавления, обновления, удаления и получения заметок.
    """
    def __init__(self):
        self.__notes = []

    def add_note(self, title, description, note_id=None, date=None):
        """
        Метод добавления заметки
        :param title: заголовок заметки
        :param description: текст заметки
        :param note_id: id заметки
        :param date: дата создания/изменения заметки
        :return Note: экземпляр добавленной заметки
        """
        self.validate_note_data(title, description)
        note = Note(title, description, note_id, date)
        self.__notes.append(note)
        return note

    def update_note(self, note, title, description):
        """
        Метод обновления заметки
        :param note: экземпляр заметки
        :param title: заголовок заметки
        :param description: текст заметки
        """
        self.validate_note_data(title, description)
        note.update(title, description)

    def delete_note(self, note_id):
        """
        Метод удаления заметки
        :param note_id: id заметки
        :raise FindNoteError: если заметка с указанным id не найдена
        """
        try:
            self.__notes.remove(self.get_note_by_id(note_id))
        except FindNoteError as e:
            raise e

    def get_all(self):
        """
        Метод получения всех заметок
        :return list[Note]: список всех заметок
        """
        return self.__notes

    def get_note_by_id(self, note_id):
        """
        Метод получения заметки по id
        :param note_id: id заметки
        :return Note: экземпляр заметки
        """
        for note in self.__notes:
            if note.get_id() == note_id:
                return note
        raise FindNoteError(f"Заметка с ID {note_id} не найдена")

    def get_note_by_date(self, date):
        """
        Метод получения заметок по дате
        :param date: дата создания/изменения заметки
        :return list[Note]: список заметок
        """
        result = []
        for note in self.__notes:
            if note.get_date().find(date) != -1:
                result.append(note)
        return result

    def validate_note_data(self, title, description):
        """
        Метод валидации данных заметки
        :param title: заголовок заметки
        :param description: текст заметки
        :raise AddNoteError: если не все поля заполнены
        """
        if not title or not description:
            raise AddNoteError('Необходимо заполнить все поля', title, description)
