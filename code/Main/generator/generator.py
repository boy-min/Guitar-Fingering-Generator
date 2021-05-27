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
        for measure in self.__music.get() :
            for notes_ in measure :
                music_.append(notes_)
        dp = [[[[-1, -1, -1, -1, -1, -1], 0, -1] for col in range(len(music_))] for row in range(4096)]
        for i in reversed(range(len(music_))) :
            print("Doing",i,"th try.")
            if i == len(music_) - 1 :
                min_ = 2147483647
                fingers1 = []
                for finger1 in range(4096):
                    for j in range(len(music_[i].get())):
                        fingers1.append((finger1 % (4 ** (6 - j))) / (4 ** (5 - j)))
                    dp[finger1][i][0] = fingers1
                    dp[finger1][i][1] = self.__difficulty(music_[i],fingers1)
            else :
                min_ = 2147483647
                fingers1 = []
                for finger1 in range(4096):
                    for j in range(len(music_[i].get())):
                        fingers1.append((finger1 % (4 ** (6 - j))) / (4 ** (5 - j)))
                    for finger2 in range(4096) :
                        dif = dp[finger2][i+1][1] + self.__difficulty(music_[i],fingers1,music_[i+1],dp[finger2][i+1][0])
                        if min_ > dif :
                            min_ = dif
                            dp[finger1][i][2] = finger2
        finger_list = []
        min_ = 2147483647
        idx = -1
        for i in range(len(music_)) :
            if i == 0 :
                for finger in range(4096) :
                    if min_ > dp[finger][i][1] :
                        min_ = dp[finger][i][1]
                        idx = finger
                finger_list.append(dp[idx][i][0])
                idx = dp[idx][i][2]
            else :
                finger_list.append(dp[idx][i][0])
                idx = dp[idx][i][2]
        for idx1, notes_ in enumerate(music_) :
            for idx2, note_ in enumerate(notes_.get()) :
                note_.set(None, None, finger_list[idx1][idx2])

    def __difficulty(self, notes1 = None, fingers1 = None, notes2 = None, fingers2 = None) :
        return 0