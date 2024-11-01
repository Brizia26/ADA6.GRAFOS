import networkx as nx
from itertools import permutations
import matplotlib.pyplot as plt

graph = nx.Graph()
estados = ['Aguascalientes', 'Jalisco', 'Zacatecas', 'Guanajuato', 'Querétaro', 'San Luis Potosí', 'Michoacán']

edges = [
    ('Aguascalientes', 'Jalisco', 80),
    ('Aguascalientes', 'Zacatecas', 100),
    ('Aguascalientes', 'San Luis Potosí', 90),
    ('Jalisco', 'Guanajuato', 120),
    ('Jalisco', 'Michoacán', 150),
    ('Zacatecas', 'San Luis Potosí', 110),
    ('Guanajuato', 'Querétaro', 130),
    ('Querétaro', 'San Luis Potosí', 85),
    ('Michoacán', 'Querétaro', 140),
    ('Aguascalientes', 'Guanajuato', 160),
    ('Zacatecas', 'Jalisco', 180),
    ('San Luis Potosí', 'Michoacán', 200),
    ('Zacatecas', 'Querétaro', 190),
    ('Querétaro', 'Aguascalientes', 175),
    ('Michoacán', 'San Luis Potosí', 180)
]
for edge in edges:
    graph.add_edge(edge[0], edge[1], weight=edge[2])

def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        if graph.has_edge(path[i], path[i + 1]):
            cost += graph[path[i]][path[i + 1]]['weight']
        else:
            return float('inf')
    return cost

min_cost_a = float('inf')
best_path_a = None
for perm in permutations(estados):
    cost = calculate_cost(perm)
    if cost < min_cost_a:
        min_cost_a = cost
        best_path_a = perm

min_cost_b = float('inf')
best_path_b = None
for perm in permutations(estados):
    path_with_repeat = perm + (perm[0],)  
    cost = calculate_cost(path_with_repeat)
    if cost < min_cost_b:
        min_cost_b = cost
        best_path_b = path_with_repeat


print("a) Recorrido sin repetir estados:")
print("Camino:", best_path_a)
print("Costo total:", min_cost_a)

print("\nb) Recorrido repitiendo al menos un estado:")
print("Camino:", best_path_b)
print("Costo total:", min_cost_b)


pos = nx.spring_layout(graph)
plt.figure(figsize=(10, 8))
nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.title("Grafo de los Estados de México y sus conexiones completadas")
plt.show()
