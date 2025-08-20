def is_prime(n):
    total = 0
    if n < 2:
        print("Not prime")
        exit()
    
    else:
        for x in range(2, n):
            integer = n / x

            if integer == round(integer, 0):
                print("Not prime")
                exit()

            else:
                total = total + 1

        if total == n - 2:
            print("Is prime")
            exit()

#num = input("Choose a number: ")
#is_prime(num)

nums = list(range(2,30))
primes = filter(is_prime(nums))
print(primes)