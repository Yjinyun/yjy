"""
现在给定整数 n(1<=n<=9)，请你输出所有的满足条件的棋子摆法。
每个解决方案占 n 行，每行输出一个长度为 n 的字符串，用来表示完整的棋盘状态。
其中 . 表示某一个位置的方格状态为空，Q 表示某一个位置的方格上摆着皇后。
每个方案输出完成后，输出一个空行。
"""


def dfs(u):
    if (u == n):
        for i in range(n):
            print("".join(q[i]))
        print("")
        return

    for i in range(n):
        if not col[i] and not dg[u + i] and not udg[n - i + u]:
            q[u][i] = 'Q'
            col[i] = dg[u + i] = udg[n - i + u] = True
            dfs(u + 1)
            col[i] = dg[u + i] = udg[n - i + u] = False;
            q[u][i] = '.';


if __name__ == "__main__":
    n = int(input())
    q = [['.'] * n for i in range(n)]
    col, dg, udg = [False] * n, [False] * 2 * n, [False] * 2 * n

    dfs(0)

"""
输入样例：
4
输出样例：
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..

"""