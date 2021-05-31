from generator.hand import hand
from music import music
import guitarpro

class Generator:
    def __init__(self, music_ = None, size_ = None, length_ = None):
        self.__music = music.Music()
        self.__hand = hand.Hand(size_, length_)
        self.__weight = [1000]

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
        difficulty += self.__check_highcode(notes_1, finger_list_1)
        difficulty += self.__check_highcode(notes_2, finger_list_2)
        difficulty += self.__check_twist(notes_1, finger_list_1)
        difficulty += self.__check_twist(notes_2, finger_list_2)
        if difficulty >= self.__weight[0]:
            return difficulty

        if notes_1 is not None and notes_2 is None:
            difficulty += self.__get_dif(notes_1, finger_list_1)
        elif notes_1 is None and notes_2 is not None:
            difficulty += self.__get_dif(notes_2, finger_list_2)
        else:
            difficulty += self.__get_dif(notes_1, finger_list_1)
            difficulty += self.__get_dif(notes_2, finger_list_2)
            pos_of_hand_1 = self.__get_pos(notes_1, finger_list_1)
            pos_of_hand_2 = self.__get_pos(notes_2, finger_list_2)
            # 여러 정보 (손의 중심에 따른 이동 거리, 손가락들 사이의 거리, 손가락들 사이의 모양이 변하는 정도 등)
            # 를 이용하여 운지법의 변화에 따른 difficulty 의 값을 반환하는 알고리즘

        return difficulty

    def __get_pos(self, notes, finger_list):
        return 0
        # 손의 중심 번호를 반환하는 알고리즘

    def __get_dif(self, notes, finger_list):
        return 0
        # 하나의 notes에 대하여 얼마나 운지하기 어려운지 판단하는 알고리즘

    def __check_twist(self, notes, finger_list):
        if notes is not None and finger_list is not None:
            temp_list = []
            for idx, note_ in enumerate(notes.get()):
                temp_list.append([note_.get("fret"), finger_list[idx]])
            temp_list.sort()
            for idx in range(len(temp_list) - 1):
                if temp_list[idx][0] < temp_list[idx+1][0]:
                    if temp_list[idx][1] >= temp_list[idx+1][1]:
                        return self.__weight[0]
                else:
                    if temp_list[idx][1] != temp_list[idx+1][1]:
                        return self.__weight[0]
        return 0

    def __check_highcode(self, notes, finger_list):
        if notes is not None and finger_list is not None:
            is_notes_highcode = False
            finger_count = [0, 0, 0, 0]
            for finger in finger_list:
                finger_count[finger] += 1
            for idx in range(4):
                if finger_count[idx] > 1:
                    if idx == 0:
                        is_notes_highcode = True
                    else:
                        return self.__weight[0]

            if is_notes_highcode:
                string_list = []
                fret = -1
                for idx, note_ in enumerate(notes.get()):
                    if fret == -1:
                        if finger_list[idx] == 0:
                            fret = note_.get("fret")
                            string_list.append(note_.get("string"))
                    else:
                        if finger_list[idx] == 0:
                            if fret != note_.get("fret"):
                                return self.__weight[0]
                            if note_.get("string") not in string_list:
                                string_list.append(note_.get("string"))

                string_list.sort()
                for idx in range(len(string_list) - 1):
                    if string_list[idx] != string_list[idx + 1] - 1:
                        return self.__weight[0]

        return 0
