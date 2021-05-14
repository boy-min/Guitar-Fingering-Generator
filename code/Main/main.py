from Generator import generator as g
from Printer import printer as p

g_generator = g.generator()
g_generator.SetMusicSheet([[[1, 1, 0], [2, 2, 0]], [[3, 3, 0]]])
p.PrintSheet(g_generator.GetMusicSheet(), 0)
p.PrintSheet(g_generator.GetMusicSheet(), 1)