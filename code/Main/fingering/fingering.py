import sys
from notes import notes

class Fingering :
    def __init__(self) :
        self.__fingering = []
        
        codes = [
            [[2, 1, 1], [4, 2, 2], [5, 3, 3]],                                  # C
            [[1, 3, 1], [5, 3, 1], [6, 3, 1], [2, 4, 2], [3, 5, 4], [4, 5, 3]], # Cm
            [[2, 1, 1], [4, 2, 2], [3, 3, 4], [5, 3, 3]],                       # C7
            [[4, 2, 2], [5, 3, 3]],                                             # CM7
            [[1, 3, 1], [3, 3, 1], [5, 3, 1], [6, 3, 1], [2, 4, 2], [4, 5, 3]], # Cm7
            [[1, 2, 2], [3, 2, 1], [2, 3, 3]],                                  # D
            [[1, 1, 1], [3, 2, 2], [2, 3, 3]],                                  # Dm
            [[2, 1, 1], [1, 2, 3], [3, 2, 2]],                                  # D7
            [[1, 2, 1], [2, 2, 1], [3, 2, 1]],                                  # DM7
            [[1, 1, 1], [2, 1, 1], [3, 2, 2]],                                  # Dm7
            [[3, 1, 1], [4, 2, 3], [5, 2, 2]],                                  # E
            [[4, 2, 3], [5, 2, 2]],                                             # Em
            [[3, 1, 1], [5, 2, 2]],                                             # E7
            [[3, 1, 2], [4, 1, 1], [5, 2, 3]],                                  # EM7
            [[5, 2, 2]],                                                        # Em7
            [[1, 1, 1], [2, 1, 1], [6, 1, 1], [3, 2, 2], [4, 3, 4], [5, 3, 3]], # F
            [[1, 1, 1], [2, 1, 1], [3, 1, 1], [6, 1, 1], [4, 3, 4], [5, 3, 3]], # Fm
            [[1, 1, 1], [2, 1, 1], [4, 1, 1], [6, 1, 1], [3, 2, 2], [5, 3, 3]], # F7
            [[2, 1, 1], [3, 2, 2], [4, 3, 3]],                                  # FM7
            [[1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 1, 1], [6, 1, 1], [5, 3, 3]], # Fm7
            [[5, 2, 2], [1, 3, 4], [6, 3, 3]],                                  # G
            [[1, 1, 1], [2, 1, 1], [3, 1, 1], [6, 1, 1], [4, 5, 4], [5, 5, 3]], # Gm
            [[1, 1, 1], [5, 2, 2], [6, 3, 3]],                                  # G7
            [[1, 2, 1], [5, 2, 2], [6, 3, 3]],                                  # GM7
            [[1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 1, 1], [6, 1, 1], [5, 5, 3]], # Gm7
            [[2, 2, 3], [3, 2, 2], [4, 2, 1]],                                  # A
            [[2, 1, 1], [3, 2, 3], [4, 2, 2]],                                  # Am
            [[2, 2, 2], [4, 2, 1]],                                             # A7
            [[3, 1, 1], [2, 2, 3], [4, 2, 2]],                                  # AM7
            [[2, 1, 1], [4, 2, 2]],                                             # Am7
            [[1, 2, 1], [5, 2, 1], [6, 2, 1], [2, 4, 4], [3, 4, 3], [4, 4, 2]], # B
            [[1, 2, 1], [5, 2, 1], [6, 2, 1], [2, 3, 2], [3, 4, 4], [4, 4, 3]], # Bm
            [[4, 1, 1], [1, 2, 4], [3, 2, 3], [5, 2, 2]],                       # B7
            [[1, 2, 1], [5, 2, 1], [6, 2, 1], [3, 3, 2], [2, 4, 4], [4, 4, 3]], # BM7
            [[1, 2, 1], [3, 2, 1], [5, 2, 1], [6, 2, 1], [2, 3, 2], [4, 4, 3]]  # Bm7
        ]

        for code in codes : 
            self.append(code)

    def append(self, code) :
        self.__fingering.append(notes.Notes(code))

    def delete(self, index) :
        if index < len(self.__fingering) :
            del self.__fingering[index]

        else:
            sys.exit("OutOfRangeError")

    def get(self) :
        return self.__fingering

    def set(self, n) : 
        """
        set의 기능 : self.__fingering에 저장되어 있는 코드들의 운지법 중
        입력으로 받은 것과 가장 유사한 코드를 찾아 fingering을 설정하는 것
        """
        idx = self.__find_similar_code(n)
        """
        Set fingering
        """

    def __find_similar_code(self, n) :
        max_count = 0
        most_similar_index = 0
        
        for index, notes_ in enumerate(self.__fingering) : 
            count = 0

            for note1 in notes_.get() :
                for note2 in n.get() :
                    if note1 == note2 : 
                        count = count + 1
                        break

            if count > max_count :
                max_count = count
                most_similar_index = index
                
        return most_similar_index
