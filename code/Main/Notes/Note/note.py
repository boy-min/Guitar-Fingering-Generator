class note :
    def __init__(self, string = 0, fret = 0, finger = 0) :
        self.__string = string
        self.__fret   = fret
        self.__finger = finger
        
    def SetValue(self, string, fret, finger) :
        self.__string = string
        self.__fret   = fret
        self.__finger = finger

    def GetValue(self) :
        return [self.__string, self.__fret, self.__finger]
