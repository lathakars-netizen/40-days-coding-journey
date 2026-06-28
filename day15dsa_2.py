text = input("Enter a sentence: ")
print(text.replace(" ", ""))  ## rmeove spaces

text = input("Enter a sentence: ")
words = text.split()
largest = max(words, key=len)
print(largest)  ## largest word ina sentence