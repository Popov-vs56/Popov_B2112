from random import randint

lst = [randint(-10, 10) for i in range(20)]
print(lst)

sum_negative = 0
for num in lst:
    if num < 0:sum_negative += num
print("Sum negative item list: ", sum_negative)

sum_of_even = 0
for num in lst:
    if num % 2 == 0:sum_of_even += num
print("Sum of even item list: ", sum_of_even)


sum_of_odd = 0
for num in lst:
    if num % 2 != 0:
        sum_of_odd += num
print("Sum of odd item list: ", sum_of_odd)

sum_elements_mult_3 = 0
for num in lst:
    if num % 3 == 0:
        sum_elements_mult_3 += num
print("Sum of elements items multiply of 3 list: ", sum_elements_mult_3)

mult_range = 1
min_value_list = min(lst)
max_value_list = max(lst)
index_min = lst.index(min_value_list)
index_max = lst.index(max_value_list)
if index_max < index_min:
    index_max,index_min = index_min,index_max
for i in range(index_min,index_max,1):
    mult_range *= lst[i]
print("The product of the elements between the minimum and maximum elements:", mult_range)
