from src.model.FileService import FileService
from src.model.Note import Note
from src.model.NotesModel import NotesModel

base_file_name = 'notes.csv'


class NotesFileBehaviourDecorator(NotesModel):
    def __init__(self):
        super().__init__()
        self.__file_service = FileService(base_file_name, ['title', 'description', 'date'])
        self.fill_notes()

    def add_note(self, title, description, date=None):
        note = super().add_note(title, description, date)
        self.save_note(note)

    def delete_note(self, note_number):
        super().delete_note(note_number)
        self.save_notes()

    def update_note(self, note, title, description):
        super().update_note(note, title, description)
        self.save_notes()

    def save_note(self, note):
        self.__file_service.write(self.get_note_save_data(note))

    def save_notes(self):
        result_list = list()
        for note in super().get_all():
            result_list.append(self.get_note_save_data(note))
        self.__file_service.rewrite(result_list)

    def fill_notes(self):
        for line in self.__file_service.read():
            super().add_note(line['title'], line['description'], line['date'])

    def get_note_save_data(self, note):
        return {
            'title': note.get_title(),
            'description': note.get_description(),
            'date': note.get_date()
        }
