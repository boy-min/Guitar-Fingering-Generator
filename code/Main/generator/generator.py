from generator.hand import hand
from music import music
import guitarpro


class Generator:
    def __init__(self, music_=None, size_=None, length_=None):
        self.__music = music.Music()
        self.__hand = hand.Hand(size_, length_)
        self.__weight = [100000, 7, 10, 28, 35, 70, 100, 5, 15, 12, 20]
        self.__ratio = [2, 3, 1, 2, 3, 1]

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
                        notes_.get().pop(i - count)
                        count += 1
                    music_.append(notes_)
        dp = [[[0, -1] for col in range(4097)] for row in range(len(music_))]
        for i in reversed(range(len(music_))):
            if i == len(music_) - 1:
                if len(music_[i].get()) == 0:
                    dp[i][4096][0] = 0
                else:
                    for finger1 in range(4 ** len(music_[i].get())):
                        finger_list_1 = []
                        for j in range(len(music_[i].get())):
                            finger_list_1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                        dp[i][finger1][0] = self.__difficulty(music_[i], finger_list_1, None, None, dp, i, music_)
            else:
                if len(music_[i].get()) == 0:
                    if len(music_[i + 1].get()) == 0:
                        dp[i][4096][0] = dp[i + 1][4096][0]
                        dp[i][4096][1] = 4096
                    else:
                        min_ = 2147483647
                        for finger2 in range(4 ** len(music_[i + 1].get())):
                            finger_list_2 = []
                            for j in range(len(music_[i + 1].get())):
                                finger_list_2.append((finger2 % (4 ** (j + 1))) // (4 ** j))
                            dif = dp[i + 1][finger2][0] + self.__difficulty(None, None, music_[i + 1],
                                                                            finger_list_2, dp, i, music_)
                            if min_ > dif:
                                min_ = dif
                                dp[i][4096][1] = finger2
                        dp[i][4096][0] = min_
                else:
                    if len(music_[i + 1].get()) == 0:
                        for finger1 in range(4 ** len(music_[i].get())):
                            finger_list_1 = []
                            for j in range(len(music_[i].get())):
                                finger_list_1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                            dp[i][finger1][0] = dp[i + 1][4096][0] + self.__difficulty(music_[i], finger_list_1,
                                                                                       None, None, dp, i, music_)
                            dp[i][finger1][1] = 4096
                    else:
                        for finger1 in range(4 ** len(music_[i].get())):
                            finger_list_1 = []
                            for j in range(len(music_[i].get())):
                                finger_list_1.append((finger1 % (4 ** (j + 1))) // (4 ** j))
                            min_ = 2147483647
                            for finger2 in range(4 ** len(music_[i + 1].get())):
                                finger_list_2 = []
                                for j in range(len(music_[i + 1].get())):
                                    finger_list_2.append((finger2 % (4 ** (j + 1))) // (4 ** j))
                                dif = dp[i + 1][finger2][0] + self.__difficulty(music_[i], finger_list_1, music_[i + 1],
                                                                                finger_list_2, dp, i, music_)
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
                    for finger in range(4 ** len(music_[i].get())):
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

    def __difficulty(self, notes_1, finger_list_1, notes_2, finger_list_2, dp, i, music_):
        difficulty = 0
        difficulty += self.__check_highcode(notes_1, finger_list_1)
        difficulty += self.__check_highcode(notes_2, finger_list_2)
        difficulty += self.__check_twist(notes_1, finger_list_1)
        difficulty += self.__check_twist(notes_2, finger_list_2)
        if difficulty >= self.__weight[0]:
            return difficulty

        list_1 = []
        list_2 = []

        if notes_1 is not None and notes_2 is None:
            for idx, note_ in enumerate(notes_1.get()):
                list_1.append([finger_list_1[idx], note_.get("fret"), note_.get("string")])
            list_1.sort()
            pos_of_hand_1 = self.__get_pos(notes_1, finger_list_1)
            difficulty += self.__get_dif(list_1, pos_of_hand_1)
            recent_use = self.__get_recent_use(dp, i, finger_list_1, None, music_)
            for idx, note_ in enumerate(notes_1.get()):
                if recent_use[finger_list_1[idx]][0] != 0:
                    if note_.get("fret") != recent_use[finger_list_1[idx]][0] \
                            and note_.get("string") != recent_use[finger_list_1[idx]][1]:
                        difficulty += self.__weight[10]
        elif notes_1 is None and notes_2 is not None:
            for idx, note_ in enumerate(notes_2.get()):
                list_2.append([finger_list_2[idx], note_.get("fret"), note_.get("string")])
            list_2.sort()
            pos_of_hand_2 = self.__get_pos(notes_2, finger_list_2)
            difficulty += self.__get_dif(list_2, pos_of_hand_2)
            recent_use = self.__get_recent_use(dp, i, None, finger_list_2, music_)
            for idx, note_ in enumerate(notes_2.get()):
                if recent_use[finger_list_2[idx]][0] != 0:
                    if note_.get("fret") != recent_use[finger_list_2[idx]][0] \
                            and note_.get("string") != recent_use[finger_list_2[idx]][1]:
                        difficulty += self.__weight[10]
        elif notes_1 is not None and notes_2 is not None:
            for idx, note_ in enumerate(notes_1.get()):
                list_1.append([finger_list_1[idx], note_.get("fret"), note_.get("string")])
            list_1.sort()
            for idx, note_ in enumerate(notes_2.get()):
                list_2.append([finger_list_2[idx], note_.get("fret"), note_.get("string")])
            list_2.sort()
            pos_of_hand_1 = self.__get_pos(notes_1, finger_list_1)
            pos_of_hand_2 = self.__get_pos(notes_2, finger_list_2)
            difficulty += self.__get_dif(list_1, pos_of_hand_1)
            difficulty += self.__get_dif(list_2, pos_of_hand_2)
            difficulty += self.__get_change_dif(list_1, list_2)
            recent_use = self.__get_recent_use(dp, i, finger_list_1, finger_list_2, music_)
            for idx, note_ in enumerate(notes_1.get()):
                if recent_use[finger_list_1[idx]][0] != 0:
                    if note_.get("fret") != recent_use[finger_list_1[idx]][0] \
                            and note_.get("string") != recent_use[finger_list_1[idx]][1]:
                        difficulty += self.__weight[10]
            for idx, note_ in enumerate(notes_2.get()):
                if recent_use[finger_list_2[idx]][0] != 0:
                    if note_.get("fret") != recent_use[finger_list_2[idx]][0] \
                            and note_.get("string") != recent_use[finger_list_2[idx]][1]:
                        difficulty += self.__weight[10]
            difficulty += abs(pos_of_hand_1 - pos_of_hand_2) * self.__weight[6] * self.__ratio[self.__hand.get("size")]

        return difficulty

    def __get_recent_use(self, dp, i, finger_list_1, finger_list_2, music_):
        if i == len(dp) - 1:
            return [[0, 0], [0, 0], [0, 0], [0, 0]]
        else:
            if finger_list_1 is not None and finger_list_2 is None:
                result = [[0, 0], [0, 0], [0, 0], [0, 0]]
                idx = 0
                count = 10
                for j in range(len(finger_list_1)):
                    idx += finger_list_1[len(finger_list_1) - 1 - j] * (4 ** j)
                for j in range(i + 1, len(dp), 1):
                    idx = dp[j][idx][1]
                    count -= 1
                    if count < 0:
                        break
                    if idx != 4096:
                        finger_list = []
                        for k in range(len(music_[j].get())):
                            finger_list.append((idx % (4 ** (k + 1))) // (4 ** k))
                        for k in range(len(finger_list)):
                            if result[finger_list[k]][0] == 0 and result[finger_list[k]][1] == 0:
                                result[finger_list[k]][0] = music_[j].get()[k].get("fret")
                                result[finger_list[k]][1] = music_[j].get()[k].get("string")
                    else:
                        continue
                    if result[0][0] != 0 and result[1][0] != 0 and result[2][0] != 0 and result[3][0] != 0:
                        break
                return result
            elif finger_list_1 is None and finger_list_2 is not None:
                result = [[0, 0], [0, 0], [0, 0], [0, 0]]
                idx = 0
                count = 10
                for j in range(len(finger_list_2)):
                    idx += finger_list_2[len(finger_list_2) - 1 - j] * (4 ** j)
                for j in range(i + 1, len(dp), 1):
                    idx = dp[j][idx][1]
                    count -= 1
                    if count < 0:
                        break
                    if idx != 4096:
                        finger_list = []
                        for k in range(len(music_[j].get())):
                            finger_list.append((idx % (4 ** (k + 1))) // (4 ** k))
                        for k in range(len(finger_list)):
                            if result[finger_list[k]][0] == 0 and result[finger_list[k]][1] == 0:
                                result[finger_list[k]][0] = music_[j].get()[k].get("fret")
                                result[finger_list[k]][1] = music_[j].get()[k].get("string")
                    else:
                        continue
                    if result[0][0] != 0 and result[1][0] != 0 and result[2][0] != 0 and result[3][0] != 0:
                        break
                return result
            elif finger_list_1 is not None and finger_list_2 is not None:
                result = [[0, 0], [0, 0], [0, 0], [0, 0]]
                idx = 0
                count = 10
                for j in range(len(finger_list_2)):
                    idx += finger_list_2[len(finger_list_2) - 1 - j] * (4 ** j)
                for j in range(i + 2, len(dp), 1):
                    idx = dp[j][idx][1]
                    count -= 1
                    if count < 0:
                        break
                    if idx != 4096:
                        finger_list = []
                        for k in range(len(music_[j].get())):
                            finger_list.append((idx % (4 ** (k + 1))) // (4 ** k))
                        for k in range(len(finger_list)):
                            if result[finger_list[k]][0] == 0 and result[finger_list[k]][1] == 0:
                                result[finger_list[k]][0] = music_[j].get()[k].get("fret")
                                result[finger_list[k]][1] = music_[j].get()[k].get("string")
                    else:
                        continue
                    if result[0][0] != 0 and result[1][0] != 0 and result[2][0] != 0 and result[3][0] != 0:
                        break
                return result

    def __get_pos(self, notes, finger_list):
        if 0 in finger_list:
            return notes.get()[finger_list.index(0)].get("fret")
        elif 1 in finger_list:
            return notes.get()[finger_list.index(1)].get("fret") - 1
        elif 2 in finger_list:
            return notes.get()[finger_list.index(2)].get("fret") - 2
        elif 3 in finger_list:
            return notes.get()[finger_list.index(3)].get("fret") - 3
        else:
            return None

    def __get_change_dif(self, sorted_list_1, sorted_list_2):
        difficulty = 0
        gradient_list_1 = [-1, 1, 1]
        gradient_list_2 = [-1, 1, 1]
        for idx in range(len(sorted_list_1) - 1):
            for i in range(sorted_list_1[idx][0], sorted_list_1[idx + 1][0], 1):
                if sorted_list_1[idx + 1][1] != sorted_list_1[idx][1]:
                    gradient_list_1[i] = (sorted_list_1[idx][2] - sorted_list_1[idx + 1][2]) \
                                         / (sorted_list_1[idx + 1][1] - sorted_list_1[idx][1])
        for idx in range(len(sorted_list_2) - 1):
            for i in range(sorted_list_2[idx][0], sorted_list_2[idx + 1][0], 1):
                if sorted_list_2[idx + 1][1] != sorted_list_2[idx][1]:
                    gradient_list_2[i] = (sorted_list_2[idx][2] - sorted_list_2[idx + 1][2]) \
                                         / (sorted_list_2[idx + 1][1] - sorted_list_2[idx][1])
        difficulty += int(abs(gradient_list_1[0] - gradient_list_2[0]) * self.__weight[7])
        difficulty += int(abs(gradient_list_1[1] - gradient_list_2[1]) * self.__weight[8])
        difficulty += int(abs(gradient_list_1[2] - gradient_list_2[2]) * self.__weight[9])
        return difficulty

    def __get_dif(self, sorted_list, pos):
        difficulty = 0
        gradient_list = [-1, 1, 1]
        for idx in range(len(sorted_list) - 1):
            if sorted_list[idx][0] == sorted_list[idx + 1][0]:
                if sorted_list[idx][0] == 0:
                    continue
            else:
                d = (sorted_list[idx][1] - sorted_list[idx + 1][1]) ** 2 \
                    + (sorted_list[idx][2] - sorted_list[idx + 1][2]) ** 2
                difficulty += (d // (sorted_list[idx][0] - sorted_list[idx + 1][0])) \
                              * self.__ratio[self.__hand.get("length") + 3]
                for i in range(sorted_list[idx][0], sorted_list[idx + 1][0], 1):
                    if sorted_list[idx + 1][1] != sorted_list[idx][1]:
                        gradient_list[i] = (sorted_list[idx][2] - sorted_list[idx + 1][2]) \
                                           / (sorted_list[idx + 1][1] - sorted_list[idx][1])
        difficulty += int(abs(gradient_list[0] + 1) * self.__weight[7])
        difficulty += int(abs(gradient_list[1] - 1) * self.__weight[8])
        difficulty += int(abs(gradient_list[2] - 1) * self.__weight[9])
        finger_fret = [pos, pos + 1, pos + 2, pos + 3]
        for idx in range(len(sorted_list)):
            if abs(sorted_list[idx][1] - finger_fret[sorted_list[idx][0]]) > 1:
                d = self.__weight[5] * abs(sorted_list[idx][1] - finger_fret[sorted_list[idx][0]]) \
                    * (sorted_list[idx][0] + 1)
                difficulty += d * self.__ratio[self.__hand.get("length") + 3]
            difficulty += self.__weight[sorted_list[idx][0] + 1] * self.__ratio[self.__hand.get("length") + 3]
        return difficulty

    def __check_twist(self, notes, finger_list):
        if notes is not None and finger_list is not None:
            temp_list = []
            for idx, note_ in enumerate(notes.get()):
                temp_list.append([note_.get("fret"), finger_list[idx]])
            temp_list.sort()
            for idx in range(len(temp_list) - 1):
                if temp_list[idx][0] < temp_list[idx + 1][0]:
                    if temp_list[idx][1] > temp_list[idx + 1][1]:
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
                if string_list[0] != 1:
                    return self.__weight[0]
                for idx in range(len(string_list) - 1):
                    if string_list[idx] != string_list[idx + 1] - 1:
                        return self.__weight[0]

        return 0
