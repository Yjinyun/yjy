"""
给定一个整数 n，将数字 1∼n 排成一排，将会有很多种排列方法。
现在，请你按照字典序将所有的排列方法输出。
"""


def dfs(u):
    # 返回条件
    global path, n, st
    if (u == n):
        for i in range(n):
            print(path[i], end=' ')
        print("")

    for i in range(1, n + 1):
        if (st[i] != True):
            path[u] = i
            st[i] = True
            dfs(u + 1)
            st[i] = False


if __name__ == "__main__":
    n = int(input())
    path = [0] * 10
    st = [False] * 10
    dfs(0)

"""
输入样例：
3
输出样例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""