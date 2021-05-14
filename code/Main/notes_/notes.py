import sys
from notes.note import note

class notes:
    def __init__(self, notes_ = None):
        self.__notes = []
        self.set(notes_)

    def set(self, notes_) :
        self.__notes = [note.note(note_) for note_ in notes_]
    
    def get(self):
        return self.__notes

    def show(self, index = -1) :
        if index == -1 : 
            for note_ in self.__notes :
                note_.show()
                
        else :
            if index < len(self.__notes) :
                self.__notes[index].show()

            else :
                sys.exit("OutOfRangeError")
