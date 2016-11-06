import disjoint_sets as ds
import heapq as h

def kruskal(graph):
	# graph = {edge: {edge: weight}}

	forest = ds.DisjointSets()
	mst = {}

	def add_edge(a, b, w):
		forest.connect(a, b)
		if a not in mst:
			mst[a] = {}
		if b not in mst:
			mst[b] = {}
		mst[a][b] = w
		mst[b][a] = w

	edge_queue = []
	for a, edges in graph.items():
		for b, weight in edges.items():
			h.heappush(edge_queue, (weight, (a, b)))

	while len(edge_queue) > 0:
		w, (a, b) = h.heappop(edge_queue)

		has_a = a in forest
		has_b = b in forest

		if has_a and has_b:
			if not forest.connected(a, b):
				add_edge(a, b, w)
		else:
			if not has_a:
				forest.add(a)
			if not has_b:
				forest.add(b)
			add_edge(a, b, w)

	return mst


