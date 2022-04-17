"""
实现一个队列，队列初始为空，支持四种操作：

push x – 向队尾插入一个数 x；
pop – 从队头弹出一个数；
empty – 判断队列是否为空；
query – 查询队头元素。
"""

N = 100010
queue = []
head = tail = 0

n = int(input())
for i in range(n):
    str = list(input().split())
    if str[0] == "push":
        # queue[tail] = int(str[1])
        # tail += 1
        queue.append(int(str[1]))
    elif str[0] == "pop":
        del queue[0]
        # head += 1
    elif str[0] == "empty":
        if queue == []:
            print("YES")
        else:
            print("NO")
    elif str[0] == "query":
        print(queue[0])

"""
输入样例：
10
push 6
empty
query
pop
empty
push 3
push 4
pop
query
push 6
输出样例：
NO
6
YES
4
"""