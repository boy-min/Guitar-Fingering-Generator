import sys
from notes import notes

class Music :
    def __init__(self, music_ = None) :
        self.__music = []
        if music_ != None :
            self.set(music_)

    def set(self, music_) :
        if type(music_) == list :
            self.__music = [notes.Notes(notes_) for notes_ in music_]
        else :
            sys.exit("WrongParameterTypeError")

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
