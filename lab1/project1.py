import random

from alive_progress import alive_bar #progress bar for loops

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

#Pure MergeSort
def mergesort(lst):
    if len(lst)<=1:
        return lst[:], 0
    mid = len(lst)//2
    left, left_comps = mergesort(lst[:mid])
    right, right_comps = mergesort(lst[mid:])
    merged, merge_comps = merge(left, right)
    return merged, left_comps + right_comps + merge_comps

#Pure InsertionSort
def insertionsort(lst):
    arr = lst[:] 
    comparisons = 0 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i - 1 
        while j >= 0: 
            comparisons += 1 
            if arr[j] > key: 
                arr[j + 1] = arr[j] 
                j -= 1 
            else: 
                break 
            arr[j + 1] = key 
    return (arr, comparisons)

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
#function to generate datasets (for different sizes)
def generate_datasets(sizes,x): #x is the max value of the random integers
    datasets={}
    for n in sizes:
        datasets[n]=[random.randint(0,x) for _ in range(n)]
    return datasets
sizes=[1000,5000,10000,50000,100000,500000,1000000,5000000,10000000]
datasets=generate_datasets(sizes,1000000000) #dictionary of datasets with key as size

#function to generate multiple datasets (for same size)
def generate_datasets_n(size,number_of_datasets,x): 
    datasets={}
    for n in range(number_of_datasets):
        datasets[n]=[random.randint(0,x) for _ in range(size)]
    return datasets #dictionary of datasets with same size


#PART C: TESTING THE SORTS AND MAKING GRAPHS

#PART C.1:












#PART C.2:

"""With the input size n fixed, plot the number of key comparisons over
different values of S. Compare your empirical results with your
theoretical analysis of the time complexity."""

# Testing on input size n
n = 10000
number_of_datasets = 100
x = 1000000000
# generate 100 datasets of size n
datasets_c_2 = generate_datasets_n(n, number_of_datasets, x)
print(f"Generated {len(datasets_c_2)} datasets of size {n} for testing.")
s = [x for x in range(1,101)] # S values from 1 to 100
comps_hyb_dict = {}
with alive_bar(len(s), title="Comparison counting in progress...") as bar:
    for i in s:
        avg_comps = 0 #average comparisons for each S value
        for j in datasets_c_2:
            avg_comps += integrate(datasets_c_2[j], i)[1] #adding up comparisons for each S value
        comps_hyb_dict[i] = avg_comps/len(datasets_c_2) #average comparisons for each S value
        bar()

# plotting the graphs
import matplotlib.pyplot as plt
plt.plot(list(comps_hyb_dict.keys()), list(comps_hyb_dict.values()))
plt.xlabel("S values")
plt.ylabel("Average number of comparisons")
plt.title(f"Average number of comparisons vs S values (n={n})")
plt.grid()
plt.show()

#PART C.3:
# lst=datasets[100000] #sample list
# lst1 = datasets[100000].copy()
# S = 15
# # test pure insertion sort
# sorted_hyb, comps_hyb = integrate(lst, S)
# sorted_mrg, comps_mrg = mergesort(lst1)
# sorted_ins, comps_ins = insertionsort(lst[:])

# print("Total Number of Key Comparisons")
# print (f"Pure Insertion Sort: {comps_ins} \nPure Merge Sort: {comps_mrg} \nHybrid Algorithm with S={S}: {comps_hyb}")
# print(f"Difference in comparisons between Hybrid and Pure Merge Sort: {comps_hyb - comps_mrg}")