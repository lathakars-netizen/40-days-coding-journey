## sum of digigts using recursion
def sum_of_digits(n):
    n = abs(n) 
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)
print(sum_of_digits(3245))  # Output: 14

##  Print All Strings Using 'A' and 'B' of Length 3 (Backtracking)
def ab_strings(length):
    def backtrack(current_str):
        if len(current_str) == length:
            print("".join(current_str))
            return
        for char in ['A', 'B']:
            current_str.append(char)
            backtrack(current_str)
            current_str.pop()
    backtrack([])
ab_strings(3)
