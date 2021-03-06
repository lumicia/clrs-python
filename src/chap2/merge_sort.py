def merge(a: list[int | float], p: int, q: int, r: int) -> None:
    left = a[p : q + 1]
    right = a[q + 1 : r + 1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort(a: list[int | float], p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
