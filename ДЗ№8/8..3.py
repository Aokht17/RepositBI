import matplotlib.pyplot as plt

import networkx as nx

G = nx.cubical_graph()
nx.draw(G)
nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')
plt.savefig('G')