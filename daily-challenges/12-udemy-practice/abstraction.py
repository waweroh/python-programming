'''
Abstraction - means hiding away information and giving away what is necessary
          student1.mark_list() - this is an example of abstraction in the code
                                  ie the mark_list method is under the hood we just
                                  implement it just like built-in functions
'''
class Student:
  def __init__(self, index, marks):
    self.index = index
    self.marks = marks

  def subjects(self): 
    print('did all 6 subjects')

  def mark_list(self):
    print(f'My index is {self.index} and I have {self.marks}marks')

student1 = Student(1, 450)
student1.mark_list()
print (student1.mark_list())