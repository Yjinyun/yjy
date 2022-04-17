"""
模板串 P 在模式串 S 中多次作为子串出现。
求出模板串 P 在模式串 S 中所有出现的位置的起始下标。
"""

m = int(input())
p = list(input())
n = int(input())
s = list(input())
p.insert(0, 0)
s.insert(0, 0)
ne = [0] * (m+1)

# 求ne数组
i, j = 2, 0
while i <= m:
    while j and p[j + 1] != p[i]: j = ne[j]
    if p[j + 1] == p[i]: j += 1
    ne[i] = j
    i += 1

i, j = 1, 0
while i <= n:
    while j and p[j + 1] != s[i]: j = ne[j]
    if p[j + 1] == s[i]: j += 1
    if j == m:
        print(i - m, end=' ')
        j = ne[j]
    i += 1



"""
输入样例：
3
aba
5
ababa
输出样例：
0 2
"""