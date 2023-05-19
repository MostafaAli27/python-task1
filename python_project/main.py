import class_file
import datetime 
import pandas as pd
from datetime import datetime

day = input("please enter the date you want to show in form yyyy-mm-dd ex: 2023-05-15... ")
check = datetime.strptime(day, '%Y-%m-%d')
file = class_file.check_file(check.strftime("%d%m%Y"))
if file:
    while True :
        print("Welcome to Contact book system ")
        print("choose your process..")
        print("1 ) for adding a new Contact")
        print("2 ) for deleteing an exicting contact")
        print("3 ) for updating an exicting contact")
        print("4 ) for viewing list of contacts of specific day")
        print("5 ) for saving and closing the program")
        choice = input()
        if choice == "1":
            class_file.add_contact(file)
        elif choice == "2":
            class_file.delete_contact(file)
        elif choice == "3" :
            class_file.update_contact(file)
        elif choice == "4":
            class_file.show_contact(file)
        else :
            print("Thanke you.")
            break
else:
        print("sorry no file created in this date")
