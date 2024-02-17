from src.controller.NotesController import NotesController
from src.model.NotesFileBehaviourDecorator import NotesFileBehaviourDecorator
from src.view.NotesView import NotesView

notes_controller = NotesController(NotesView(), NotesFileBehaviourDecorator())
notes_controller.run()
