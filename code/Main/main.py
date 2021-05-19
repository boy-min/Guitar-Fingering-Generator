from generator import generator as g
from printer import printer
import guitarpro

Song = input()

ProTab = guitarpro.parse("Resources\\Falling slowly.gp5")



g_generator = g.Generator(ProTab)

#print("Before")
#printer.show(g_generator.get())
g_generator.generate()
print("After")
printer.show(g_generator.get())
#printer.show(g_generator.get(), 0)
#printer.show(g_generator.get(), 1)
