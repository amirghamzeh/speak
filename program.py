from Student import Student
from Person import Person

# name = input("Enter first name: ")
# lastname = input('Enter last name: ')
# age = int(input('Enter age: '))

# userPerson = Person(name, lastname, age)
# userPerson = Person(lastname=lastname, name=name, age=age)
# userPerson.introduce()

person1 = Person('Masood', 'Babamohammadi', 25)
person2 = Student('Abolfazl', 'Alizadeh', gender="female", isStudy=True)
# person1.introduce()
# person2.introduce()
person2.duStudyYourLesson()