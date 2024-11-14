import shelve
from question import Question as q 

def menu():
    while True:
        print("Select the program (1-3) to run: ")
        print("1. Add a Question")
        print("2. Display a Question (by id)")
        print("3. Quit the program")

        try:
            val = int(input("Enter your command (1-3): "))
        except ValueError:
            val = 3

        if val == 1:
            add()
        elif val == 2:
            display()
        else:
            print("End of program")
            break

def add():
    new_id = input("Enter the question id: ")
    new_description = input("Enter the question description: ")
    new_answer = input("Enter the question answer: ")

    newq = q()
    newq.set_id(new_id)
    newq.set_description(new_description)
    newq.set_answer(new_answer)

    db[newq.get_id()] = newq
    

def display():
    id = input("Enter the id of the question you want to display: ")
    try:
        print("The question is: ", db[id].get_description())
        print("The answer is: ", db[id].get_answer())
    except:
        print("Question not found")

try:
    db = shelve.open("appdev/revision/q3/question")
except IOError:
    print("Error: File not found")
else:
    menu()
    db.close()
