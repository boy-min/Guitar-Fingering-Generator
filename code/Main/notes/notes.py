import sys
from notes.note import note

class Notes:
    def __init__(self, notes_ = None):
        self.__notes = []
        if notes_ is not None:
            self.set(notes_)

    def set(self, notes_):
        if type(notes_) == list:
            self.__notes = [note.Note(note_) for note_ in notes_]

        else:
            sys.exit("WrongParameterTypeError")

    def get(self):
        return self.__notes
