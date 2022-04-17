def merge_sort(str):
    if len(str) <= 1:
        return
    mid = len(str) // 2
    L = str[:mid]
    R = str[mid:]
    merge_sort(L)
    merge_sort(R)

    # 合并子问题
    k = 0
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            str[k] = L[i]
            i += 1
        else:
            str[k] = R[j]
            j += 1
        k += 1
    while i < mid:
        str[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        str[k] = R[j]
        k += 1
        j += 1





