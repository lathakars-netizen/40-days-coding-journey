file = open("name.txt", "w")
name =input("Enter name: ")
file.write(name)
file.close()


file = open("name.txt", "r")
print(file.read())
file.close()