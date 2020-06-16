#O(n^2)
def bubble_sort(a):
    for _ in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t 
    return a 

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

# used when array is almost sorted and small data set..best case is O(n)

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

l1 = [5,6,3,1,8,7,2,4]
l = [ 1,5,12,12,0,135,1,21,12,35,51,12,35,12,5556,2,3,222,0]
# print(bubble_sort(l))
# print(selection_sort(l))
print(insertion_sort(l))