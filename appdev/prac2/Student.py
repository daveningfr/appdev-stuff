from Person import person as p

class student(p):
    def __init__(self, name, nric,admin_no):
        p.__init__(self,name, nric)

        self.__admin_no = admin_no
        self.__test_mark = 0
        self.__exam_mark = 0
    
    
    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no
    def get_admin_no(self):
        return self.__admin_no
    def set_test_mark(self, test_mark):
        self.__test_mark = test_mark
    def get_test_mark(self):
        return self.__test_mark
    def set_exam_mark(self, exam_mark):
        self.__exam_mark = exam_mark
    def get_exam_mark(self):
        return self.__exam_mark
    
    def compute_final_mark(self):
        self.__final_mark =  (self.__test_mark + self.__exam_mark)/2
    def __str__(self):
        return f'{self.__name}, Admin no:{self.__admin_no} final mark is {self.__final_mark} '