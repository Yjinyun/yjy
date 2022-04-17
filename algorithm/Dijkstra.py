"""
朴素班Djkstra算法适合稠密图；
请你求出 1 号点到 n 号点的最短距离，如果无法从 1 号点走到 n 号点，则输出 −1。
第一行包含整数 n 和 m。
接下来 m 行每行包含三个整数 x,y,z，表示存在一条从点 x 到点 y 的有向边，边长为 z
"""


def dikjstra():
    global graph, st, dist, n
    dist[1] = 0

    # 遍历每个节点
    for i in range(1, n + 1):
        t = -1
        for j in range(1, n + 1):
            if st[j] == False and (t == -1 or dist[j] < dist[t]):
                t = j
        st[t] = True
        # 用找到的点更新其他所有点
        for j in range(1, n + 1):
            if dist[j] > dist[t] + graph[t][j]:
                dist[j] = dist[t] + graph[t][j]

    if dist[n] == float('inf'):
        return -1
    else:
        return dist[n]


def main():
    global graph, st, dist, n
    n, m = map(int, input().split())
    # 二维数组存图
    graph = [[float('inf') for j in range(n + 1)] for i in range(n + 1)]
    st = [False] * (n + 1)
    dist = [float('inf')] * (n + 1)
    for i in range(m):
        x, y, w = map(int, input().split())
        graph[x][y] = min(w, graph[x][y])
    # 处理结点自身
    for i in range(1, n + 1):
        graph[i][i] = 0

    print(dikjstra())


main()

"""
输入样例：
3 3
1 2 2
2 3 1
1 3 4
输出样例：
3
"""