#text = input("enter the text:")
#count = 0
#for ch in text.lower():
#   if ch in'aeiou':
#       count+=1
#print("vowels:",count) 


text = input("enter the text:")
count = 0
for ch in text.lower():
    if ch not in'aeiou':
        count+=1
print("consonants:",count) 