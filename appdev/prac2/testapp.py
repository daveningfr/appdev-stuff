import Lecturer as l
import Student as s

lecname = input("Enter lecturer name: ")
lecnric = input("Enter lecturer nric: ")
lecstaffid = input("Enter lecturer staff id: ")
lechours = int(input("Enter total teaching hours: "))
lec = l.lecturer(lecname, lecnric, lecstaffid)
lec.compute_salary(lechours)

sname = input("Enter student name: ")
snric = input("Enter student nric: ")
sadminno = input("Enter student admin no: ")
s = s.student(sname, snric, sadminno)
stestmark = int(input("Enter student test mark: "))
sexammark = int(input("Enter student exam mark: "))
s.set_test_mark(stestmark)
s.set_exam_mark(sexammark)
s.compute_final_mark()

print(lec)
print(s)