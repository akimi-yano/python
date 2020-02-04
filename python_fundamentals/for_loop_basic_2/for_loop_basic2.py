#1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i]>0:
#             list[i] = 'big'
#     return list
# print(biggie_size([-1, 3, 5, -5]))


#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def count_positives(list):
#     counter = 0
#     for i in range(len(list)):
#         if list[i]>0:
#             counter +=1
#     list[len(list)-1]=counter
#     return list
# # print(count_positives([1,6,-4,-2,-7,-2]))
# print(count_positives([-1,1,1,1]))


#3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_total(list):
#     sum = 0
#     for i in range(len(list)):
#         sum+=list[i]
#     return sum
# # print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

#4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def average(list):
#     sum=0
#     for i in range(len(list)):
#         sum+=list[i]
#     avg = sum/len(list)
#     return avg
# print(average([1,2,3,4]))


#5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(list):
#     return len(list)
# print(length([37,2,1,-9]))
# print(length([]))

#6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(list):
#     if len(list)<1:
#         return False
#     min = list[0]
#     for i in range(len(list)):
#         if list[i]< min:
#             min = list[i]
#     return min
# print(minimum([37,2,1,-9]))
# print(minimum([]))

#7. Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(list):
#     if len(list)<1:
#         return False
#     max = list[0]
#     for i in range(len(list)):
#         if list[i]> max:
#             max = list[i]
#     return max
# print(maximum([37,2,1,-9]))
# print(maximum([]))

#8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(list):
#     dict = {}
#     sumTotal = 0
#     minimum = list[0]
#     maximum = list[0]
#     for i in range(len(list)):
#         if list[i] > maximum:
#             maximum = list[i]
#         if list[i] < minimum:
#             minimum = list[i]
#         sumTotal += list[i]
#     average = sumTotal/len(list)
#     dict['sumTotal'] = sumTotal
#     dict['average'] = average
#     dict['minimum'] = minimum
#     dict['maximum'] = maximum
#     dict['length'] = len(list)
#     return dict
# print(ultimate_analysis([37,2,1,-9]))

#9. Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse_list(list):
#     for i in range(len(list)//2):
#         temp = list[i]
#         list[i] = list[len(list)-1-i]
#         list[len(list)-1-i] = temp
#     return list
# print(reverse_list([37,2,1,-9]))