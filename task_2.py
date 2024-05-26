import networkx as nx
from task_1 import create_graph

'''
Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі,
який було розроблено у першому завданні.
Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах.
Поясніть, чому шляхи для алгоритмів саме такі.
'''

def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	print(start, end=' ')
	for next in set(graph[start]) - visited:
		dfs(graph, next, visited)
	return visited

def bfs(graph, start):
	visited = []
	queue = [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			queue.extend(set(graph[vertex]) - set(visited))
	return visited

if __name__ == '__main__':
	G = create_graph()
	graph = nx.to_dict_of_lists(G)
	print('DFS:')
	dfs(graph, 'A')
	print('\nBFS:')
	print(bfs(graph, 'A'))


	'''
	DFS: A B D E G I J H F C H F H G F C E D C
	BFS: ['A', 'B', 'D', 'C', 'E', 'G', 'F', 'I', 'H', 'J']
	Виведення відрізняється оскільки нашому графі є цикли, і ми використовуємо вираз set(graph[vertex]) - set(visited) для визначення 
	множини невідвіданих сусідніх вершин. Порядок елементів у вбудованих множинах у Python не гарантований, і це може вплинути 
	на порядок, у якому вершини додаються до черги.
	'''