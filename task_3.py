from task_1 import create_graph, draw_graph

'''
У граф додано ваги ребер, програмно реалізовано алгоритм Дейкстри 
для знаходження найкоротшого шляху в розробленому графі.
'''

def dijkstra(graph, start):
	visited = {start: 0}
	path = {}
	nodes = set(graph.nodes)
	while nodes:
		min_node = None
		for node in nodes:
			if node in visited:
				if min_node is None:
					min_node = node
				elif visited[node] < visited[min_node]:
					min_node = node
		if min_node is None:
			break
		nodes.remove(min_node)
		current_weight = visited[min_node]
		for edge in graph[min_node]:
			weight = current_weight + graph[min_node][edge]['weight']
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = min_node
	return visited, path

if __name__ == '__main__':
	G = create_graph()

	# Додавання ваг ребер
	G.add_weighted_edges_from([('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3), ('B', 'D', 4), ('B', 'E', 5), ('C', 'D', 6),
								('C', 'F', 7), ('D', 'E', 8), ('D', 'F', 9), ('D', 'G', 10), ('E', 'G', 11), ('F', 'G', 12),
								('F', 'H', 13), ('G', 'H', 14), ('G', 'I', 15), ('H', 'I', 16), ('H', 'J', 17), ('I', 'J', 18)])
	
	# Візуалізація графа
	draw_graph(G)

	visited, path = dijkstra(G, 'A')
	print('Відстані:', visited)