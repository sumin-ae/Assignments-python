
prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

def check_prime_in_set(number):
    if number in prime_set:
        return f"{number} is a prime number in the set."
    else:
        return f"{number} is not in the prime number set."


user_input = int(input("Enter a number to check: "))
print(check_prime_in_set(user_input))
