import pyttsx3

class Person:
    def __init__(self, name, lastname, age = 0, gender = 'male'):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def speak(self, text):
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        if self.gender == 'male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()

    def introduce(self):
        # text = "Hello my name is " + self.name + " " + self.lastname
        # text = f"Hello my name is {self.name} {self.lastname}"
        if self.age == 0:
            text =  "Hello my name is %s %s" % (self.name, self.lastname)
        else:
            text = "Hello my name is %s %s and im %d years old" % (self.name, self.lastname, self.age)
        self.speak(text)
        
    
        