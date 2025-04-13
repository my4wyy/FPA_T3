import networkx as nx
import matplotlib.pyplot as plt

from main import hamiltonian_path

graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}

G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

start = 0
visited = [False] * len(graph)
visited[start] = True
path = hamiltonian_path(graph, [start], visited)

if path:
    path_edges = list(zip(path, path[1:]))
else:
    path_edges = []

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.savefig("assets/grafo.png")
plt.show()
