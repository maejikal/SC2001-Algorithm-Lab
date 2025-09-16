import random

def merge(l1, l2):
    #print(l1, l2)
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

# pure merge sort function
def mergesort(lst):
    if len(lst)<=1:
        return (list(lst), 0)
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    
    left_sorted, left_comp = mergesort(left)
    right_sorted, right_comp = mergesort(right)
    merged, merge_comp = merge(left_sorted, right_sorted)
    return (merged, left_comp + right_comp + merge_comp)

# pure insertion sort function
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

#PART A: HYBRID SORT
#function that integrates the insertion sort and the merge sort logics
def integrate(lst, S=15):
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

#PART B: GENERATION OF DATASETS
#function to generate datasets
def generate_datasets(sizes,x):
    datasets={}
    for n in sizes:
        datasets[n]=[random.randint(0,x) for _ in range(n)]
    return datasets
sizes=[1000,5000,10000,50000,100000,500000,1000000,5000000,10000000]
datasets=generate_datasets(sizes,1000000000)


#PART C: TESTING THE SORTS AND MAKING GRAPHS

#PART C.1:












#PART C.2:













#PART C.3:
lst=datasets[100000] #sample list

# test pure insertion sort
sorted_ins, comps_ins = insertionsort(lst[:])


# test pure merge sort
sorted_merge, comps_merge = mergesort(lst[:])


# test hybrid (integrated) sort
sorted_hyb, comps_hyb = integrate(lst)


# comparison summary
print("\ncomparison summary:")
print(f"insertion sort: {comps_ins} comparisons")
print(f"merge sort: {comps_merge} comparisons")
print(f"hybrid sort: {comps_hyb} comparisons")
print(f"\nhybrid vs pure merge sort: {comps_hyb} vs {comps_merge} (difference: {comps_hyb - comps_merge})")