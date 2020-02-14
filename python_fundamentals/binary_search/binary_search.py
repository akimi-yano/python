# normal binary search

# def binary_search(arr, val):
#     if len(arr)<=0:
#         return False

#     begin = 0
#     end = len(arr)-1
#     while begin <= end:
#         idx = (begin+end)//2
#         if arr[idx]==val:
#             return idx
#         if arr[idx]<val:
#             begin = idx +1
#         if arr[idx]>val:
#             end  =idx-1
#     return False

# print(binary_search([1,2,3,4,5],5))


#recursion ver.

def bin_search(arr, val):
    return re_b_s(arr,val, 0, len(arr)-1)
    

def re_b_s(arr,val, begin, end):
    #base_case_1
    if begin>end:
        return False
    idx = (begin+end)//2
    #base_case_2
    if arr[idx]==val:
        return idx
    if arr[idx]<val:
        return re_b_s(arr, val, idx+1, end)
    if arr[idx]>val:
        return re_b_s(arr, val, begin, idx-1)

print(bin_search([1,2,3,4,5],5))