import networkx as nx
import matplotlib.pyplot as plt

'''
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
(наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
Візуалізуйте створений граф, проведіть аналіз основних характеристик 
(наприклад, кількість вершин та ребер, ступінь вершин).
'''

def create_graph():
	G = nx.Graph()
	G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
	G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'F'),
					('D', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'G'), ('F', 'G'), ('F', 'H'), ('G', 'H'),
					('G', 'I'), ('H', 'I'), ('H', 'J'), ('I', 'J')])
	return G

def draw_graph(G):
	nx.draw(G, with_labels=True)
	plt.show()

if __name__ == '__main__':
	G = create_graph()
	# Візуалізація графа
	draw_graph(G)

	# Аналіз основних характеристик
	print('Кількість вершин:', G.number_of_nodes())
	print('Кількість ребер:', G.number_of_edges())
	print('Ступінь вершин:', G.degree())
