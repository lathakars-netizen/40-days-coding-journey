# Simple Backtracking Example
## Print all binary strings of length 3.

def generate(s, n):
    if len(s) == n:
        print(s)
        return
    generate(s + "0", n)
    generate(s + "1", n)

generate("", 3)