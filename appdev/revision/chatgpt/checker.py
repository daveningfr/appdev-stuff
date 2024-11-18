from idk import isAlpha
import shelve

def menu():
    while True:
        try:
            print('1.alpha checker \n2.add an alpha \n3.delete an alpha\n4.edit an alpha \n5.End')
            check = int(input('Choose one my alpha'))

            if check == 1:
                checker()
            elif check == 2:
                add()
            elif check == 3:
                delete()
            else:
                print('ok bye')
                break
        except ValueError:
            print('dawg enter a number u retard')



def add():
    newalpha = input('what is the name')
    newage = input('what is the age')
    newgen = input('gender(m or f)')

    sigma = isAlpha()
    if newgen == 'm' or 'f':
        sigma.set_alpha()
    
    

    

def edit():
    pass
def delete():
    pass

def checker():
    pass



try:
    db = shelve.open('appdev/revision/chatgpt/alpha')
except IOError:
    print('something broke idk what goodluck lil bro')
else:
    menu()
    db.close()