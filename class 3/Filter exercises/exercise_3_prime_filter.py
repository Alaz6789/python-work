def is_prime(n):
    total = 0
    if int(n) < 2:
        print("Not prime")
        exit()
    
    else:
        for x in range(2, int(n)):
            integer = int(n) / x

            if integer == round(integer, 0):
                print("Not prime")
                exit()

            else:
                total = total + 1

        if total == int(n) - 2:
            print("Is prime")
            exit()

num = input("Choose a number: ")
is_prime(num)