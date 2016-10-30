import heapq as h

def find_path(graph, pos, goal, h):
	"""
	A* search for optimal path from pos -> goal in m
	:graph: the graph
	:pos: the start
	:goal: the end
	:h: heuristic function
	:return: the optimal path or False
	"""

	fringe = []
	h.heappush(fringe, (0, (pos,)))
	costs = {pos: 0}

	while fringe:
		_, (curr, *prev) = h.heappop(fringe)

		# check for goal
		if curr == goal:
			return list(reversed([curr, *prev]))

		# add children to heap
		for child in graph[curr]:
			# calculate cost g(x)
			new_cost = costs[curr] + graph[curr][child]

			if child not in costs or new_cost < costs[child]:
				costs[child] = new_cost
				# calculate priority g(x) + h(x)
				priority = new_cost + h(child, goal)
				h.heappush(fringe, (priority, (child, curr, *prev)))

	# not possible
	return False
