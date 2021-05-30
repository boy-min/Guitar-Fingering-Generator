import sys
from notes import notes

class Music:
    def __init__(self, music_ = None):
        self.__music = []
        if music_ is not None:
            self.set(music_)

    def set(self, music_):
        if type(music_) == list:
            self.__music = [[notes.Notes(notes_) for notes_ in measure] for measure in music_]
        else:
            sys.exit("WrongParameterTypeError")

    def get(self):
        return self.__music
