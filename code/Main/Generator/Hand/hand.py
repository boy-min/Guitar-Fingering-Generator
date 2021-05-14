class hand:
    def __init__(self, size=0, length=0):
        self.__size = size
        self.__length = length

    def SetHand(self, size, length):
        self.__size = size
        self.__length = length

    def GetHand(self):
        return [self.__size, self.__length]
