import os

#-------------------------------#
#------------Classes------------#
#-------------------------------#

os.system('cls||clear')

class account:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '----------------\n' \
            + 'Name:\t\t' + self.name \
            + '\n' + 'Username:\t' + self.username \
            + '\n' + 'Password:\t' +  self.password \
            + '\n----------------'
      
#-------------------------------#
#-----------Functions-----------#
#-------------------------------#
            
def load():
    database = []
    
    try:
        file = open("database.csv", "r")
        
    except:
        pass
    
    else:
        db = file.read()
        db = db.split("\n")
        
        for row in db:
            acc = row.split(",")
            if len(acc) == 3:
                acc = account(acc[0], acc[1], acc[2])
                database.append(acc)
                
        file.close()
    
    return database
        
def print_menu():
    print(
"""
----------------
Password Manager
----------------
0: Exit
1: Add account
2: Remove account
3: Edit account
4: Print account
5: Print all accounts
"""
)
         
def add_account():
    print('Insert name: ')
    name = input('>> ')
    found = False
    
    for acc in database:
        if name.lower() == acc.name.lower():
            found = True
            break
        
    if not found:
        print('Insert username: ')
        username = input('>> ')
        print('Insert password: ')
        password = input('>> ')
        print(f'\n{name} account has been added successfully')
        acc = account(name, username, password)
        database.append(acc)
        
        db = ""
        
        for acc in database:
            db = db + acc.name + "," + acc.username + "," + acc.password + "\n"
        
        file = open("database.csv", "w")
        
        file.write(db)
        
        file.close()
        
    else:
        print(f'\n{name} already exist')

def remove_account():
    print('Insert account name: ')
    acc_name = input('>> ')
    found = False
    
    for acc in database:
        if acc_name.lower() == acc.name.lower():
            found = True
            database.remove(acc)
            break
        
    if not found:
        print(f'\nNo {acc_name} account has been found')
        
    else:
        print(f'\n{acc_name} account has been deleted successfully')
        
        db = ""
        
        for acc in database:
            db = db + acc.name + "," + acc.username + "," + acc.password + "\n"
        
        file = open("database.csv", "w")
        
        file.write(db)
        
        file.close()

def edit_account():
    print('Insert account name: ')
    acc_name = input('>> ')
    found = False
    
    for acc in database:
        if acc_name.lower() == acc.name.lower():
            found = True
            print('Edit username (leave blank to not edit): ')
            edited_username = input('>> ')
            print('Edit password (leave blank to not edit): ')
            edited_password = input('>> ')
            
            if edited_username != "":
                acc.username = edited_username
                
            if edited_password != "":
                acc.password = edited_password
                
            break
    
    if not found:
        print(f'\nNo {acc_name} account has been found')
        
    else:
        print(f'\n{acc_name} account has been edited successfully')
        
        db = ""
        
        for acc in database:
            db = db + acc.name + "," + acc.username + "," + acc.password + "\n"
        
        file = open("database.csv", "w")
        
        file.write(db)
        
        file.close()

def print_account():
    pass
    print('Insert account name: ')
    acc_name = input('>> ')
    found = False
    
    for acc in database:
        if acc_name.lower() == acc.name.lower():
            found = True
            print(acc)
            break
            
    if not found:
        print(f'\nNo {acc_name} account has been found')

def print_all():
    found = False
    if len(database) != 0:
        found = True
    
    for acc in database:
        print(acc)
        
    if not found:
        print('\nNo account has been found')

#-------------------------------#
#-------------Start-------------#
#-------------------------------#

database = load()

while True:
    print_menu()
    
    print('Insert number: ')
    i = input('>> ')
        
    if i == '0':
        os.system("cls||clear")
        print("Password-manager closed.\n")
        break
    
    elif i == '1':
        os.system('cls||clear')
        add_account()
    
    elif i == '2':
        os.system('cls||clear')
        remove_account()
        
    elif i == '3':
        os.system('cls||clear')
        edit_account()
    
    elif i == '4':
        os.system('cls||clear')
        print_account()
    
    elif i == '5':
        os.system('cls||clear')
        print_all()
    
    else:
        os.system('cls||clear')
        print('No action found for', i)
        