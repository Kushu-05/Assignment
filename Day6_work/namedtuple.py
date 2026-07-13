from collections import  namedtuple
Student=namedtuple("Student",["name","age","grade"])
student1=Student("Alice",20,"A")
print(student1.name)
print(student1.age)
print(student1.grade)
