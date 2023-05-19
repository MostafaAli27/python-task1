#this is a class 
import pandas as pd
import datetime
import csv  
from datetime import datetime
import glob

global file 

def add_contact(file):
    name=input("Enter Contact Name..")
    address = input("Enter Contact address..")
    phone = input("Enter Contact phone..")
    email = input("Enter Contact email..")
    time = datetime.now()
    if file:
        header = [name,address,phone,email,time]
        with open(file, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            f.close()

    else:
        current_date = time.strftime("%d%m%Y")
        with open(f'contactbook_{current_date}.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            f.close()


def delete_contact(file):
    if file:
        updatedlist=[]
        with open(file,newline="") as f:
            reader=csv.reader(f)
            username=input("Enter the username of the user you wish to remove or edit from file: ")         
            for row in reader:         
                 if row[0]!=username: 
                   updatedlist.append(row) 
            updatefile(updatedlist,file)
    else:
        print("sorry no file created in this date")


def updatefile(updatedlist,file):
    with open(file,"w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
    

def update_contact(file):
    show_contact(file)
    delete_contact(file)
    add_contact(file)

def show_contact(file) :
        with open(file, 'r') as file:
             csvreader = csv.reader(file)
             print("Name    : Address   : Phone     : Email     : Time    ")
             for row in csvreader:
                print(row[0] + "    "+row[1]+ "       "+row[2]+ "        "+row[3]+ "         "+row[4])

filenames = glob.glob("*.csv")

def check_file(num):
    return next((s for s in filenames if num in s), None)