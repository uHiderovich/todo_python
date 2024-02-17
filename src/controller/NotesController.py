from src.model.exeptions.AddNoteException import AddNoteException
from src.model.exeptions.FindNoteException import FindNoteException


class NotesController:
    def __init__(self, notes_view, notes_model):
        self.notes_view = notes_view
        self.notes_model = notes_model

    def run(self):
        while True:
            self.notes_view.print_menu()
            command = self.notes_view.get_command()
            if command == 'add':
                self.add_note()
            elif command == 'update':
                self.update_note()
            elif command == 'delete':
                self.delete_note()
            elif command == 'show':
                self.show_notes()
            elif command == 'exit':
                self.exit()
                break
            else:
                print('Неизвестная команда. Попробуйте еще раз.')

    def add_note(self):
        try:
            title, description = self.notes_view.get_note_info_for_add()
            self.notes_model.add_note(title, description)
            self.notes_view.print_add_success()
        except AddNoteException as e:
            self.notes_view.print_error_add(e)

    def update_note(self):
        note_number = self.notes_view.get_note_info_for_update()
        note = None

        try:
            note = self.notes_model.get_note_by_number(note_number)
        except FindNoteException as e:
            self.notes_view.print_message(e.message)
            return

        self.notes_view.print_selected_note(note)

        new_title = self.notes_view.get_note_title(is_update=True) or note.get_title()
        new_description = self.notes_view.get_note_description(is_update=True) or note.get_description()

        try:
            self.notes_model.update_note(note, new_title, new_description)
            self.notes_view.print_update_success()
        except AddNoteException as e:
            self.notes_view.print_error_add(e)

    def delete_note(self):
        note_number = self.notes_view.get_note_info_for_delete()
        try:
            self.notes_model.delete_note(note_number)
            self.notes_view.print_delete_success()
        except FindNoteException as e:
            self.notes_view.print_message(e.message)

    def show_notes(self):
        notes = self.notes_model.get_all()
        self.notes_view.print_notes(notes)

    def exit(self):
        self.notes_view.print_exit()
        exit(0)

