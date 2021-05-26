from generator.hand import hand
from music import music
import guitarpro

class Generator :
    def __init__(self, music_ = None, size_ = None, length_ = None) :
        self.__music = music.Music()
        self.__hand = hand.Hand(size_, length_)

        if type(music_) == guitarpro.models.Song :
            musics = []

            for tr in music_.tracks :
                for ms in tr.measures :
                    measure = []
                    for vc in ms.voices :
                        for bt in vc.beats :
                            beat = []
                            for nt in bt.notes :
                                note = [nt.string, nt.value, 0]
                                beat.append(note)
                            measure.append(beat)
                    musics.append(measure)
                    
            self.set(musics)
            
        elif music_ != None : 
            self.set(music_)
            
    def set(self, music_) :
        self.__music.set(music_)

    def get(self) :
        return self.__music

    def generate(self) :
        for measure in self.__music.get() :
            for idx, notes_ in enumerate(measure) :
                self.__set_init_fingering(notes_)

    def __set_init_fingering(self, notes_) :
        fret_list = []
        overlap = -1
        count = 0
        for note1 in notes_.get() :
            if note1.get("fret") != 0 :
                if note1.get("fret") not in fret_list :
                    fret_list.append(note1.get("fret"))
                else :
                    overlap = note1.get("fret")
                    count = count + 1
        fret_list.sort()
        if len(fret_list) != 0 :
            if overlap == -1 :
                for note1 in notes_.get() :
                    for idx in range(0,len(fret_list)) :
                        if fret_list[idx] == note1.get("fret") :
                            note1.set(None, None, idx + 1)
                            break
            else :
                if count > 1 :
                    for note1 in notes_.get() :
                        for idx in range(0, len(fret_list)) :
                            if fret_list[idx] == note1.get("fret") :
                                note1.set(None, None, idx + 1)
                                break
                else :
                    temp_list = []
                    for note1 in notes_.get() :
                        for idx in range(0,len(fret_list)) :
                            if fret_list[idx] == note1.get("fret") :
                                if fret_list[idx] > overlap :
                                    note1.set(None, None, idx + 2)
                                    break
                                else :
                                    note1.set(None, None, idx + 1)
                                    if fret_list[idx] == overlap :
                                        temp_list.append(note1)
                                    break

                    if len(temp_list) == 2 :
                        if temp_list[0].get("string") > temp_list[1].get("string") :
                            temp_list[1].set(None, None, temp_list[1].get("finger") + 1)
                        else :
                            temp_list[0].set(None, None, temp_list[0].get("finger") + 1)

    def __get_distance(self, string_1, string_2, fret_1, fret_2) :
        return abs(string_1 - string_2)**2 + abs(fret_1 - fret_2)**2

    def __get_direction(self, fret_1, fret_2):
        if fret_1 > fret_2 :
            return -1
        elif fret_1 == fret_2 :
            return 0
        else :
            return 1
