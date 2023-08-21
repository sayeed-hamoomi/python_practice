from collections import defaultdict


def duplicates(arr, n):
    d = defaultdict(lambda: 0)
    a = []
    for i in arr:
        d[i] += 1
        if d[i] > 1 and i not in a:
            a.append(i)
    # print((sorted(a)), len(a))
    if len(a) == 0:
        a.append(-1)
    a = sorted(a)
    return a


print(duplicates([3, 2, 1, 3, 1], 5))
