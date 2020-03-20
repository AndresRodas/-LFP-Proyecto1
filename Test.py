from graphviz import *

dot = Digraph()


dot.node('A', 'S0')
dot.node('B', 'S1')
dot.node('C', 'S2')
dot.node('D', 'S3')
dot.node('E', 'S4')
dot.edge('B', 'E', label=';')
dot.edge('B', 'B', label='D')
dot.edge('B', 'B', label='L')
print(dot.source)
dot.render('Grafo')