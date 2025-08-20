total = 0
sum1 = 0
average = 0
list1 = []
for x in range(1,6):
    num = int(input("Choose a number to store: "))
    list1.append(num)
    sum1 = sum1 + num
for integer in list1:
    integer = integer**2
average = sum1/5
print(f"your list of numbers is {list1}")
print(f"the sum of the integers is {sum1}")
print(f"the average is {average}")
