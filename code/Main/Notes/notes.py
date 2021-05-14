from Notes.Note import note


class notes:
    def __init__(self):
        self.__list = []

    def SetNotes(self, note_list):
        for i in note_list:
            if len(i) != 3:
                print("ParameterError")
                break
            else:
                n = note.note(i[0], i[1], i[2])
                self.__list.append(n)

    def GetNotes(self):
        result = []
        for i in self.__list:
            result.append(i.GetNote())
        return result
