from generator import generator as g
from printer import printer
import guitarpro

Song = input()

ProTab = guitarpro.parse("Resources\\twilight.gp5")

music = []

for tr in ProTab.tracks:
    for ms in tr.measures:
        for vc in ms.voices:
            for bt in vc.beats:
                beat = []
                for nt in bt.notes:
                    note = [nt.value, nt.string, 0]
                    beat.append(note)
                music.append(beat)


g_generator = g.Generator(music)

print("Before")
printer.show(g_generator.get())
"""
g_generator.generate()
print("After")
printer.show(g_generator.get(), 0)
printer.show(g_generator.get(), 1)
"""
