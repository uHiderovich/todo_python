from src.model.Note import Note
from src.model.exeptions.AddNoteException import AddNoteException
from src.model.exeptions.FindNoteException import FindNoteException


class NotesModel:
    def __init__(self):
        self.__notes = []

    def add_note(self, title, description, note_id=None, date=None):
        self.validate_note_data(title, description)
        note = Note(title, description, note_id, date)
        self.__notes.append(note)
        return note

    def update_note(self, note, title, description):
        self.validate_note_data(title, description)
        note.update(title, description)

    def delete_note(self, note_id):
        try:
            self.__notes.remove(self.get_note_by_id(note_id))
        except FindNoteException as e:
            raise e

    def get_all(self):
        return self.__notes

    def get_note_by_id(self, note_id):
        for note in self.__notes:
            if note.get_id() == note_id:
                return note
        raise FindNoteException(f"Заметка с ID {note_id} не найдена")

    def get_note_by_date(self, date):
        result = []
        for note in self.__notes:
            if note.get_date().find(date) != -1:
                result.append(note)
        return result

    def validate_note_data(self, title, description):
        if not title or not description:
            raise AddNoteException('Необходимо заполнить все поля', title, description)

