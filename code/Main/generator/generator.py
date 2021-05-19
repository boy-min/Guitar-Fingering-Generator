from generator.hand import hand
from music import music
from fingering import fingering
import guitarpro

class Generator :
    def __init__(self, music_ = None) :
        self.__music = music.Music()
        self.__fingering = fingering.Fingering()
        self.__hand = hand.Hand(0, 0)

        if type(music_) == guitarpro.models.Song:
            musics = []

            for tr in music_.tracks:
                for ms in tr.measures:
                    for vc in ms.voices:
                        for bt in vc.beats:
                            beat = []
                            for nt in bt.notes:
                                note = [nt.string, nt.value, 0]
                                beat.append(note)
                            musics.append(beat)
            self.set(musics)
            
        elif music_ != None : 
            self.set(music_)
            
    def set(self, music_) :
        self.__music.set(music_)

    def get(self) :
        return self.__music

    def generate(self) :
        #  generate efficient fingering and edit fingering in self.__music

        #  set initial fingering
        for notes_ in self.__music.get() :
            self.__fingering.set(notes_)

        #  generate efficient fingering
        #  algorithms here
