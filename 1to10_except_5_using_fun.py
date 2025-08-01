# '1to10_except_5_using_fun.py'
def print_numbers():
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)

print_numbers()