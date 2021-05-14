from Notes import notes


class fingering:
    def __init__(self):
        self.__fingering = []

    def AppendCode(self, code):
        n = notes.notes()
        n.SetNotes(code)
        self.__fingering.append(n)

    def DeleteCode(self, index):
        if index < len(self.__fingering):
            del self.__fingering[index]
        else:
            print("OutOfRangeError")

    def GetCode(self):
        result = []
        for i in self.__fingering:
            result.append(i.GetNotes())
        return result

    def SetFingering(self, n):
        """
        SetFingering의 기능 : self.__fingering에 저장되어 있는 코드들의 운지법 중
        입력으로 받은 것과 가장 유사한 코드를 찾아 fingering을 설정하는 것
        """
        idx = self.__FindSimilarCode(n)
        """
        Set fingering
        """

    def __FindSimilarCode(self, n):
        count = 0
        max_count = 0
        most_similar_index = 0
        for i in self.GetCode():
            count = 0
            for j in i:
                for k in n:
                    if j[0] == k[0] and j[1] == k[1]:
                        count = count + 1
                        break
            if count > max_count:
                max_count = count
                most_similar_index = self.GetCode().index(i)
        return most_similar_index
