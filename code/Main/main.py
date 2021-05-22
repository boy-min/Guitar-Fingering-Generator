from generator import generator as g
import guitarpro

print("Music title : ", end='')
Song = input()

ProTab = guitarpro.parse("Resources\\"+Song)

g_generator = g.Generator(ProTab)

g_generator.generate()

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
guitarpro.write(ProTab, "Resources\\Finger_"+Song)
