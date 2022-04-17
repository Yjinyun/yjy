"""
堆优化版dijkstra适合稀疏图
"""

import collections, heapq


def dijkstraHeap():
    global g, h, n, dist, st
    while len(h) != 0:
        d, k = heapq.heappop(h)
        if st[k]:
            continue
        st[k] = True  # ~~~~~~~~~~~~~~~~~~~~~~
        for w, j in g[k]:
            if dist[j] > dist[k] + w:
                dist[j] = dist[k] + w
                heapq.heappush(h, [dist[j], j])


def main():
    global g, h, n, dist, st
    n, m = map(int, input().split())
    h = []
    g = collections.defaultdict(list)
    st = [False] * (n + 1)
    dist = [float('inf')] * (n + 1)

    dist[1] = 0
    heapq.heappush(h, [0, 1])

    for i in range(m):
        x, y, w = map(int, input().split())
        g[x].append([w, y])

    dijkstraHeap()

    print(dist[n] if dist[n] != float('inf') else -1)


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