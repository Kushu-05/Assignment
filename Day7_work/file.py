file = open('student.txt', 'r')
data =file.read()
print(data)
file.close()

file = open('student.txt', 'w')
file.write("This is a new line of text.\n")
file.write("This is another line of text.\n")
file.close()

file = open('student.txt', 'r')
data = file.read()
print(data)
file.close()