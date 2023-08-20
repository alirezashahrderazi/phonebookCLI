import os

menu="""
=========================
|1-Add user             |
|2-Serch Phone          |                  
|3-Delete Phone         |
|4-Show All Number      |
|0-Exit                 |
=========================
"""
clear=lambda: os.system("cls")


# Define the login credentials
username = "admin"
password = "admin"

# Check if the user is authenticated
def authenticate():
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    return entered_username == username and entered_password == password


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH=os.path.join(BASE_DIR,"database.txt")
def validation():
    if not os.path.exists(PATH):
        f=open(PATH,"w+")
        f.close()
       


def menus():
    print(menu)
    

def add(name,number):
    validation()
    f=open(PATH,"a+")
    new_phone=name+':'+number+'\n'
    f.write(new_phone)
    

def search(name):
    validation()
    f=open(PATH,"r")
    for line in f.readlines():
         if name==line.split(':')[0]:
             print(name +":"+line.split(':')[1])
    f.close()


def delete(name):
    validation()

    f=open(PATH,"r")
    new_database=''
    for line in f.readlines():
         if not name == line.split(':')[0]:
             new_database += line
    f.close()
    f=open(PATH,"w")
    f.write(new_database)   
    f.close() 

def show_all():
    f=open(PATH,"r")
    database=''
    database=f.read()
    f.close()
    print(database)
    

select=10
authenticated = False
while select !=0:
    if not authenticated:
        authenticated = authenticate()

    if authenticated:
        menus()
        select=int(input('Enter Your Choice:'))
        clear() 
        if select==1:
            name=input('Enter Name:')
            number=input('Enter Number:')
            add(name,number)
        elif select==2:
            name=input('Enter Name:')
            search(name)
        elif select==3:
            name=input('Enter Name:')
            delete(name)
        elif select==4:
            show_all()