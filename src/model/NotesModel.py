from src.model.Note import Note
from src.model.exeptions.AddNoteException import AddNoteException
from src.model.exeptions.FindNoteException import FindNoteException


class NotesModel:
    def __init__(self):
        self.__notes = []

    def add_note(self, title, description, date=None):
        self.validate_note_data(title, description)
        note = Note(title, description, date)
        self.__notes.append(note)
        return note

    def update_note(self, note, title, description):
        self.validate_note_data(title, description)
        note.update(title, description)

    def delete_note(self, note_number):
        self.validate_note_number(note_number)
        self.__notes.pop(note_number - 1)

    def get_all(self):
        return self.__notes

    def get_note_by_number(self, number):
        self.validate_note_number(number)
        return self.__notes[number - 1]

    def validate_note_data(self, title, description):
        if not title or not description:
            raise AddNoteException('Необходимо заполнить все поля', title, description)

    def validate_note_number(self, number):
        if number < 1 or number > len(self.__notes):
            raise FindNoteException('Заметка с таким номером не найдена')