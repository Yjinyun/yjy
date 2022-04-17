def quick_sort(q, start, end):
    if start >= end: return
    left, right = start, end
    pivot = q[(start + end) // 2]  # 选取一个哨兵
    while left <= right:
        while q[left] < pivot:
            left += 1
        while q[right] > pivot:
            right -= 1
        if left <= right:
            q[left], q[right] = q[right], q[left]
            left += 1
            right -= 1
    quick_sort(q, start, right)
    quick_sort(q, left, end)





