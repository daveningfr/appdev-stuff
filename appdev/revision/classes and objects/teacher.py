import person #import the person class from person.py

#create a teacher class which inherits from person
class teacher(person):
    def __init__(self, name, age, teacher_id):
        person.__init__(self, name, age) #this uses the person class to get the attributes which is called in teacher(person)
        self.__teacher_id = teacher_id

    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id
    
    def get_teacher_id(self):
        return self.__teacher_id
    
    def __str__(self):
        return f"name:{self.get_name()} age:{self.get_age()} teacher_id:{self.get_teacher_id()}"