"""
单链表
向链表头插入一个数；
删除第 k 个插入的数后面的数；
在第 k 个插入的数后插入一个数
"""

def insert_head(x):
    global idx, e, ne, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1


def delete(k):
    global idx, e, ne, head
    ne[k] = ne[ne[k]]


def insert(k, x):
    global idx, e, ne, head
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx
    idx += 1


if __name__ == "__main__":
    N = 100010
    n = int(input())
    head = -1
    idx = 0
    e = [0] * N
    ne = [0] * N
    for i in range(n):
        str = list(input().split())
        if str[0] == 'H':
            insert_head(int(str[1]))
        elif str[0] == 'I':
            insert(int(str[1]) - 1, int(str[2]))
        else:
            if int(str[1]) == 0:
                head = ne[head]
            else:
                delete(int(str[1]) - 1)

    i = head
    while i != -1:
        print(e[i], end=' ')
        i = ne[i]

"""
H x，表示向链表头插入一个数 x。
D k，表示删除第 k 个插入的数后面的数（当 k 为 0 时，表示删除头结点）。
I k x，表示在第 k 个插入的数后面插入一个数 x（此操作中 k 均大于 0）
输入样例：
10
H 9
I 1 1
D 1
D 0
H 6
I 3 6
I 4 5
I 4 5
I 3 4
D 6
输出：
6 4 6 5
"""