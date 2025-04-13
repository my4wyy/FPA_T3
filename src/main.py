def hamiltonian_path(graph, path, visited):
    if len(path) == len(graph):
        return path

    for neighbor in graph[path[-1]]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)

            result = hamiltonian_path(graph, path, visited)
            if result:
                return result

            path.pop()
            visited[neighbor] = False

    return None

if __name__ == "__main__":
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    start = 0
    visited = [False] * len(graph)
    visited[start] = True
    path = [start]

    result = hamiltonian_path(graph, path, visited)

    if result:
        print(f"caminho hamiltoniano encontrado: {result}")
    else:
        print("nenhum caminho hamiltoniano encontrado")
