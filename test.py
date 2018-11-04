class Student():
    pass

mingyue = Student()

class PythonStudent():
    name = None
    age = 19
    course = "Python"
    
    def doHomework(self):
        print("I am doing my homework!")
        return None
    
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()
