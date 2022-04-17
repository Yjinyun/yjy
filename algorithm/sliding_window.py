"""
滑动窗口
给定大小为n的数组，滑动窗口大小为k,滑动窗口每次移动一个位置
确定滑动窗口位于每个位置时，窗口中的最大值和最小值。
该数组为 [1 3 -1 -3 5 3 6 7]，k 为 3。
窗口位置         	  最小值	  最大值
[1 3 -1] -3 5 3 6 7	    -1  	3
1 [3 -1 -3] 5 3 6 7	    -3	    3
1 3 [-1 -3 5] 3 6 7	    -3	    5
1 3 -1 [-3 5 3] 6 7	    -3	    5
1 3 -1 -3 [5 3 6] 7	    3	    6
1 3 -1 -3 5 [3 6 7]	    3	    7
"""

from collections import deque

n, k = map(int, input().split())
str = list(map(int, input().split()))

def max_min(func):
    q = deque()
    for i, u in enumerate(str):
        if q and i-q[0][0] == k: q.popleft()
        while q and func(q[-1][1], u): q.pop()
        q.append((i, u))
        if i >= k-1: print(q[0][1], end=' ')
    print("")

max_min(lambda x, y : x > y)
max_min(lambda x, y : x < y)

"""
输入样例：
8 3
1 3 -1 -3 5 3 6 7
输出样例：
-1 -3 -3 -3 3 3
3 3 5 5 6 7
"""