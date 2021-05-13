from Notes.Note import note

class notes :
    def __init__(self) :
        self.__list = []

    def Append(self, n) :
        self.__list.append(n)

    def Delete(self, n) :
        if n < len(self.__list) :
            del self.__list[n]
        else :
            print("OutOfRangeError")

    def GetList(self) :
        return self.__list
