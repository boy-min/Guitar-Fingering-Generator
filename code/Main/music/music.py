import sys
from notes import notes

class music:
    def __init__(self, music_ = None):
        self.__music = []
        if music_ != None :
            self.set(music_)

    def set(self, music_):
        self.__music = [notes.notes(notes_) for notes_ in music_]

    def get(self) :
        return self.__music

    def show(self, index = -1) :
        if index == -1 : 
            for i, notes_ in enumerate(self.__music) :
                print("notes #", i + 1, sep = '')
                notes_.show()

        else :
            if index < len(self.__music) :
                print("notes #", index + 1, sep = '')
                self.__music[index].show()
                
            else :
                sys.exit("OutOfRangeError")
