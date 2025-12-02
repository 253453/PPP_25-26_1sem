def find_shortest_path(graph, start, end, path=None, dist=0, best=None, logs=None):
    if path is None:
        path = [start]
    if logs is None:
        logs = []
    logs.append(f'Текущий путь: {path}, текущее расстояние: {dist}')
    
    if start == end:
        if best is None or dist < best[0]:
            best = (dist, path[:])
            logs.append(f'Новый кратчайший путь: {path} с длиной {dist}')
        return best, logs
    
    for neighbor, weight in enumerate(graph[start]):
        if weight != 0 and neighbor not in path:
            candidate, logs = find_shortest_path(graph, neighbor, end, path + [neighbor], dist + weight, best, logs)
            if candidate and (best is None or candidate[0] < best[0]):
                best = candidate
                logs.append(f'Лучший путь: {best[1]} с длиной {best[0]}')
    
    return best, logs


graph = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]

start, end = 0, 4
result, logs = find_shortest_path(graph, start, end)
print('Кратчайший путь', result[1], 'с длиной', result[0])
print('\nЗапись шагов поиска:')
for log in logs:
    print(log)


