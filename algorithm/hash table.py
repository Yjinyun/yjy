"""
模拟散列表
维护一个集合，支持如下几种操作：
I x，插入一个数 x；
Q x，询问数 x 是否在集合中出现过；
"""

N = 100003
e = [0] * N
ne = [0] * N
h = [-1] * N
idx = 0


def insert(x):
    global idx
    k = (x % N + N) % N
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx
    idx += 1


def query(x):
    k = (x % N + N) % N
    i = h[k]
    while (i != -1):
        if e[i] == x:
            return True
            break
        i = ne[i]
    return False


def main():
    n = int(input())
    for i in range(n):
        str = input().split()
        if str[0] == "I":
            insert(int(str[1]))
        else:
            if query(int(str[1])):
                print("Yes")
            else:
                print("No")

main()


"""
输入样例：
5
I 1
I 2
I 3
Q 2
Q 5
输出样例：
Yes
No
"""