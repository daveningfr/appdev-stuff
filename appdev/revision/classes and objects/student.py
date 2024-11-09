import person #import the person class from person.py

#create a student class which inherits from person
class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)  #this uses the super function to get parrent attributes(in this case person)
        self.__student_id = student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def get_student_id(self):
        return self.__student_id
    
    def __str__(self): 
        return f"name:{self.get_name()} age:{self.get_age()} student_id:{self.get_student_id()}" #this will return the string when the object is called
    

sigma = student("sigma", 20, 1234)#create a student object with name sigma
sigma.set_name(input("Enter new name: "))#set the name of the student object of sigma using the input function
print(sigma)#this prints the student object sigma which uses the __str__ method to print the object