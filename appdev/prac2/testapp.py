import Lecturer as l
import Student as s

lecname = input("Enter lecturer name: ")
lecnric = input("Enter lecturer nric: ")
lecstaffid = input("Enter lecturer staff id: ")
while lecnric != lecstaffid:
    print("Staff ID must be the same as NRIC")
    lecstaffid = input("Enter lecturer staff id: ")

        
lechours = int(input("Enter total teaching hours: "))
lec = l.lecturer(lecname, lecnric, lecstaffid)
lec.compute_salary(lechours)

sname = input("Enter student name: ")
snric = input("Enter student nric: ")
sadminno = input("Enter student admin no: ")
s = s.student(sname, snric, sadminno)
stestmark = int(input("Enter student test mark: "))
while stestmark <= 0 or stestmark >= 100:
    print("Test mark must be between 0 and 100")
    stestmark = int(input("Enter student test mark: "))
sexammark = int(input("Enter student exam mark: "))

while sexammark <= 0 or sexammark >= 100:
    print("Exam mark must be between 0 and 100")
    sexammark = int(input("Enter student exam mark: "))

s.set_test_mark(stestmark)
s.set_exam_mark(sexammark)
s.compute_final_mark()

print(lec)
print(s)