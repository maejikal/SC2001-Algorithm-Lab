global comparisons
mergesort_comparisons = [0]
def merge(l1, l2):
    print(l1, l2)
    ans = []
    p1 = 0
    p2 = 0
    while p1<len(l1) and p2<len(l2):
        mergesort_comparisons[0] += 1
        if l1[p1] < l2[p2]:
            ans.append(l1[p1])
            p1+=1
        else:
            ans.append(l2[p2])
            p2+=1
    ans.extend(l1[p1:])
    ans.extend(l2[p2:])
    return ans

def mergesort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    
    return merge(mergesort(left), mergesort(right))

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


def integrate(lst):
    pass

# lst = [5, 4, 2, 1, 3, 9, 10, 15, 12]
lst = [6, 4, 1, 3, 5, 2]
# print(insertionsort(lst)[0])
print(mergesort(lst))
print(mergesort_comparisons)