def PrintSheet(music_sheet, index):
    """
    PrintSheet의 기능 : 입력으로 받은 music_sheet에서 index에 해당하는 notes의 정보를 출력하는 것
    """
    print(index, "번째 notes")
    for i in music_sheet[index]:
        print(i)
