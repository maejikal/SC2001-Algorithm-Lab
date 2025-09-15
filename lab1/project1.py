import random

def merge(l1, l2):
    print(l1, l2)
    ans = []
    p1 = 0
    p2 = 0
    comparisons = 0
    while p1<len(l1) and p2<len(l2):
        comparisons += 1
        if l1[p1] < l2[p2]:
            ans.append(l1[p1])
            p1+=1
        else:
            ans.append(l2[p2])
            p2+=1
    ans.extend(l1[p1:])
    ans.extend(l2[p2:])
    return (ans, comparisons)

"""def mergesort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    
    return merge(mergesort(left), mergesort(right))"""

def insertionsort(lst):
    comparisons = 0
    for i in range(1, len(lst)):
        j = i
        while j > 0:
            comparisons+=1
            if lst[j]<lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j-=1
            else:
                break
    return (lst, comparisons)


def integrate(lst, S=10):
    def hybrid(arr):
        n = len(arr)
        if n <= 1:
            return (list(arr), 0)
        if n <= S:
            return insertionsort(arr)
        mid = n // 2
        left_sorted, left_comp = hybrid(arr[:mid])
        right_sorted, right_comp = hybrid(arr[mid:])
        merged, merge_comp = merge(left_sorted, right_sorted)
        return (merged, left_comp + right_comp + merge_comp)

    return hybrid(lst)

#lst = [4, 3,21,143,14,234,4,12331231,423,25,522,34525,123]
lst=[]
for i in range(10000):
    lst.append(random.randint(0, 1000000))
sorted_ins, comps_ins = insertionsort(lst[:])
sorted_hyb, comps_hyb = integrate(lst)
print ((comps_ins, comps_hyb))
#print((sorted_ins, comps_ins))
#print((sorted_hyb, comps_hyb))