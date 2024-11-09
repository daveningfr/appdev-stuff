# create a class person with name and age
class person:
    def __init__(self, name,age): #this inintializes the class with name and age
        self.__name = name
        self.__age = age

    def set_name(self, name): 
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    




