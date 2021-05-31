from generator import generator as g
import guitarpro


print("Music title : ", end='')
Song = input()

ProTab = guitarpro.parse("Resources\\"+Song)

size = 0
length = 0

while 1:
    print("Your hand size (0 : normal, 1 : small, 2 : big) : ", end='')
    size_ = input()
    size_ = int(size_)
    if size_ != 0 and size_ != 1 and size_ != 2:
        print("Unexpected input. Try again.")
        continue
    print("Your finger length (0 : normal, 1 : short, 2 : long) : ", end='')
    length_ = input()
    length_ = int(length_)
    if length_ != 0 and length_ != 1 and length_ != 2:
        print("Unexpected input. Try again.")
        continue
    size = size_
    length = length_
    break

print("Generating...",end='')

g_generator = g.Generator(ProTab, size, length)

g_generator.generate()

notes = g_generator.get()
for id_, measure in enumerate(notes.get()):
    for idx, beat in enumerate(measure):
        for index, note in enumerate(beat.get()):
            fin = note.get()["finger"]
            finger = 0
            if fin == 1 :
                finger = guitarpro.Fingering.index
            elif fin == 2 :
                finger = guitarpro.Fingering.middle
            elif fin == 3 :
                finger = guitarpro.Fingering.annular
            elif fin == 4 :
                finger = guitarpro.Fingering.little
            else :
                finger = guitarpro.Fingering.open
            ProTab.tracks[0].measures[id_].voices[0].beats[idx].notes[index].effect.leftHandFinger = finger
guitarpro.write(ProTab, "Resources\\Finger_"+Song)

print("\n"+"Success to write file : Finger_"+Song)
print("Exit the program.")