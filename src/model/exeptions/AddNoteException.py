class AddNoteException(Exception):
    def __init__(self, message, title, description):
        super().__init__(message)
        self.message = message
        self.title = title
        self.description = description

