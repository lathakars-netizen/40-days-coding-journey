def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)
print(sum_numbers(5))

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)