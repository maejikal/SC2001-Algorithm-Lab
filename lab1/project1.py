import random
import math
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

"""With the value of S fixed, plot the number of key comparisons over
different sizes of the input list n. Compare your empirical results with
your theoretical analysis of the time complexity."""

import numpy as np   # add here since not imported above
import matplotlib.pyplot as plt  # already imported later

# fixed threshold S
S_fixed = 20

# input sizes to test
n_values = [1000, 2000, 5000, 10000, 20000, 50000]

# number of datasets per n
trials = 5

# set reproducible random seed
random.seed(2025)
np.random.seed(2025)

comps_n_dict = {}

with alive_bar(len(n_values), title="Comparison counting for fixed S...") as bar:
    for n in n_values:
        avg_comps = 0
        for _ in range(trials):
            dataset = [random.randint(0, 10**9) for _ in range(n)]
            _, comps = integrate(dataset, S_fixed)
            avg_comps += comps
        comps_n_dict[n] = avg_comps / trials
        bar()

def theoretical_comparisons(n, S): #approx number of comparisons for hybrid
    if S >= n:
        # if S >= n, it's just insertion sort on the whole array
        return  (n * (n-1) / 4)
    return n * math.log2(n / S) + (n * (S-1) / 4)

theoretical_results_n = {n: theoretical_comparisons(n, S_fixed) for n in n_values}

# plotting empirical vs theoretical results
plt.plot(list(comps_n_dict.keys()), list(comps_n_dict.values()), label="Empirical", marker="o")
plt.plot(list(theoretical_results_n.keys()), list(theoretical_results_n.values()),
         label="Theoretical", linestyle="--", marker="x")

plt.xlabel("Input size n (log scale)")
plt.ylabel("Number of comparisons")
plt.xscale("log")
plt.title(f"Empirical vs Theoretical Comparisons (S={S_fixed})")
plt.legend()
plt.grid(True)
plt.show()

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


# n and s were definied earlier, n = 10000, s = [x for x in range(1,101)]
theoretical_results = {S: theoretical_comparisons(n, S) for S in s}

import matplotlib.pyplot as plt
# plotting empirical vs theoretical results
plt.plot(list(comps_hyb_dict.keys()), list(comps_hyb_dict.values()), label="Empirical")
plt.plot(list(theoretical_results.keys()), list(theoretical_results.values()), label="Theoretical", linestyle="--")

plt.xlabel("S values")
plt.ylabel("Number of comparisons")
plt.title(f"Empirical vs Theoretical Comparisons (n={n})")
plt.legend()
plt.grid(True)
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
