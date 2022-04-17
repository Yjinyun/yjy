"""
双链表
在最左侧插入一个数；
在最右侧插入一个数；
将第 k 个插入的数删除；
在第 k 个插入的数左侧插入一个数；
在第 k 个插入的数右侧插入一个数
"""

# 初始化
N = 100010
e = [0] * N
r = [0] * N
l = [0] * N
idx = 2
l[1] = 0
r[0] = 1


# 在地k个节点后插入x
def add(k, x):
    global idx
    e[idx] = x
    l[idx] = k
    r[idx] = r[k]
    l[r[k]] = idx
    r[k] = idx
    idx += 1


def delete(k):
    l[r[k]] = l[k]
    r[l[k]] = r[k]


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        str = list(input().split())
        if str[0] == 'L':
            add(0, int(str[1]))
        elif str[0] == 'R':
            add(l[1], int(str[1]))
        elif str[0] == 'D':
            delete(int(str[1]) + 1)
        elif str[0] == 'IL':
            k, x = map(int, str[1:])
            add(l[k + 1], x)
        else:
            k, x = map(int, str[1:])
            add(k + 1, x)

    i = r[0]
    while i != 1:
        print(e[i], end=' ')
        i = r[i]

"""
L x，表示在链表的最左端插入数 x。
R x，表示在链表的最右端插入数 x。
D k，表示将第 k 个插入的数删除。
IL k x，表示在第 k 个插入的数左侧插入一个数。
IR k x，表示在第 k 个插入的数右侧插入一个数
输入样例：
10
R 7
D 1
L 3
IL 2 10
D 3
IL 2 7
L 8
R 9
IL 4 7
IR 2 2
输出样例：
8 7 7 3 2 9
"""