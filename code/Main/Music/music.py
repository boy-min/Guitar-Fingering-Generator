from Notes import notes


class music:
    def __init__(self):
        self.__music = []

    def SetMusic(self, music_sheet):
        for i in music_sheet:
            n = notes.notes()
            n.SetNotes(i)
            self.__music.append(n)

    def GetMusic(self):
        result = []
        for i in self.__music:
            result.append(i.GetNotes())
        return result
