"""
将所有边按权重从小到大排序

给定一个 n 个点 m 条边的无向图，图中可能存在重边和自环，边权可能为负数。
求最小生成树的树边权重之和，如果最小生成树不存在则输出 impossible。
"""


"""
判断是否会产生回路的方法为：使用并查集。
在初始状态下给各个个顶点在不同的集合中。、
遍历过程的每条边，判断这两个顶点的是否在一个集合中。
如果边上的这两个顶点在一个集合中，说明两个顶点已经连通，这条边不要。如果不在一个集合中，则要这条边。
"""
def find(x):    #并查集
    if p[x] != x: p[x] = find(p[x])
    return p[x]


n, m = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for i in range(m)], key=lambda x: x[-1])
# 初始化父节点
p = list(range(n + 1))
res, cnt = 0, 0

for x, y, w in edges:
    if find(x) != find(y):
        p[find(y)] = find(x)
        res += w
        cnt += 1
print(res) if cnt == n - 1 else print('impossible')


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