n = int(input(f'Введите количество жителей:'))
graph =[]
while True:
    line = input(f'Введите связь построчно. Для завершения ввода введите пустую строку:')
    if line == "":
        break
    dob = list(map(int, line.split()))
    graph.append(dob)
#print(graph)
graph1={}
for i in range(n):
    graph1[i]=[]
for edge in graph:
    graph1[edge[0]-1].append(edge[1]-1)
#print(graph1)
def is_bipartite_dfs(graph, node, colors=None, color=0):
    if colors is None:
        colors = {}  # Словарь для хранения цветов вершин
    
    if node in colors:
        return colors[node] == color  # Проверяем, что вершина уже окрашена правильно
    
    colors[node] = color  # Красим текущую вершину в текущий цвет
    
    for neighbor in graph[node]:
        # Рекурсивно проверяем соседей, окрашивая их в противоположный цвет
        if not is_bipartite_dfs(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def check_bipartite(graph):
    colors = {}  # Словарь для хранения информации о цветах вершин
    for node in graph:
        if node not in colors:  # Проверяем каждую компоненту связности
            if not is_bipartite_dfs(graph, node, colors):
                return False  # Если хоть одна компонента не двудольная, возвращаем False
    return True


print("true" if check_bipartite(graph1) else "false")