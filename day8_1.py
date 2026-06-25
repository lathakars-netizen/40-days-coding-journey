## write data to file
##file = open("student.txt", "w")
##file.write("Hello Simhadri")
##file.close()

## read data from file
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

## Append data
file = open("student.txt", "a")
file.write("\nWelcome to Python")
file.close()
