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
        difficulty = 0
        difficulty += self.__check_highcode(notes_1, finger_list_1, notes_2, finger_list_2)
        if difficulty >= self.__weight[0]:
            return difficulty
        if notes_1 is None and finger_list_1 is None:
            if 3 in finger_list_2:
                difficulty += self.__weight[1]
            elif 2 in finger_list_2:
                difficulty += self.__weight[2]
            elif 1 in finger_list_2:
                difficulty += self.__weight[3]
            else:
                difficulty += 1
        elif notes_2 is None and finger_list_2 is None:
            if 3 in finger_list_1:
                difficulty += self.__weight[1]
            elif 2 in finger_list_1:
                difficulty += self.__weight[2]
            elif 1 in finger_list_1:
                difficulty += self.__weight[3]
            else:
                difficulty += 1
        else :
            if 3 in finger_list_1:
                difficulty += self.__weight[1]
            elif 2 in finger_list_1:
                difficulty += self.__weight[2]
            elif 1 in finger_list_1:
                difficulty += self.__weight[3]
            else:
                difficulty += 1
            if 3 in finger_list_2:
                difficulty += self.__weight[1]
            elif 2 in finger_list_2:
                difficulty += self.__weight[2]
            elif 1 in finger_list_2:
                difficulty += self.__weight[3]
            else:
                difficulty += 1
        return difficulty


    def __check_twist(self, notes_1, finger_list_1, notes_2, finger_list_2):
        difficulty = 0
        fret_list = []
        finger_list = []
        for idx, note_ in enumerate(notes_1.get()):
            fret_list.append(note_.get("fret"))
            finger_list.append(finger_list_1[idx])
        for i in range(len(fret_list) - 1):
            for j in range(len(fret_list) - 2 - i):
                if fret_list[j] > fret_list[j+1]:
                    temp = fret_list[j]
                    fret_list[j] = fret_list[j+1]
                    fret_list[j+1] = temp
                    temp = finger_list[j]
                    finger_list[j+1] = finger_list[j]
                    finger_list[j] = temp
        for idx in range(len(fret_list) - 1):
            if fret_list[idx] < fret_list[idx+1]:
                if finger_list[idx] >= finger_list[idx+1]:
                    return self.__weight[0]
            else:
                if finger_list[idx] != finger_list[idx+1]:
                    difficulty += self.__weight[1]
        return difficulty

    def __check_highcode(self, notes_1, finger_list_1, notes_2, finger_list_2):
        if notes_1 is not None and finger_list_1 is not None:
            is_notes1_highcode = False
            finger_1_count = [0, 0, 0, 0]
            for finger in finger_list_1:
                finger_1_count[finger] += 1
            for idx in range(4):
                if finger_1_count[idx] > 1:
                    if idx == 0:
                        is_notes1_highcode = True
                    else:
                        return self.__weight[0]
            if not is_notes1_highcode:
                return 0

            string_list_1 = []
            if is_notes1_highcode:
                fret = -1
                for idx, note_ in enumerate(notes_1.get()):
                    if fret == -1:
                        if finger_list_1[idx] == 0:
                            fret = note_.get("fret")
                            string_list_1.append(note_.get("string"))
                    else:
                        if finger_list_1[idx] == 0:
                            if fret != note_.get("fret"):
                                return self.__weight[0]
                            if note_.get("string") not in string_list_1:
                                string_list_1.append(note_.get("string"))

            string_list_1.sort()
            for idx in range(len(string_list_1) - 1):
                if string_list_1[idx] != string_list_1[idx + 1] - 1:
                    return self.__weight[0]

        if notes_2 is not None and finger_list_2 is not None:
            is_notes2_highcode = False
            finger_2_count = [0, 0, 0, 0]
            for idx in finger_list_2:
                finger_2_count[idx] += 1
                if finger_2_count[idx] > 1:
                    if idx == 0:
                        is_notes2_highcode = True
                    else:
                        return self.__weight[0]
            if not is_notes2_highcode:
                return 0

            string_list_2 = []
            if is_notes2_highcode:
                fret = -1
                for idx, note_ in enumerate(notes_2.get()):
                    if fret == -1:
                        if finger_list_2[idx] == 0:
                            fret = note_.get("fret")
                            string_list_2.append(note_.get("string"))
                    else:
                        if finger_list_2[idx] == 0:
                            if fret != note_.get("fret"):
                                return self.__weight[0]
                            if note_.get("string") not in string_list_2:
                                string_list_2.append(note_.get("string"))

            string_list_2.sort()
            for idx in range(len(string_list_2) - 1):
                if string_list_2[idx] != string_list_2[idx + 1] - 1:
                    return self.__weight[0]

        return 0
