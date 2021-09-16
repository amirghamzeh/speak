from Person import Person


class Student(Person):
    
    def __init__(self, name, lastname, age = 0, gender = 'male', isStudy = False):
        super().__init__(name, lastname, age=age, gender=gender)
        
        self.isStudy = isStudy

    def duStudyYourLesson(self):
        if self.isStudy == False:
            text = "no im not"
        else:
            text = "yes im study my lesson"
        
        self.speak(text)