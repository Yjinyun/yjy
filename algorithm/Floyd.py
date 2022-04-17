"""
多源最短路
给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环，边权可能为负数。
再给定 k 个询问，每个询问包含两个整数 x 和 y，表示查询从点 x 到点 y 的最短距离，如果路径不存在，则输出 impossible。
"""

def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


n, m, k = map(int, input().split())
graph = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    x, y, w = map(int, input().split())
    graph[x][y] = min(graph[x][y], w)

for i in range(1, n + 1):
    graph[i][i] = 0

floyd()

for i in range(k):
    x, y = map(int, input().split())
    if graph[x][y] == float('inf'):
        print('impossible')
    else:
        print(graph[x][y])

"""
输入样例：
3 3 2
1 2 1
2 3 2
1 3 1
2 1
1 3
输出样例：
impossible
1
"""