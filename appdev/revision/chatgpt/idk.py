class person:
    def __init__(self,name,age,gender):
        self.__name = name
        self/__age = age
        self.__gender = gender
    
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set__age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    
    def set_gender(self,gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender


class isAlpha(person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.__alpha = False

    def get_alpha(self):
        return self.__alpha
    def set_alpha(self):
        self.__alpha = not self.__alpha

    def __str__(self):
        if self.__alpha:
            return f'{self.__name} is an alpha'
        else:
            return f'{self.__name} is NOT an alpha'


