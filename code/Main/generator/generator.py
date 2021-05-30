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
        music_ = []
        for measure_ in self.__music.get() :
            for notes_ in measure_ :
                music_.append(notes_)
        dp = [[[0, -1] for col in range(len(music_))] for row in range(4096)]
        for i in reversed(range(len(music_))) :
            if i == len(music_) - 1 :
                min_ = 2147483647
                for finger1 in range(4**len(music_[i].get())) :
                    fingers1 = []
                    for j in range(len(music_[i].get())) :
                        fingers1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                    dp[finger1][i][0] = self.__difficulty(music_[i],fingers1)
            else :
                min_ = 2147483647
                for finger1 in range(4**len(music_[i].get())) :
                    fingers1 = []
                    for j in range(len(music_[i].get())) :
                        fingers1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                    for finger2 in range(4**len(music_[i].get())) :
                        dif = dp[finger2][i+1][0] + self.__difficulty(music_[i],fingers1,music_[i+1],dp[finger2][i+1][0])
                        if min_ > dif :
                            min_ = dif
                            dp[finger1][i][1] = finger2

        finger_list = []
        min_ = 2147483647
        idx = -1
        for i in range(len(music_)) :
            if i == 0 :
                for finger in range(4**len(music_[i].get())) :
                    if min_ > dp[finger][i][0] :
                        min_ = dp[finger][i][0]
                        idx = finger
                fingers = []
                for j in range(len(music_[i].get())) :
                    fingers.append((idx % (4 ** (j + 1))) // (4 ** j))
                finger_list.append(fingers)
                idx = dp[idx][i][1]
            else :
                fingers = []
                for j in range(len(music_[i].get())) :
                    fingers.append((idx % (4 ** (j + 1))) // (4 ** j))
                finger_list.append(fingers)
                idx = dp[idx][i][1]

        for idx1, notes_ in enumerate(music_) :
            for idx2, note_ in enumerate(notes_.get()) :
                note_.set(None, None, finger_list[idx1][idx2] + 1)

    def __difficulty(self, notes_1 = None, finger_list_1 = None, notes_2 = None, finger_list_2 = None) :
        if notes_2 == None and finger_list_2 == None :
            return 0
        else :
            return 0