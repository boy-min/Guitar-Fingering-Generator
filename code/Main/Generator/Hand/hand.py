class hand :
    def __init__(self) :
        self.__size   = 0
        self.__length = 0

    def SetHand(self, size, length) :
        self.__size   = size
        self.__length = length

    def GetHand(self) :
        return [self.__size, self.__length]
