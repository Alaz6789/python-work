def find_even(*nums):
    even = []
    for num in nums:
        if num%2==0:
            even.append(num)
    print(f"the even numbers are {even}")

find_even(12,13,15,78,45)