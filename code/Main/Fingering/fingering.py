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

    def SetFingering(self, n):
        """
        SetFingering의 기능 : self.__fingering에 저장되어 있는 코드들의 운지법 중
        입력으로 받은 것과 가장 유사한 코드를 찾아 fingering을 설정하는 것
        """
