#HospMmain.py (main program)

from HospMmodule import *
import random
import csv

p_name = "Enter patient's name: "                                      
p_ID = "Enter patient's ID: "
p_room = "Enter room type[Private/Semi-private/Public]: "
count = 0   #keeping count zero when no patients are admitted 


#below are 4 user defined functions to be carried out in the hospital menu : 
def admit_pat():
    rows = []
    n=int(input("Enter the number of patients: "))
    for i in range(n):
        name=input(p_name)
        contact=int(input("Enter contact number: "))
        room=input(p_room)
        days=int(input("Enter the number of days to be admitted for: "))
        #creating patient ID using random function:
        ID=random.randint(1111,9999)  
        print(">>>","Patient ",name,"is admitted in",room,"room,")
        print("with ID",ID,"for",days,"days.")
        print()
        row = [name,ID,room,days,contact]
        rows.append(row)

    #storing patient data in file 'Patient.csv':        
    with open("Patient_data.csv",'a',newline='') as f:
        csv_w = csv.writer(f)
        for i in rows:
            csv_w.writerow(i)

def view_list():
    f = open("Patient_data.csv",'r')
    csv_r = csv.reader(f)
    print("\nNAME  :  ID  :  ROOM TYPE  :  DAYS ADMITTED  :  CONTACT NO.")
    for row in csv_r:
        print(row[0]," : ",row[1]," : ",row[2]," : ",row[3]," : ",row[4])

def discharge_pat():
    c=0
    #taking data to discharge patient:
    x=input("Enter the name of patient to be discharged: ")
    y = input(p_ID)
    print()
    f = open("Patient_data.csv",'r')
    csv_r = csv.reader(f)
    for row in csv_r:
        #veryfing if a patient with the above data exists:
        if row[0]==x and row[1]==y :
            print("\n>>> Patient",x,", ID",y,"will be disharged within 24 hours.")
            print()
            c=1
            
        else:
            continue
    if c==0:
        print("No match for the patient is found.")
    f.close()

def view_bill():
    c1=0
    #collecting data to create bill:
    name=input("\nEnter patient's name to view their bill: ")

    f = open("Patient_data.csv",'r')
    csv_r = csv.reader(f)
    room = input(p_room)
    for row in csv_r:
        #veryfing if a patient with the above data exists:
        if row[0]==name and  row[2]==room:
            pat_name = row[0]
            pat_ID = row[1]
            pat_room = row[2]
            pat_days = int(row[3])
            c1=1
        else:
            continue

    if c1==1:
        #setting up fees according to the room type:
        fee = 1
        if room == "Private":
            fee = fee*pat_days*1000
        elif room == "Semi-private":
            fee = fee*pat_days*520
        elif room == "Public":
            fee = fee*pat_days*300
        print("\nPatient's Bill :-")
        print("NAME :", "\t" , pat_name.title())
        print("ID :", "\t" , pat_ID)
        print("ROOM TYPE :", "\t" , pat_room.title())
        print("DAYS ADMITTED FOR : ", pat_days)
        print("BILLING FEE :", "\t" , fee , "INR.")
        print()
        
    else:
        print("No match for the patient is found.")
    f.close()

    
while True:
    print()
    print('''
_________________________________________________________________________________

                           ~  WELCOME TO MYHOSPITAL! ~  
_________________________________________________________________________________

---------------------------------------------------------------------------------
                                   MAIN MENU  
---------------------------------------------------------------------------------       
    1. Patient menu.
    2. Appoint a doctor.
    3. Exit.
''')
    ch=int(input("Enter choice: "))

    #ch[1]:
    if ch == 1:
        print('''
    Welcome to 'Patient Menu':
                                1. Admit a patient
                                2. View list of the admitted patients
                                3. Discharge a patient
                                4. View a patient's bill.
''')
        choice=int(input("Enter choice: "))
        
        #choice[1], (to admit patient):
        if choice == 1:
            admit_pat()
            #changing count to 1 when a patient has been admitted:
            count = 1

        #choice[2], (to view list of patients):
        elif choice == 2:
            if count==0:
                print("No patients admitted yet.")
            else:
                view_list()

        #choice[3] ,(to discharge patient):
        elif choice == 3:
            if count==0:
                print("No patients admitted yet.")
            else:
                discharge_pat()

        #choice[4], (to view bill):
        elif choice == 4:
            if count==0:
                print("No patients admitted yet.")
            else:
                view_bill()

        else:   #for wrong 'patient menu' choice
            print("Invalid choice, Please retry.")
            continue
        

    #ch[2], (to appoint a doctor):
    elif ch == 2:
        #calling the required function from the module 'HospMmodule':
        opt()
    

    #ch[3], (to exit):
    elif ch==3:
        print("\n>>> Thankyou for your visit!")
        print("Program terminated.")    #terminating the program
        break

    else:   #for wrong 'main menu' choice
        print("Invalid choice, please retry.")
        continue










    
