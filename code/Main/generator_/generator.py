from generator.hand import hand
from music import music
from fingering import fingering

class generator:
    def __init__(self, music_ = None):
        self.__music = music.music()
        self.__fingering = fingering.fingering()
        self.__hand = hand.hand(0, 0)

        if music_ != None : 
            self.set(music_)
            
    def set(self, music_):
        self.__music.set(music_)

    def get(self):
        return self.__music

    def generate(self):
        """
        Generate의 기능 : 알고리즘을 통해 효율성을 고려한 fingering을 찾아
        music_sheet의 각 note 별로 fingering 정보를 수정하는 것
        """
        for notes_ in self.__music.get():
            self.__fingering.set(notes_)
        """
        Algorithms
        """
