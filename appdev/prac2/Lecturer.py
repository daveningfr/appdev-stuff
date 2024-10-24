from Person import person as p 

class lecturer(p):
    def __init__(self, name, nric,staff_id):
        super().__init__(name, nric)
        self.__staff_id = staff_id
    def compute_salary(self,total_teaching_hour):
        self.__salary = total_teaching_hour*90
    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id
    def get_staff_id(self):
        return self.__staff_id
    def __str__(self):
        return f'{self.get_name()}, Staff Id:{self.__staff_id} earns {self.__salary}'