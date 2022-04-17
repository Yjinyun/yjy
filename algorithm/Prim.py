"""
prim 算法采用的是一种贪心的策略。
每次将离连通部分的最近的点和点对应的边加入的连通部分，连通部分逐渐扩大，最后将整个图连通起来，并且边长之和最小。

给定一个 n 个点 m 条边的无向图，图中可能存在重边和自环，边权可能为负数。
求最小生成树的树边权重之和，如果最小生成树不存在则输出 impossible。
"""


def prim():
    dist[1] = 0
    res = 0

    for i in range(1, n + 1):
        t = 0
        for j in range(1, n + 1):
            if st[j] == False and (t == 0 or dist[t] > dist[j]):
                t = j

        if dist[t] == float('inf'):
            return float('inf')
        if i:
            res += dist[t]

        # 用找出的点更新其他点
        for j in range(1, n + 1):
            dist[j] = min(dist[j], graph[t][j])  # 不是dist[t] + graph[t][j]，距集合最近的点，不是距离原点

        st[t] = True

    return res


n, m = map(int, input().split())
graph = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
dist = [float('inf') for i in range(n + 1)]
st = [False] * (n + 1)

for i in range(m):
    x, y, w = map(int, input().split())
    graph[x][y] = graph[y][x] = min(graph[x][y], w)

# 处理结点自身
for i in range(1, n + 1):
    graph[i][i] = 0

res = prim()
print('impossible') if res >= float('inf') / 2 else print(res)


"""
输入样例：
4 5
1 2 1
1 3 2
1 4 3
2 3 2
3 4 4
输出样例：
6
"""