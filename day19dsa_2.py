# Countdown Recursion
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

## print numbers n to 1
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)