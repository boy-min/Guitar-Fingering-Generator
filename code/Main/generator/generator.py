from generator.hand import hand
from music import music
import guitarpro

class Generator:
    def __init__(self, music_ = None, size_ = None, length_ = None):
        self.__music = music.Music()
        self.__hand = hand.Hand(size_, length_)
        self.__weight = [1000, 100, 50, 10]

        if type(music_) == guitarpro.models.Song:
            musics = []

            for tr in music_.tracks:
                for ms in tr.measures:
                    measure = []
                    for vc in ms.voices:
                        for bt in vc.beats:
                            beat = []
                            for nt in bt.notes:
                                note = [nt.string, nt.value, 0]
                                beat.append(note)
                            measure.append(beat)
                    musics.append(measure)
                    
            self.set(musics)
            
        elif music_ is not None:
            self.set(music_)
            
    def set(self, music_):
        self.__music.set(music_)

    def get(self):
        return self.__music

    def generate(self):
        music_ = []
        for measure_ in self.__music.get():
            for idx, notes_ in enumerate(measure_):
                if idx != len(measure_) - 1:
                    pop_list = []
                    for idx2 in range(len(notes_.get())):
                        if notes_.get()[idx2].get("fret") == 0:
                            pop_list.append(idx2)
                    count = 0
                    for i in pop_list:
                        notes_.get().pop(i-count)
                        count += 1
                    music_.append(notes_)
        dp = [[[0, -1] for col in range(4097)] for row in range(len(music_))]
        for i in reversed(range(len(music_))):
            if i == len(music_) - 1:
                if len(music_[i].get()) == 0:
                    dp[i][4096][0] = 0
                else:
                    for finger1 in range(4**len(music_[i].get())):
                        fingers1 = []
                        for j in range(len(music_[i].get())):
                            fingers1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                        dp[i][finger1][0] = self.__difficulty(music_[i],fingers1,None,None)
            else:
                if len(music_[i].get()) == 0:
                    if len(music_[i+1].get()) == 0:
                        dp[i][4096][0] = dp[i+1][4096][0]
                        dp[i][4096][1] = 4096
                    else:
                        min_ = 2147483647
                        for finger2 in range(4 ** len(music_[i+1].get())):
                            fingers2 = []
                            for j in range(len(music_[i+1].get())):
                                fingers2.append((finger2 % (4 ** (j + 1))) // (4 ** j))
                            dif = dp[i+1][finger2][0] + self.__difficulty(None,None,music_[i+1],fingers2)
                            if min_ > dif:
                                min_ = dif
                                dp[i][4096][1] = finger2
                        dp[i][4096][0] = min_
                else:
                    if len(music_[i + 1].get()) == 0:
                        for finger1 in range(4 ** len(music_[i].get())):
                            fingers1 = []
                            for j in range(len(music_[i].get())):
                                fingers1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                            dp[i][finger1][0] = dp[i+1][4096][0] + self.__difficulty(music_[i],fingers1,None,None)
                            dp[i][finger1][1] = 4096
                    else:
                        for finger1 in range(4**len(music_[i].get())):
                            fingers1 = []
                            for j in range(len(music_[i].get())):
                                fingers1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                            min_ = 2147483647
                            for finger2 in range(4**len(music_[i+1].get())):
                                fingers2 = []
                                for j in range(len(music_[i+1].get())):
                                    fingers2.append((finger2 % (4 ** (j + 1))) // (4 ** j))
                                dif = dp[i+1][finger2][0] + self.__difficulty(music_[i],fingers1,music_[i+1],fingers2)
                                if min_ > dif:
                                    min_ = dif
                                    dp[i][finger1][1] = finger2
                            dp[i][finger1][0] = min_

        finger_list = []
        min_ = 2147483647
        idx = -1
        for i in range(len(music_)):
            if i == 0:
                if len(music_[i].get()) == 0:
                    fingers = []
                    finger_list.append(fingers)
                    idx = 4096
                else:
                    for finger in range(4**len(music_[i].get())):
                        if min_ > dp[i][finger][0]:
                            min_ = dp[i][finger][0]
                            idx = finger
                    fingers = []
                    for j in range(len(music_[i].get())):
                        fingers.append((idx % (4 ** (j + 1))) // (4 ** j))
                    finger_list.append(fingers)
                    idx = dp[i][idx][1]
            else:
                if len(music_[i].get()) == 0:
                    fingers = []
                    finger_list.append(fingers)
                    idx = dp[i][4096][1]
                else:
                    fingers = []
                    for j in range(len(music_[i].get())):
                        fingers.append((idx % (4 ** (j + 1))) // (4 ** j))
                    finger_list.append(fingers)
                    idx = dp[i][idx][1]

        for idx1, notes_ in enumerate(music_):
            for idx2, note_ in enumerate(notes_.get()):
                note_.set(None, None, finger_list[idx1][idx2] + 1)

    def __difficulty(self, notes_1, finger_list_1, notes_2, finger_list_2):
        return 0
