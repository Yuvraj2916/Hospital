
#HospMmodule.py (module)

def nephro():
    print('''  Please visit Dr. Anubhav Anand,
    Room No. 1.
    If needed, call 111-748-1910''')

def vet():
    print('''  Please visit Dr. Mihika Sharma,
    Room No. 2.
    If needed, call 111-787-1610''')

def cardio():
    print('''  Please visit Dr. Divyansh Mutreja,
    Room No. 3.
    If needed, call 111-831-6282''')

def gasint():
    print('''  Please visit Dr. Soumil Dubey,
    Room No. 4.
    If needed, call 111-227-3800''')

def neuro():
    print('''  Please visit Dr. Pawani Rawat,
    Room No. 5.
    If needed, call 111-266-4462''')

def ped():
    print('''  Please visit Dr. Somi Ali,
    Room No. 6.
    If needed, call 111-789-6326''')

def ortho():
    print('''  Please visit Dr. Ashu Sharma,
    Room No. 7.
    If needed, call 111-796-0567''')

def psych():
    print('''  Please visit Dr. Panshul Kayat,
    Room No. 8.
    If needed, call 111-829-3313''')

def ENT():
    print('''  Please visit Dr. Shloka Abhishek,
    Room No. 9.
    If needed, call 111-394-8222''')

def derm():
    print('''  Please visit Dr. Dhanishta Dhakate,
    Room No. 10.
    If needed, call 111-293-4772''')

def dent():
    print('''  Please visit Dr. Shashwat Koul,
    Room No. 11.
    If needed, call 111-830-9302''')

def therap():
    print('''  Please visit Dr. Arishta Jaiswal,
    Room No. 12.
    If needed, call 111-231-9312''')

def opth():
    print('''  Please visit Dr. Samrat Chakrabarti,
    Room No. 13.
    If needed, call 111-934-4924''')

def opt():
    name = input("Enter patient's name: ")
    print('''Please choose the specialist category required:
    01. Nephrologist
    02. Veterinarian
    03. Cardiologist
    04. Gastro-intestinal
    05. Neurologist
    06. Pedotrician
    07. Orthologist
    08. Psychiatrist
    09. ENT
    10. Dermatologist
    11. Dentist
    12. Therapist
    13. Opthalmologist''')
    
    cho=int(input("Enter a choice: "))
    print()
    if cho==1:
        print(">>Mr./Ms.",name.title(),",")
        nephro()
    elif cho==2:
        print(">>Mr./Ms.",name.title(),",")
        vet()
    elif cho==3:
        print(">>Mr./Ms.",name.title(),",")
        cardio()
    elif cho==4:
        print(">>Mr./Ms.",name.title(),",")
        gasint()
    elif cho==5:
        print(">>Mr./Ms.",name.title(),",")
        neuro()
    elif cho==6:
        print(">>Mr./Ms.",name.title(),",")
        ped()
    elif cho==7:
        print(">>Mr./Ms.",name.title(),",")
        ortho()
    elif cho==8:
        print(">>Mr./Ms.",name.title(),",")
        psych()
    elif cho==9:
        print(">>Mr./Ms.",name.title(),",")
        ENT()
    elif cho==10:
        print(">>Mr./Ms.",name.title(),",")
        derm()
    elif cho==11:
        print(">>Mr./Ms.",name.title(),",")
        dent()
    elif cho==12:
        print(">>Mr./Ms.",name.title(),",")
        therap()
    elif cho==13:
        print(">>Mr./Ms.",name.title(),",")
        opth()       
    else:
        print("Invalid choice.")



    
