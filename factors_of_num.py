# 'factors_of_num.py'
num = int(input("Enter a number to find its factors: "))
print(f"The factors of {num} are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)