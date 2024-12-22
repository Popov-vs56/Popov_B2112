from random import randint

lst = [randint(-10, 10) for i in range(20)]
print(lst)

sum_negative = 0

for num in lst:
    if num < 0:sum_negative += num
    print("Sum negative item list: ", sum_negative)