class Student:
    def __init__(self, name):
        self.name = name
        self.math = 0
        self.chinese = 0
        self.english = 0
        self.science = 0
        self.choices = ['SchoolA','SchoolB','SchholC']

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4


def main():
    students = load_result()
    for s in students:
        print(s.name, s.get_score())


def load_result():
    students = []
    # implement the load result logic here
    try:
        file = open("appdev/persistence/results.txt", "r")
        for result in file:
            list = result.split(',')
            s = Student(list[0])
            s.math = float(list[1])
            s.chinese = float(list[2])
            s.english = float(list[3])
            s.science = float(list[4])
            students.append(s)
    except IOError:
        print('file not found')
    finally:
        file.close()
    
    return students

# start the test program
main()
