"""
走迷宫
给定一个 n×m 的二维整数数组，用来表示一个迷宫，数组中只包含 0 或 1，其中 0 表示可以走的路，1 表示不可通过的墙壁。
"""

def bfs():
    d[0][0] = 0
    queue = [(0, 0)] #把第一个表格放入队列
    while queue:
        x, y = queue.pop(0)
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if (0 <= a < n and 0 <= b < m and q[a][b] == 0 and d[a][b] == -1):
                queue.append((a, b))
                d[a][b] = d[x][y] + 1
    print (d[n - 1][m - 1])

if __name__ == "__main__":
    n, m = map(int, input().split())
    q = [[-1] * m for i in range(n)]
    d = [[-1] * m for i in range(n)]
    for i in range(n):
        q[i] = list(map(int, input().split()))
    bfs()



"""
输入样例：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出样例：
8
"""