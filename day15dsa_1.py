str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

## Two-Pointer Technique (Introduction)
## The two-pointer technique uses two indexes to solve problems efficiently.
text = list("Python")
left = 0
right = len(text) - 1

while left < right:
    text[left], text[right] = text[right], text[left]
    left += 1
    right -= 1

print("".join(text))