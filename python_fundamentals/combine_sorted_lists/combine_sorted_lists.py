def marge_sorted_lists(arr1,arr2):
    arr3=[]
    i=0
    j=0
    while(i < len(arr1) or j < len(arr2)):
        if i<len(arr1):
            if j<len(arr2):
                if arr1[i]<arr2[j]:
                    arr3.append(arr1[i])
                    i+=1
                else:
                    arr3.append(arr2[j])
                    j+=1
            else:
                arr3.append(arr1[i])
                i+=1
        else:
            if j<len(arr2):
                arr3.append(arr2[j])
                j+=1
    return arr3
print(marge_sorted_lists([1,3,6], [3,4,5]))
        