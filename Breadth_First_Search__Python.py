from collections import deque

def bfs(graph, start):
    # Initialize the queue with the start node
    queue = deque([start])
    # Initialize the set of visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the front of the queue
        current_node = queue.popleft()
        print(current_node, end=' ')
        
        # Iterate over all adjacent nodes
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Enqueue non-visited adjacent nodes
                queue.append(neighbor)
                # Mark the node as visited
                visited.add(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

