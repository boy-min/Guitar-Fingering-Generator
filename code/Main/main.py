from generator import generator as g
from printer import printer

g_generator = g.Generator([[[1, 1, 0], [2, 3, 0]], [[3, 3, 0]]])
print("Before")
printer.show(g_generator.get())
g_generator.generate()
print("After")
printer.show(g_generator.get(), 0)
printer.show(g_generator.get(), 1)

