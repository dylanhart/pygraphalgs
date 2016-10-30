class Traversal(Enum):
    bfs = 0
    dfs = 1

def do_traversal(graph, start, end, traversal):

    # set of seen nodes
    seen = set()
    # queue is a queue of path tuples
    queue = deque([(start,)])

    # while there are items to check
    while len(queue) > 0:
        # grab current vert and rest of path off of queue
        vert, *prev = queue.pop()

        # skip vert if seen
        if vert in seen:
            continue

        # check for end node
        if vert == end:
            # if found, flip the path and return it
            # flip is need to transform from end -> start to start -> end
            return tuple(reversed([vert, *prev]))

        # add the current vertex to seen nodes
        seen.add(vert)

        # find all children (as paths) that haven't been seen
        children = (
            # append child to current path
            (child, vert, *prev)
            for child in graph[vert]
            if child not in seen
        )

        # add children to queue based on traversal alg
        if traversal == Traversal.bfs:
            queue.extendleft(children)
        elif traversal == Traversal.dfs:
            queue.extend(children)

    # end was not found (path does not exist)
    return False

def dfs(graph, start, end):
    return do_traversal(graph, start, end, Traversal.dfs)


def bfs(graph, start, end):
    return do_traversal(graph, start, end, Traversal.bfs)
