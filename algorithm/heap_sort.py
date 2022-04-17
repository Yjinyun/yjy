"""
第一行包含整数 n 和 m。
第二行包含 n 个整数，表示整数数列。

输入样例：
5 3
4 5 1 3 2
输出样例：
1 2 3
"""


def down(x):
    t = x
    if (x * 2 <= n and h[x * 2] < h[t]): t = x * 2
    if (x * 2 + 1 <= n and h[x * 2 + 1] < h[t]): t = x * 2 + 1
    if (t != x):
        h[x], h[t] = h[t], h[x]
        down(t)


n, m = map(int, input().split())
h = list(map(int, input().split()))
h.insert(0, 0)
s = n
# 初始化堆
for i in range(n // 2, 0, -1):
    down(i)
while m:
    m -= 1
    print(h[1], end=' ')
    h[1] = h[n]
    n -= 1
    down(1)
