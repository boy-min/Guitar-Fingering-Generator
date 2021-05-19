from generator import generator as g
from printer import printer
import guitarpro

Song = input()

ProTab = guitarpro.parse("Resources\\"+Song)



g_generator = g.Generator(ProTab)

#print("Before")
#printer.show(g_generator.get())
g_generator.generate()
print("After")

notes = g_generator.get()
for id, measure in enumerate(notes.get()):
    for idx, beat in enumerate(measure):
        for index, note in enumerate(beat.get()):
            fin = note.get()["finger"]
            if fin == 0:
                finger = guitarpro.Fingering.open
            elif fin == 1:
                finger = guitarpro.Fingering.index
            elif fin == 2:
                finger = guitarpro.Fingering.middle
            elif fin == 3:
                finger = guitarpro.Fingering.annular
            elif fin == 4:
                finger = guitarpro.Fingering.little
            ProTab.tracks[0].measures[id].voices[0].beats[idx].notes[index].effect.leftHandFinger = finger
guitarpro.write(ProTab, "Finger_"+Song)

#printer.show(g_generator.get())
#printer.show(g_generator.get(), 0)
#printer.show(g_generator.get(), 1)
