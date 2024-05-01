def prime_checker(number):
    n = int(input("Check this number: "))
    is_prime = True
    for i in range(2, n - 1):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime a number.")
prime_checker(number="n")
input()
