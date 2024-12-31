first_element = int(input())
difference = int(input())
progression = [first_element + i * difference for i in range(10)]
print(progression)