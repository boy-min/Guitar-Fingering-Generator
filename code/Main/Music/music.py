import sys, os
from Notes import notes

class music :
    def __init__(self) :
        self.__m_music = []
        
    def Append(self, n) :
        self.__m_music.append(n)

    def Delete(self, n) :
        if n < len(self.__m_music) :
            del self.__m_music[n]

        else :
            print("OutOfRangeError")

    def GetMusic(self) :
        return __m_music
