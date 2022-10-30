class Student:
 def __init__(self, name, subjects=None):
     self.set_name(name)
     if not isinstance(subjects, list):
         raise TypeError("subjects must be a list")
     self.subjects = subjects

 def set_name(self, name):
     if not isinstance(name, str):
         raise TypeError("name must be a string")
     self._name = name

 def get_name(self):
     return self._name

 name=property(fget = get_name, fset = set_name, doc = 'nombre del alumno')
