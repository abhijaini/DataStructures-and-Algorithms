def mergeArrays(l1,l2):
    result = []
    i=0
    j=0
    while(l1[i] or l2[j]):
        print(l1[i] , l2[j])
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i = i + 1
        else:
            result.append(l2[j])
            j = j + 1
    return result
list1 = [1,2,5,7]
list2 = [3,4,5,8,9,12]
print(mergeArrays(list1,list2))
