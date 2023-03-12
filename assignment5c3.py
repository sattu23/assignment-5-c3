# Challenge 3 implement the complete student class

class student:
    
    def __init__(self,name,rollno):
        self._name=name
        self._rollno=rollno
    def set_name(self,x):
        self._name=x
        pass
    def get_name(self):
        return self._name
    pass
    def set_rollno(self,x):
        self._rollno=x
        pass
    def get_rollno(self):
        return self._rollno
    pass
name=input('enter name>>')
rollno=int(input('enter roll no>>'))
s=student(name,rollno)
s.set_name(name)
print(s.get_name())
s.get_name()
s.set_rollno(rollno)
print(s.get_rollno())

        