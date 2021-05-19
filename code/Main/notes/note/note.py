import sys

class Note :
    def __init__(self, note_ = None) :
        self.__string = 0
        self.__fret = 0
        self.__finger = 0

        if note_ != None :
            if type(note_) == list :
                if len(note_) == 3 :
                    self.set(note_[0], note_[1], note_[2])

                elif len(note_) == 2 :
                    self.set(note_[0], note_[1], 0)

                else :
                    sys.exit("WrongParameterNumberError")
            else :
                sys.exit("WrongParameterTypeError")

    def __eq__(self, other) :
        return self.get('string') == other.get('string') and self.get('fret') == other.get('fret')

    def set(self, string = None, fret = None, finger = None) :
        if string != None :
            self.__string = string
        if fret != None :
            self.__fret = fret
        if finger != None :
            self.__finger = finger

    def get(self, key = None) :
        if key == None :
            return {'string' : self.__string, 'fret' : self.__fret, 'finger' : self.__finger}

        return {'string' : self.__string, 'fret' : self.__fret, 'finger' : self.__finger}.get(key)

    def show(self) :
        print(self.__string, self.__fret, self.__finger)
