import math


#Mostly used for educational purpose
#O(n^2)
def bubble_sort(a):
    for _ in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t 
    return a 

#mostly used for teaching
#O(n^2)
def selection_sort(a):
    for i in range(len(a)-1):
        index = i
        for j in range(i,len(a)-1):
            # temp = a[i]
            if a[j] < a[i]:
                # temp = a[j]
                index = j
        x = a[i]
        a[i] = a[index]
        a[index] = x
    return a 

#Insertion Sort
# used when array is almost sorted and small data set..best case is O(n) ; best to use when
# small dataset which is almost sorted - space compleity O(1)

def insertion_sort(a):
    for i in range(len(a)-1):
        if a[i+1] < a[i]:
            temp = a[i+1]
            for j in range(i,-1,-1) :
                if a[j]>temp:
                    a[j+1] = a[j]
                # else:
                    a[j] = temp
                    # break
    return a 

# Divide and conquer sortings 
# Merge Sort and Quick Sort and  have O(nlogn) but space complexity is higher O(n)
# shouldnt be used when memory is constrained
def merge_sort(a):
    if len(a) == 1:
        return a
    
    l = math.floor(len(a)/2)
    left = a[:l]
    right = a[l:]

    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    result = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]
l1 = [5,6,3,1,8,7,2,4,12,1222,31,2]
# l = [ 1,5,12,12,0,135,1,21,12,35,51,12,35,12,5556,2,3,222,0]
# print(bubble_sort(l))
# print(selection_sort(l))
# print(insertion_sort(l))
print(merge_sort(l1))


#quick sort is good but worst case is pretty bad

# comparison sor vs non-comparison sort
# comparison sort 
# bubble sort
# selection sort 
# insetion sort
# merge sort 
# quick sort



# non-comparison sort
# radix sort
# counting sort