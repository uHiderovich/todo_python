class NotesView:
    def __init__(self):
        pass

    def print_notes(self, notes):
        print('-------------------')
        print('Список заметок:')
        for note in notes:
            print(f"ID заметки {note.get_id()}. Дата: {note.get_date()}. Заголовок: {note.get_title()}")
        print('-------------------')

    def print_menu(self):
        print('-------------------')
        print('Меню:')
        print('1. add для добавления заметки')
        print('2. update для обновления заметки')
        print('3. delete для удаления заметки')
        print('4. show_all для просмотра всех заметок')
        print('5. show_by_id для просмотра заметки по ее id')
        print('6. find для поиска по дате')
        print('7. exit для выхода из программы')
        print('-------------------')

    def get_command(self):
        return self.promnt('Введите команду: ')

    def get_note_info_for_add(self):
        title = self.get_note_title()
        description = self.get_note_description()
        return title, description

    def get_note_id(self):
        return int(self.promnt('Введите id заметки: '))

    def get_note_title(self, is_update=False):
        help_message = ' (оставьте пустым, если не хотите обновлять)' if is_update else ''
        return self.promnt(f'Введите заголовок заметки{help_message}: ')

    def get_note_description(self, is_update=False):
        help_message = ' (оставьте пустым, если не хотите обновлять)' if is_update else ''
        return self.promnt(f'Введите тело заметки{help_message}: ')

    def print_selected_note(self, note):
        print('Выбранная заметка: ')
        print(f"ID заметки {note.get_id()}. Дата: {note.get_date()}. Заголовок: {note.get_title()}")
        print(note.get_description())

    def print_add_success(self):
        print('Заметка успешно добавлена!')

    def print_update_success(self):
        print('Заметка успешно обновлена!')

    def print_delete_success(self):
        print('Заметка успешно удалена!')

    def print_nothing_to_update(self):
        print('Нечего обновлять!')

    def print_error_add(self, e):
        error_message = e.message
        if not e.title:
            error_message += '\n' + 'Необходимо заполнить добавть заголовок"'
        if not e.description:
            error_message += '\n' + 'Необходимо заполнить добавть описание"'
        print(error_message)

    def get_date_for_find(self):
        message = 'Введите дату для поиска в формате в одном из форматов: '
        format_1 = '\n<день>.<месяц>.<год>'
        format_2 = '\n<день>.<месяц>.<год> <час>:<минута>\n'
        return self.promnt(message + format_1 + format_2)

    def print_message(self, message):
        print(message)

    def print_exit(self):
        print('Выход из программы')

    def promnt(self, message):
        return input(message)
