from util import Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    current_node = starting_node
    relationships = {}

    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]

        if child not in relationships:
            relationships[child] = set()
        relationships[child].add(parent)

    if starting_node in relationships:
        queue.enqueue(relationships[current_node])
    else:
        return -1

    while True:
        relations = queue.dequeue()
        current_node = min(relations)
        if current_node not in relationships:
            return current_node
        else:
            queue.enqueue(relationships[current_node])