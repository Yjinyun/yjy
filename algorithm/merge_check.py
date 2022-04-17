"""
并查集：支持两种操作,n个数，m个操作
M a b，将编号为 a 和 b 的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
Q a b，询问编号为 a 和 b 的两个数是否在同一个集合中；
"""

N = 100010
p = [0] * N

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def main():
    n, m = map(int, input().split())
    i = 1
    for i in range(n + 1): p[i] = i

    for i in range(m):
        str = input().split()
        a, b = int(str[1]), int(str[2])
        if str[0] == 'M':
            p[find(a)] = find(b)
        else:
            if find(a) == find(b):
                print("Yes")
            else:
                print("No")

main()


"""
输入样例：
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
输出样例：
Yes
No
Yes
"""