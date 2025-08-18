nums = [1,2,3,4,5,6,7,8,9,10]

odd = list(filter(lambda x: x % 2 == 1, nums))

square = list(map(lambda x: x * x, odd))

print(square)