from generator import generator as g
from printer import printer

g_generator = g.generator([[[1, 1, 0], [2, 2, 0]], [[3, 3, 0]]])
g_generator.generate()
printer.show(g_generator.get(), 0)
printer.show(g_generator.get(), 1)
