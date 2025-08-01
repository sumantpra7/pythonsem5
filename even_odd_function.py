# 'even_odd_function.py'
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 7
print(f"The number {num} is {check_even_odd(num)}.")
# Output: The number 7 is Odd.