import Lecturer as l
import Student as s

lecname = input("Enter lecturer name: ")
lecnric = input("Enter lecturer nric: ")
lecstaffid = input("Enter lecturer staff id: ")
lechours = int(input("Enter total teaching hours: "))
lec = l.lecturer(lecname, lecnric, lecstaffid)
lec.compute_salary(lechours)
print(lec)
