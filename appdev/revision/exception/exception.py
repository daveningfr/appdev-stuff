try:
    error = input('what error you want to raise? choose from value, zero, io or unknown: ')
    if error == 'value':
        sigma = int('fein')
    elif error == 'zero':
        dweah = 1/0
    elif error == 'io':
        file = open('file.txt')
    else:
        s
except ValueError:
    print("Invalid input(value error)")
except ZeroDivisionError:
    print("You can't divide by zero")
except IOError:
    print("this is an IO error")
except:
    print("An error occurred")
else:
    print("this will run if there are no exceptions")
finally:
    print('this will always run')