from Generator.Hand import hand
from Music import music
from Fingering import fingering


class generator:
    def __init__(self):
        self.__music = music.music()
        self.__fingering = fingering.fingering()
        self.__hand = hand.hand(0, 0)

    def SetMusicSheet(self, music_sheet):
        self.__music.SetMusic(music_sheet)

    def GetMusicSheet(self):
        return self.__music.GetMusic()

    def Generate(self) :
        """
        Generate의 기능 : 알고리즘을 통해 효율성을 고려한 fingering을 찾아
        music_sheet의 각 note 별로 fingering 정보를 수정하는 것
        """
        for i in self.__music.GetMusic():
            self.__fingering.SetFingering(i)
        """
        Algorithms
        """