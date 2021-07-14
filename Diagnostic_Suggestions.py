#312264781 Reuven Hadad
#313577595 Dan Monsonego
#203956321 Yahalomit Levi

from datetime import *
import PIL
from PIL import ImageTk, Image
import datetime
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from add_patient import *


def frame(args):
    pass


def scroll_bar(args):
    pass


def diagnostic_suggestions(patientid):


    diseaseDic = {"anemia" : 0, "diet" : 0, "bleeding" : 0, "hyperlipidemia" : 0, "blood production disorder": 0, "hematologic disorder": 0,
                   "iron poisoning":0, "dehydration": 0, "infection": 0,"lack of vitamins": 0, "viral disease": 0, "bile duct disease":0,
                   "heart disease": 0, "blood disease": 0, "liver disease": 0, "kidney disease": 0, "lack of iron": 0, "muscles disease":0,
                   "smokers": 0, "lunges disease": 0,"Hypothyroidism": 0, "diabetes": 0, "cancer":0, "meat overloading": 0, "medicine use": 0,
                   "Malnutrition": 0, "Immune system failure":0, "Lymphoma":0}

    careDic = {"anemia" : "2 10 mg pill of B12 per day", "diet" : "set a meeting with a nutritionist", "bleeding" : "To be rushed to the hospital",
               "hyperlipidemia" : "Schedule an appointment with a nutritionist a 5 mg pill of Simobil daily for a week",
               "blood production disorder": "10 mg pill of B12 per day for one month,\n and 5 mg pill of folic acid per day for one month",
               "hematologic disorder": "An injection of a hormone to encourage red blood cell production",
               "iron poisoning":"To be evacuated to the hospital", "dehydration": "Complete rest when lying down, returning fluids to drinking",
               "infection": "antibiotics" ," lack of vitamins": "Referral for a blood test to identify the missing vitamins",
               "viral disease": "Rest at home", "bile duct disease":"Referral to surgical treatment",
               "heart disease": "Schedule an appointment with a nutritionist", "blood disease": "A combination of cyclophosphamide and corticosteroids",
               "liver disease": "Referral to a specific diagnosis for the purpose of determining treatment", "kidney disease": "Balancing blood sugar levels",
               "lack of iron": "Two 10 mg pills of B12 a day for a month", "muscles disease":"Two 5 mg pills of Altman C3 turmeric a day for a month",
               "smokers": "Quit smoking", "lunges disease": "Quit smoking, or referral for a lung scan",
               "Hypothyroidism": "propylthiouracil to reduce thyroid activity", "diabetes": "Insulin adjustment for the patient",
               "cancer": "Antarctinib", "meat overloading": "Schedule an appointment with a nutritionist",
               "medicine use": "Referral to a family doctor for the purpose of checking compatibility between medications",
                "Malnutrition": "Schedule an appointment with a nutritionist", "Immune system failure": "rushed to the hospital", "Lymphoma": "Antarctinib"}

    Lines = []
    filename = patientid + ".txt"
    # Using readlines()
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    length = len(Lines)
    birthdayLength = len(Lines[3])
    print(birthdayLength)

    yearOfBirth = Lines[3][birthdayLength-3]+Lines[3][birthdayLength-2]
    print(yearOfBirth)
    if(int(yearOfBirth)>22):
        yearOfBirth = "19" + yearOfBirth
    else:
        yearOfBirth = "20" + yearOfBirth

    yearOfBirth = int(yearOfBirth)
    today = (datetime.today())
    thisYear= today.year
    print(yearOfBirth)

    #white blood cells reasult
    print(Lines[length-12])
    if(not "not tested" in Lines[length-12]):
        if(thisYear-int(yearOfBirth)>=18):
            if("11001-15500" in Lines[length-12] or "15501-17500" in Lines[length-12] or "higher" in Lines[length-12]):
                diseaseDic["infection"]+=1
                diseaseDic["blood disease"]+=0.25
                diseaseDic["cancer"]+=0.25
            elif("lower" in Lines[3]):
                diseaseDic["viral disease"]+=1
                diseaseDic["cancer"]+=0.25
                diseaseDic["Immune system failure"]+=1
        elif(thisYear-yearOfBirth<=17 and thisYear-yearOfBirth>=4):
            if("15501-17500" in Lines[length-12] or "higher" in Lines[length-12]):
                diseaseDic["infection"]+=1
                diseaseDic["blood disease"]+=0.25
                diseaseDic["cancer"]+=0.25
            elif("lower" in Lines[length-12] or "4500-5500" in Lines[length-12]):
                diseaseDic["viral disease"]+=1
                diseaseDic["cancer"]+=0.25
                diseaseDic["Immune system failure"]+=1
        elif(thisYear-yearOfBirth<=3):
            if("higher" in Lines[length-12]):
                diseaseDic["infection"]+=1
                diseaseDic["blood disease"]+=0.25
                diseaseDic["cancer"]+=0.25
            elif("lower" in Lines[length-12] or "4500-5500" in Lines[length-12] or "5501-6000" in Lines[length-12]):
                diseaseDic["viral disease"]+=1
                diseaseDic["cancer"]+=0.25
                diseaseDic["Immune system failure"]+=1


    #Neutrophil result
    if(not "not tested" in Lines[length-11]):
        if("lower" in Lines[length-11]):
            diseaseDic["blood production disorder"]+=1
            diseaseDic["infection"]+=0.5
            diseaseDic["cancer"]+=0.25
        elif("higher" in Lines[length-11]):
            diseaseDic["viral disease"]+=1


    #Lymphocytes
    if(not "not tested" in Lines[length-10]):
        if("lower" in Lines[length-10]):
            diseaseDic["blood production disorder"]+=1
        elif("higher" in Lines[length-10]):
            diseaseDic["viral disease"]+=1
            diseaseDic["infection"]+=1
            diseaseDic["Lymphoma"]+=1


    #red blood cells
    if(not "not tested" in Lines[length-9]):
        if("lower" in Lines[length-9]):
            diseaseDic["anemia"]+=1
            diseaseDic["bleeding"]+=1
        elif("higher" in Lines[length-9]):
            diseaseDic["blood production disorder"]+=1
            diseaseDic["smokers"]+=1
            diseaseDic["lunges disease"]+=1


    #HTC
    if(not "not tested" in Lines[length-8]):
        if("male" in Lines[2]):
            if("lower" in Lines[length-8]):
                diseaseDic["bleeding"]+=1
                diseaseDic["anemia"]+=1
            elif("higher" in Lines[length-8]):
                diseaseDic["smokers"]+=1
        else:
            if("lower" in Lines[length-8]):
                diseaseDic["bleeding"]+=1
                diseaseDic["anemia"]+=1
            elif("higher" in Lines[length-8]):
                diseaseDic["smokers"]+=1


    #urean
    if(not "not tested" in Lines[length-7]):
        if("south africans" in Lines[4] and "not" in Lines[length-1]):
            if("17-18.7" in Lines[length-7] or "lower" in Lines[length-7]):
                diseaseDic["diet"]+=1
                diseaseDic["liver disease"]+=1
            elif("higher" in Lines[length-7]):
                diseaseDic["meat overloading"]+=1
                diseaseDic["diet"]+=1
                diseaseDic["dehydration"]+=1
        else:
            if("lower" in Lines[length-7]):
                diseaseDic["diet"]+=1
                diseaseDic["liver disease"]+=1
            elif("43-47.3" in Lines[length-7] or "higher" in Lines[length-7]):
                diseaseDic["meat overloading"]+=1
                diseaseDic["diet"]+=1
                diseaseDic["dehydration"]+=1


    #hemoglobin
    if(not "not tested" in Lines[length-6]):
        if("male" in Lines[32]):
            if("lower" in Lines[length-6] or "11.5-12" in Lines[length-6]):
                diseaseDic["lack of iron"]+=1
                diseaseDic["bleeding"]+=1
                diseaseDic["hematologic disorder"]+=1
        elif("female" in Lines[2]):
            if("lower" in Lines[length-6] or "11.5-12" in Lines[length-6]):
                diseaseDic["lack of iron"]+=1
                diseaseDic["bleeding"]+=1
                diseaseDic["hematologic disorder"]+=1
        elif((thisYear-yearOfBirth)<18):
            if("lower" in Lines[length-6]):
                diseaseDic["lack of iron"]+=1
                diseaseDic["bleeding"]+=1
                diseaseDic["hematologic disorder"]+=1


    #creatinin
    if(not "not tested" in Lines[length-5]):
        if((thisYear-yearOfBirth)<3):
            if("lower" in Lines[length-5]):
                diseaseDic["muscles disease"]+=1
                diseaseDic["Malnutrition"]+=1
                diseaseDic["diet"]+=1
            elif("0.5-0.6" in Lines[length-5] or "0.6-1" in Lines[length-5] or "1-1.2" in Lines[length-5] or
                 "higher" in Lines[length-5]):
                diseaseDic["kidney disease"]+=1
                diseaseDic["muscles disease"]+=0.5
                diseaseDic["meat overloading"]+=0.5
        elif (thisYear-yearOfBirth>=3 and thisYear-yearOfBirth <=17):
            if("lower" in Lines[length-5] or "0.2-0.5"):
                diseaseDic["muscles disease"]+=1
                diseaseDic["Malnutrition"]+=1
                diseaseDic["diet"]+=1
            elif( "1-1.2" in Lines[length-5] or "higher" in Lines[length-5]):
                diseaseDic["kidney disease"]+=1
                diseaseDic["muscles disease"]+=0.5
                diseaseDic["meat overloading"]+=0.5
        elif (thisYear-yearOfBirth>=18 and thisYear-yearOfBirth<=59):
            if("lower" in Lines[length-5]  or "0.2-0.5" in Lines[length-5] or "0.5-0.6" in Lines[length-5]):
                diseaseDic["muscles disease"]+=1
                diseaseDic["Malnutrition"]+=1
                diseaseDic["diet"]+=1
            elif( "1-1.2" in Lines[length-5] or "higher" in Lines[length-5]):
                diseaseDic["kidney disease"]+=1
                diseaseDic["muscles disease"]+=0.5
                diseaseDic["meat overloading"]+=0.5
        elif (thisYear-yearOfBirth>=60):
            if("lower" in Lines[length-5] or  "0.5-0.6" in Lines[length-5]):
                diseaseDic["muscles disease"]+=1
                diseaseDic["Malnutrition"]+=1
                diseaseDic["diet"]+=1
            elif("higher" in Lines[length-5]):
                diseaseDic["kidney disease"]+=1
                diseaseDic["muscles disease"]+=0.5
                diseaseDic["meat overloading"]+=0.5



    #iron
    if("female" in Lines[2]):
        if("lower" in Lines[length-4]):
            diseaseDic["diet"]+=1
            diseaseDic["bleeding"]+=1
        elif("128-160" in Lines[length-4] or "higher" in Lines[length-4]):
            diseaseDic["iron poisoning"]+=1
    elif("male" in Lines[2]):
        if("lower" in Lines[length-4] or "48-60" in Lines[length-4]):
            diseaseDic["diet"]+=1
            diseaseDic["bleeding"]+=1
        elif("higher" in Lines[length-4]):
            diseaseDic["iron poisoning"]+=1



    #DHL
    if("female" in Lines[2]):
        if("lower" in Lines[length-3]):
            diseaseDic["heart disease"]+=1
            diseaseDic["hyperlipidemia"]+=1
    elif("male" in Lines[2]):
        if("lower" in Lines[length-3] or "48-60" in Lines[length-3]):
            diseaseDic["heart disease"]+=1
            diseaseDic["hyperlipidemia"]+=1




    #alkaline Phosphatase
    if("sout africans" in Lines[length-2]):
        if("lower" in Lines[length-2] or "30-60" in Lines[length-2]):
            diseaseDic["diet"]+=1
            diseaseDic["lack of vaitamins"]+=1
        elif("higher" in Lines[length-2]):
            diseaseDic["liver disease"]+=1
            diseaseDic["Hypothyroidism"]+=1
    else:
        if("lower" in Lines[length-2] ):
            diseaseDic["diet"]+=1
            diseaseDic["lack of vitamins"]+=1
        elif("higher" in Lines[length-2] or "90-120" in Lines[length-2]):
            diseaseDic["liver disease"]+=1
            diseaseDic["Hypothyroidism"]+=1



    newDic = sorted(diseaseDic.items())
    print("the diseases with most probability are:")



    root = Tk()
    root.geometry("500x600")
    root.title("Medical Aid")
    pic = ImageTk.PhotoImage(PIL.Image.open("medic.jpeg"))

    treat = []
    for key in diseaseDic.keys():
        if(not diseaseDic[key]==0):
            line1 = str(key) + " ,Recommended treatment:\n"
            line2 = str(careDic[key]) +"\n"
            line3 = ""
            treat.append(line1)
            treat.append(line2)
            treat.append(line3)

    label2 = Label(root, text="patient diagnose", font=("Times", 20,"bold", "underline"), fg="#0099ff")
    label2.place(x=45, y=20)

    frame = Frame(root, width=600, height=450)
    frame.place(x=45, y=100)
    scroll_bar = Scrollbar(frame)
    scroll_bar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(frame, yscrollcommand=scroll_bar.set)
    mylist.config(width=65, height=25)
    for line in treat: mylist.insert(END, str(line))
    mylist.pack(fill=BOTH)
    scroll_bar.config(command=mylist.yview)
    print(patientid)

    f = open(patientid + ".txt", "a")
    f.write("the patient diagnose result from the date " + str(today) + "\n")
    for line in treat:
        print(line)
        f.write(line)
    f.close()



#diagnostic_suggestions("3122")