class Question:
    def __init__(self):
        self.__id = None
        self.__description = None
        self.__answer = None

    def get_id(self):
        return self.__id
    def get_description(self):
        return self.__description
    def get_answer(self):
        return self.__answer
    

    def set_id(self,id):
        self.__id = id
    def set_description(self,description):
        self.__description = description
    def set_answer(self,answer):
        self.__answer = answer
    