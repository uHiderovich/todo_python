class NotesView:
    def __init__(self):
        pass

    def print_notes(self, notes):
        print('-------------------')
        print('Список заметок:')
        for index, note in enumerate(notes, 1):
            print(f"{index}. {note}")
        print('-------------------')

    def print_menu(self):
        print('-------------------')
        print('Меню:')
        print('1. add для добавления заметки')
        print('2. update для обновления заметки')
        print('3. delete для удаления заметки')
        print('4. show для просмотра всех заметок')
        print('5. exit для выхода из программы')
        print('-------------------')

    def get_command(self):
        return self.promnt('Введите команду: ')

    def get_note_info_for_add(self):
        title = self.get_note_title()
        description = self.get_note_description()
        return title, description

    def get_note_info_for_delete(self):
        return int(self.promnt('Введите номер заметки из списка для удаления: '))

    def get_note_info_for_update(self):
        return int(self.promnt('Введите номер заметки из списка для обновления: '))

    def get_note_title(self, is_update=False):
        help_message = ' (оставьте пустым, если не хотите обновлять)' if is_update else ''
        return self.promnt(f'Введите заголовок заметки{help_message}: ')

    def get_note_description(self, is_update=False):
        help_message = ' (оставьте пустым, если не хотите обновлять)' if is_update else ''
        return self.promnt(f'Введите тело заметки{help_message}: ')

    def print_selected_note(self, note):
        print('Выбранная заметка: ')
        print(str(note))

    def print_add_success(self):
        print('Заметка успешно добавлена!')

    def print_update_success(self):
        print('Заметка успешно обновлена!')

    def print_delete_success(self):
        print('Заметка успешно удалена!')

    def print_error_add(self, e):
        error_message = e.message
        if not e.title:
            error_message += '\n' + 'Необходимо заполнить добавть заголовок"'
        if not e.description:
            error_message += '\n' + 'Необходимо заполнить добавть описание"'
        print(error_message)

    def print_message(self, message):
        print(message)

    def print_exit(self):
        print('Выход из программы')

    def promnt(self, message):
        return input(message)
