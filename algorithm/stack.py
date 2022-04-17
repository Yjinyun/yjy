"""
实现栈，支持四种操作
push x – 向栈顶插入一个数 x；
pop – 从栈顶弹出一个数；
empty – 判断栈是否为空；
query – 查询栈顶元素。
"""


def push(x):
    stack.append(x)


def pop():
    del stack[-1]


def empty():
    if stack == []:
        print("YES")
    else:
        print('NO')


def query():
    print(stack[-1])


if __name__ == "__main__":
    stack = []  # 列表实现栈
    x = int(input())
    for i in range(x):
        str = list(input().split())
        if str[0] == "push":
            push(int(str[1]))
        elif str[0] == 'pop':
            pop()
        elif str[0] == 'query':
            query()
        else:
            empty()


"""
输入样例：
10
push 5
query
push 6
pop
query
pop
empty
push 4
query
empty
输出样例：
5
5
YES
4
NO
"""