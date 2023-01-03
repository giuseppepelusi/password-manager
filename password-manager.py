import os 

#-------------------------------#
#---------Initialization--------#
#-------------------------------#

file = open("database.csv", "w")

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
        
        file.write(database)

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
    for acc in database:
        print(acc)

#-------------------------------#
#-------------Start-------------#
#-------------------------------#
    
database = []

while True:
    print_menu()
    
    print('Insert number: ')
    i = input('>> ')
        
    if i == '0':
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
        