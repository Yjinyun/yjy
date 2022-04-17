"""
给定一个按照升序排列的长度为 n 的整数数组，以及 q 个查询。
对于每个查询，返回一个元素 k 的起始位置和终止位置（位置从 0 开始计数）。
如果数组中不存在该元素，则返回 -1 -1
"""


def main():
    n, m = map(int, input().split())
    str = list(map(int, input().split()))
    for i in range(m):
        k = int(input())
        l, r = 0, n - 1
        while l < r:
            mid = l + r >> 1
            if str[mid] >= k:
                r = mid
            else:
                l = mid + 1
        if str[l] != k:
            print('-1 -1')
        else:
            print(l, end=' ')
        # 找终止下标
        l, r = 0, n - 1
        while l < r:
            mid = l + r + 1 >> 1
            if str[mid] <= k:
                l = mid
            else:
                r = mid - 1
        if str[l] == k:
            print(l)


main()

"""
输入样例：
6 3
1 2 2 3 3 4
3
4
5
输出样例：
3 4
5 5
-1 -1
"""