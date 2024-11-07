try:
    file = 'appdev/exception/BMI.txt'
    while True:
        name = input('Enter name: ')
        weight = float(input('Enter weight (kg): '))
        height = float(input('Enter height(m): '))

        bmi = weight/height**2
        print(bmi)

        command = input('Store your bmi to file? (Y/N): ')
        if command.upper() == 'Y':
            bmi_File = open(file, 'a')
            bmi_File.write(name+','+ str(bmi) +'\n')
            bmi_File.close()
        
        command = input('Do you want to continue? (Y/N): ')
        if command.upper() == 'N':
            break

    command = input('Do you want view BMI record in file? (Y/N): ')
    if command.upper() == 'Y':
        bmi_File = open(file, 'r')
        contents = bmi_File.read()
        print(contents)
        bmi_File.close()
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Cannot divide by zero')
except IOError:
    print('Error in file operation')
except:
    print('Unknown error')