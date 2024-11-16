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
    file = open("appdev/revision/q3/question.txt", "a")
    new_id = input("Enter the question id: ")
    new_description = input("Enter the question description: ")
    new_answer = input("Enter the question answer: ")

    newq = q()
    newq.set_id(new_id)
    newq.set_description(new_description)
    newq.set_answer(new_answer)
    file.write(f"{newq.get_id()},{newq.get_description()},{newq.get_answer()}\n")

    file.close()
    
    

def display():
    file = open("appdev/revision/q3/question.txt", "r")
    line = file.readline()
    try:
        ques = input("Enter the id of the question you want to display: ")
        while True:
            if line == "":
                print("Question not found")
                break
            elif line.split(',')[0] == ques:
                print("The question is: ", line.split(',')[1])
                print("The answer is: ", line.split(',')[2])
                break
            else:
                line = file.readline()
    except IOError:
        print("Question not found")

menu()
