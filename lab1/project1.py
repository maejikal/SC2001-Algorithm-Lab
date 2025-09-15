def merge(l1, l2):
    ans = []
    p1 = 0
    p2 = 0
    while p1<len(l1) and p2<len(l2):
        if l1[p1] < l2[p2]:
            ans.append(l1[p1])
            p1+=1
        else:
            ans.append(l2[p2])
            p2+=1
    ans.extend(l1[p1:])
    ans.extend(l2[p2:])
    return ans

"""def mergesort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    
    return merge(mergesort(left), mergesort(right))"""

def insertionsort(lst):
    a = list(lst)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def integrate(lst, S=10):
    def hybrid(arr):
        n = len(arr)
        if n <= 1:
            return list(arr)
        if n <= S:
            return insertionsort(arr)
        mid = n // 2
        left = hybrid(arr[:mid])
        right = hybrid(arr[mid:])
        return merge(left, right)

    return hybrid(lst)

lst = [4, 3,21,143,14,234,4,12331231,423,25,522,34525,123]
print(insertionsort(lst))
print(integrate(lst))