total = 0
sum = 0
digits = []
nums = int(input("Choose a number: "))
copy = nums
#noOfdigits = len(str(num))
while nums > 0:
    digits.append(nums % 10)
    nums = (nums - nums % 10) // 10
for num in digits:
    total = total + 1
for digit in digits:
    product = digit**total
    sum = product + sum
if sum == copy:
    print(f"{copy} is an armstrong number")
else:
    print(f"{copy} is not an armstrong number")