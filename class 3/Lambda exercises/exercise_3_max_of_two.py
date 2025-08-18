num1 = int(input("Choose the first number: "))
num2 = int(input("Choose the second number: "))

max2 = lambda x,y: x if x > y else y 

print(max2(num1,num2))