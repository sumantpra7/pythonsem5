# 'even_odd_function.py'
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 7
print(f"The number {num} is {check_even_odd(num)}.")

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if is_prime(num):
    print(f"The number {num} is Prime.")
else:
    print(f"The number {num} is Not Prime.")
