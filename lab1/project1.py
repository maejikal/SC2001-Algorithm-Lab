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

def mergesort(lst):
    if len(lst)<=1:
        return lst, 0
    mid = len(lst)//2
    left, left_comps = mergesort(lst[:mid])
    right, right_comps = mergesort(lst[mid:])
    merged, merge_comps = merge(left, right)
    return merged, left_comps + right_comps + merge_comps

def insertionsort(lst): 
    comparisons = 0 
    for i in range(1, len(lst)): 
        key = lst[i] 
        j = i - 1 
        while j >= 0: 
            comparisons += 1 
            if lst[j] > key: 
                lst[j + 1] = lst[j] 
                j -= 1 
            else: 
                break 
            lst[j + 1] = key 
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
sorted_mrg, comps_mrg = mergesort(lst1)
S = 15
sorted_hyb, comps_hyb = integrate(lst, S)
print("Total Number of Key Comparisons")
print ("Pure Insertion Sort: " + str(comps_ins) + "\nPure Merge Sort: " + str(comps_mrg) + "\nHybrid Algorithm with S="+str(S)+": " + str(comps_hyb))