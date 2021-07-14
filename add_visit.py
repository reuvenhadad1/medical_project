#312264781 Reuven Hadad
#313577595 Dan Monsonego
#203956321 Yahalomit Levi
import datetime
import PIL
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox

from Diagnostic_Suggestions import diagnostic_suggestions


def add_visit(patientid):
    root = Tk()
    root.geometry("730x800")
    root.title("Add Visit")

    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()
    e = IntVar()
    f = IntVar()
    g = IntVar()
    h = IntVar()
    v = IntVar()
    i = IntVar()
    j = IntVar()
    w = IntVar()


    icon = ImageTk.PhotoImage(PIL.Image.open("icon.jpeg"))
    root.iconphoto(True, icon)


    header = Label(root, text="insert patient test reasults:", font=("Times", 20, "italic"), fg="#0099ff").place(x=90, y=20)

    pic= ImageTk.PhotoImage(PIL.Image.open("medic.jpeg"))
    picLabel= Label(root, image=pic, height=239, width=200)
    picLabel.place(x=500, y=550)


    whiteBloodCellsLabel = Label(root, text="white blood cells:", font=("Ariel", 10, "underline"))
    whiteBloodCellsLabel.place(x=30, y=95)
    whiteBloodCells = Radiobutton(root, text="not tested", variable=a, value=0, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=120)
    whiteBloodCells = Radiobutton(root, text="lower", variable=a, value=1, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=145)
    whiteBloodCells = Radiobutton(root, text="4500-5500", variable=a, value=2, font=("Ariel", 10))
    whiteBloodCells.place(x=30,y=170)
    whiteBloodCells = Radiobutton(root, text="5500-6000", variable=a, value=3, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=195)
    whiteBloodCells = Radiobutton(root, text="6000-11000", variable=a, value=4, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=220)
    whiteBloodCells = Radiobutton(root, text="11000-15500", variable=a, value=5, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=245)
    whiteBloodCells = Radiobutton(root, text="15500-17500", variable=a, value=6, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=270)
    whiteBloodCells = Radiobutton(root, text="higher", variable=a, value=7, font=("Ariel", 10))
    whiteBloodCells.place(x=30, y=295)



    neutrophilLabel = Label(root, text="neutrophil:", font=("Ariel",10, "underline"))
    neutrophilLabel.place(x=200, y=95)
    neutrophil = Radiobutton(root, text="not tested", variable=b, value=0, font=("Ariel",10))
    neutrophil.place(x=200, y=120)
    neutrophil = Radiobutton(root, text="lower", variable=b, value=1, font=("Ariel",10))
    neutrophil.place(x=200, y=145)
    neutrophil = Radiobutton(root, text="28%-52%", variable=b, value=2, font=("Ariel",10))
    neutrophil.place(x=200, y=170)
    neutrophil = Radiobutton(root, text="higher", variable=b, value=3, font=("Ariel",10))
    neutrophil.place(x=200, y=195)

    lymphocytesLabel = Label(root, text="lymphocytes:", font=("Ariel",10, "underline"))
    lymphocytesLabel.place(x=30,y=350)
    lymphocytes = Radiobutton(root, text="not tested", variable=c, value=0, font=("Ariel", 10))
    lymphocytes.place(x=30, y=375)
    lymphocytes = Radiobutton(root, text="lower", variable=c, value=1, font=("Ariel", 10))
    lymphocytes.place(x=30, y=400)
    lymphocytes = Radiobutton(root, text="36%-52%", variable=c, value=2, font=("Ariel", 10))
    lymphocytes.place(x=30, y=425)
    lymphocytes = Radiobutton(root, text="higher", variable=c, value=3, font=("Ariel", 10))
    lymphocytes.place(x=30, y=450)

    redBloodCellsLabel = Label(root, text="red blood cells:", font=("Ariel",10, "underline"))
    redBloodCellsLabel.place(x=30, y=510)
    redBloodCells = Radiobutton(root, text="not tested", variable=d, value=0, font=("Ariel", 10))
    redBloodCells.place(x=30, y=535)
    redBloodCells = Radiobutton(root, text="lower", variable=d, value=1, font=("Ariel", 10))
    redBloodCells.place(x=30, y=560)
    redBloodCells = Radiobutton(root, text="4.5-6", variable=d, value=2, font=("Ariel", 10))
    redBloodCells.place(x=30, y=585)
    redBloodCells = Radiobutton(root, text="higher", variable=d, value=3, font=("Ariel", 10))
    redBloodCells.place(x=30, y=610)

    HTCLabel = Label(root, text="HTC:", font=("Ariel",10, "underline"))
    HTCLabel.place(x=200, y=260)
    HTC = Radiobutton(root, text="not tested", variable=e, value=0, font=("Ariel", 10))
    HTC.place(x=200, y=290)
    HTC = Radiobutton(root, text="lower", variable=e, value=1, font=("Ariel", 10))
    HTC.place(x=200, y=315)
    HTC = Radiobutton(root, text="33%-37%", variable=e, value=2, font=("Ariel", 10))
    HTC.place(x=200, y=340)
    HTC = Radiobutton(root, text="33%-48%", variable=e, value=3, font=("Ariel", 10))
    HTC.place(x=200, y=340)
    HTC = Radiobutton(root, text="48%-54%", variable=e, value=4, font=("Ariel", 10))
    HTC.place(x=200, y=365)
    HTC = Radiobutton(root, text="higher", variable=e, value=5, font=("Ariel", 10))
    HTC.place(x=200, y=390)

    ureanLabel = Label(root, text="urean:", font=("Ariel",10, "underline"))
    ureanLabel.place(x=360, y=530)
    urean = Radiobutton(root, text="not tested", variable=f, value=0, font=("Ariel", 10))
    urean.place(x=360, y=555)
    urean = Radiobutton(root, text="lower", variable=f, value=1, font=("Ariel", 10))
    urean.place(x=360, y=580)
    urean = Radiobutton(root, text="17-18.7", variable=f, value=2, font=("Ariel", 10))
    urean.place(x=360, y=605)
    urean = Radiobutton(root, text="17.7-43", variable=f, value=3, font=("Ariel", 10))
    urean.place(x=360, y=630)
    urean = Radiobutton(root, text="43-47.3", variable=f, value=4, font=("Ariel", 10))
    urean.place(x=360, y=655)
    urean = Radiobutton(root, text="higher", variable=f, value=5, font=("Ariel", 10))
    urean.place(x=360, y=680)

    hemoglobinLabel = Label(root, text="hemoglobin:", font=("Ariel",10, "underline"))
    hemoglobinLabel.place(x=360,y=95)
    hemoglobin = Radiobutton(root, text="not tested", variable=g, value=0, font=("Ariel", 10))
    hemoglobin.place(x=360, y=120)
    hemoglobin = Radiobutton(root, text="lower", variable=g, value=1, font=("Ariel", 10))
    hemoglobin.place(x=360, y=145)
    hemoglobin = Radiobutton(root, text="11.5-12", variable=g, value=2, font=("Ariel", 10))
    hemoglobin.place(x=360, y=170)
    hemoglobin = Radiobutton(root, text="15.5-16", variable=g, value=3, font=("Ariel", 10))
    hemoglobin.place(x=360, y=195)
    hemoglobin = Radiobutton(root, text="16-18", variable=g, value=4, font=("Ariel", 10))
    hemoglobin.place(x=360, y=220)
    hemoglobin = Radiobutton(root, text="higher", variable=g, value=5, font=("Ariel", 10))
    hemoglobin.place(x=360, y=245)


    creatinineLabel = Label(root, text="creatinine:", font=("Ariel",10, "underline"))
    creatinineLabel.place(x=360, y=300)
    creatinine = Radiobutton(root, text="not tested", variable=h, value=0, font=("Ariel",10))
    creatinine.place(x=360, y=325)
    creatinine = Radiobutton(root, text="lower", variable=h, value=1, font=("Ariel",10))
    creatinine.place(x=360, y=350)
    creatinine = Radiobutton(root, text="0.2-0.5", variable=h, value=2, font=("Ariel",10))
    creatinine.place(x=360, y=375)
    creatinine = Radiobutton(root, text="0.5-0.6", variable=h, value=3, font=("Ariel",10))
    creatinine.place(x=360, y=400)
    creatinine = Radiobutton(root, text="0.7-1", variable=h, value=4, font=("Ariel",10))
    creatinine.place(x=360, y=425)
    creatinine = Radiobutton(root, text="1-1.2", variable=h, value=5, font=("Ariel",10))
    creatinine.place(x=360, y=450)
    creatinine = Radiobutton(root, text="higher", variable=h, value=6, font=("Ariel",10))
    creatinine.place(x=360, y=475)


    ironLabel = Label(root, text="iron:", font=("Ariel",10, "underline"))
    ironLabel.place(x=200, y=445)
    iron = Radiobutton(root, text="not tested", variable=v, value=0, font=("Ariel",10))
    iron.place(x=200, y=470)
    iron = Radiobutton(root, text="lower", variable=v, value=1, font=("Ariel",10))
    iron.place(x=200, y=495)
    iron = Radiobutton(root, text="48-60", variable=v, value=2, font=("Ariel",10))
    iron.place(x=200, y=520)
    iron = Radiobutton(root, text="60-128", variable=v, value=3, font=("Ariel",10))
    iron.place(x=200, y=545)
    iron = Radiobutton(root, text="128-160", variable=v, value=4, font=("Ariel",10))
    iron.place(x=200, y=570)
    iron = Radiobutton(root, text="higher", variable=v, value=5, font=("Ariel",10))
    iron.place(x=200, y=595)

    HDLLabel = Label(root, text="high density lipoprotein:", font=("Ariel",10, "underline"))
    HDLLabel.place(x=510, y=95)
    HDL = Radiobutton(root, text="not tested", variable=i, value=0, font=("Ariel",10))
    HDL.place(x=510, y=120)
    HDL = Radiobutton(root, text="lower", variable=i, value=1, font=("Ariel",10))
    HDL.place(x=510, y=145)
    HDL = Radiobutton(root, text="29-34", variable=i, value=2, font=("Ariel",10))
    HDL.place(x=510, y=170)
    HDL = Radiobutton(root, text="34-62", variable=i, value=3, font=("Ariel",10))
    HDL.place(x=510, y=195)
    HDL = Radiobutton(root, text="62-82", variable=i, value=4, font=("Ariel",10))
    HDL.place(x=510, y=220)
    HDL = Radiobutton(root, text="higher", variable=i, value=5, font=("Ariel",10))
    HDL.place(x=510, y=245)

    alkalinePhosphataseLabel = Label(root, text="alkaline phosphatase:", font=("Ariel",10, "underline"))
    alkalinePhosphataseLabel.place(x=510, y=310)
    alkalinePhosphatase = Radiobutton(root, text="not tested", variable=j, value=0, font=("Ariel",10))
    alkalinePhosphatase.place(x=510, y=335)
    alkalinePhosphatase = Radiobutton(root, text="lower", variable=j, value=1, font=("Ariel",10))
    alkalinePhosphatase.place(x=510, y=370)
    alkalinePhosphatase = Radiobutton(root, text="30-60", variable=j, value=2, font=("Ariel",10))
    alkalinePhosphatase.place(x=510, y=395)
    alkalinePhosphatase = Radiobutton(root, text="60-90", variable=j, value=3, font=("Ariel",10))
    alkalinePhosphatase.place(x=510, y=420)
    alkalinePhosphatase = Radiobutton(root, text="90-120", variable=j, value=4, font=("Ariel",10))
    alkalinePhosphatase.place(x=510, y=445)
    alkalinePhosphatase = Radiobutton(root, text="higher", variable=j, value=5, font=("Ariel",10))
    alkalinePhosphatase.place(x=510, y=470)

    filename = patientid + ".txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    if ("female" in Lines[2]):
        pregnenetLabel = Label(root, text="is patient is pregnant?:", font=("Ariel",10, "underline"))
        pregnenetLabel.place(x=30, y=660)
        pregnant = Radiobutton(root, text="no", variable=w, value=0, font=("Ariel",10))
        pregnant.place(x=30, y=685)
        pregnant = Radiobutton(root, text="yes", variable=w, value=1, font=("Ariel",10))
        pregnant.place(x=30, y=710)
    file1.close()


    def try1():
        write(patientid)
        root.destroy()

    def write(patientid):

            if(a.get()!=0 or b.get()!=0 or c.get()!=0 or d.get()!=0 or e.get()!=0 or f.get()!=0 or g.get()!=0 or h.get()!=0 or i.get()!=0
            or j.get()!=0 or v.get()!=0):
                f1 = open(patientid + ".txt", "r")
                Lines = f1.readlines()
                f1.close()

                f1 = open(patientid + ".txt", "a")

                now = datetime.date.today()  # current date and time
                year = str(now.year)
                month = str(now.month)
                day = str(now.day)
                f1.write("Patient test results from date " + day + "." + month + "." + year + "\n")
                if (a.get()==1):
                    f1.write("white blood sells : is lower"  + "\n")
                elif(a.get()==0):
                    f1.write("white blood sells : not tested" + "\n")
                elif(a.get()==2):
                    f1.write("white blood sells : 4500-5550" + "\n")
                elif(a.get()==3):
                    f1.write("white blood sells : 5500-6000" + "\n")
                elif(a.get()==4):
                    f1.write("white blood sells : 6000-11000" + "\n")
                elif (a.get() == 5):
                    f1.write("white blood sells : 11000-15500" + "\n")
                elif (a.get() == 6):
                    f1.write("white blood sells : 15500-17500" + "\n")
                elif (a.get() == 7):
                    f1.write("white blood sells : higher than 175000" + "\n")

                if (b.get()==0):
                    f1.write("neutrophil: not tested" +"\n")
                elif (b.get()==1):
                    f1.write("neutrophil: lower" +"\n")
                elif (b.get()==2):
                    f1.write("neutrophil: 28%-54%" +"\n")
                elif (b.get() == 3):
                    f1.write("neutrophil:higher than 54%" + "\n")


                if (c.get()==0):
                    f1.write("lymphocytes : not tested" + "\n")
                elif (c.get()==1):
                    f1.write("lymphocytes : lower" + "\n")
                elif (c.get()==2):
                    f1.write("lymphocytes : 36%-52%" + "\n")
                elif (c.get()==3):
                    f1.write("lymphocytes : higher than 52%" + "\n")

                if (d.get()==0):
                    f1.write("red blood cells:  not tested  "+"\n")
                elif (d.get()==1):
                    f1.write("red blood cells:  lower  "+"\n")
                elif (d.get()==2):
                    f1.write("red blood cells:  4.5-6  "+"\n")
                elif (d.get()==3):
                    f1.write("red blood cells:  higher than 6  "+"\n")

                if (e.get()==0):
                    f1.write("HTC:  not tested  "+"\n")
                elif (e.get()==1):
                    f1.write("HTC: lower  "+"\n")
                elif (e.get()==2):
                    f1.write("HTC: 33%-37%  "+"\n")
                elif (e.get()==3):
                    f1.write("HTC: 37%-48%  "+"\n")
                elif (e.get()==4):
                    f1.write("HTC: 48%-54%  "+"\n")
                elif (e.get()==5):
                    f1.write("HTC: higher than 54% "+"\n")

                if (f.get()==0):
                    f1.write("urean: not tested  " +"\n")
                elif (f.get()==1):
                    f1.write("urean: lower  " + "\n")
                elif (f.get()==2):
                    f1.write("urean: 17-18.7  " + "\n")
                elif (f.get()==3):
                    f1.write("urean: 18.7-43  " + "\n")
                elif (f.get()==4):
                    f1.write("urean: 43-47.3  " + "\n")
                elif(f.get()==5):
                    f1.write("urean: higher than 43mg " + "\n")

                if (g.get() == 0):
                    f1.write("hemoglobin: not tested  " + "\n")
                elif(g.get()==1):
                    f1.write("hemoglobin: lower than 11.5 mg " + "\n")
                elif (g.get() == 2):
                    f1.write("hemoglobin: 11.5-12 mg " + "\n")
                elif (g.get() == 3):
                    f1.write("hemoglobin: 15.5-16 mg " + "\n")
                elif (g.get() == 4):
                    f1.write("hemoglobin: 16-18 mg " + "\n")
                elif (g.get() == 2):
                    f1.write("hemoglobin: higher 18mg " + "\n")

                if (h.get() == 0):
                    f1.write("creatinine: not tested  " + "\n")
                elif (h.get() == 1):
                    f1.write("creatinine: lower  " + "\n")
                elif (h.get() == 2):
                    f1.write("creatinine:0.2-0.5  " + "\n")
                elif (h.get() == 3):
                    f1.write("creatinine: 0.5-0.6  " + "\n")
                elif (h.get() == 4):
                    f1.write("creatinine: 0.7-1 " + "\n")
                elif (h.get() == 5):
                    f1.write("creatinine: 1-1.2 " + "\n")
                elif (h.get() == 4):
                    f1.write("creatinine: higher than 1.2" + "\n")


                if (v.get() == 0):
                    f1.write("iron: not tested  " + "\n")
                elif (v.get() == 1):
                    f1.write("iron: lower  " + "\n")
                elif (v.get() == 2):
                    f1.write("iron: 48-60 " + "\n")
                elif (v.get() == 3):
                    f1.write("iron: 61-128  " + "\n")
                elif (v.get() == 5):
                    f1.write("iron: 129-160  " + "\n")
                elif (v.get() == 6):
                    f1.write("iron: higher than 160 " + "\n")

                if(i.get() == 0):
                    f1.write("high density lipoprotein: not tested  " + "\n")
                elif (i.get() == 1):
                    f1.write("high density lipoprotein: lower  " + "\n")
                elif (i.get() == 2):
                    f1.write("high density lipoprotein: 29-34  " + "\n")
                elif (i.get() == 3):
                    f1.write("high density lipoprotein: 34-62  " + "\n")
                elif (i.get() == 4):
                    f1.write("high density lipoprotein: 62-82  " + "\n")
                elif (i.get() == 5):
                    f1.write("high density lipoprotein: higher than 82  " + "\n")

                if(j.get()==0):
                    f1.write("alkaline phosphatase:not tested"+"\n")
                elif(j.get()==1):
                    f1.write("alkaline phosphatase:  lower"+"\n")
                elif (j.get() == 2):
                    f1.write("alkaline phosphatase: 30-60 " + "\n")
                elif (j.get() == 3):
                    f1.write("alkaline phosphatase: 60-90" + "\n")
                elif (j.get() == 4):
                    f1.write("alkaline phosphatase:  90-120  " + "\n")
                elif (j.get() == 5):
                    f1.write("alkaline phosphatase:higher than 120" + "\n")

                if("female" in Lines[3]):
                    if (w.get()==0):
                        f1.write("pregnancy: no " + "\n")
                    elif (w.get()==1):
                        f1.write("pregnancy: yes " + "\n")
                else:
                    f1.write("")

                f1.close()
                diagnostic_suggestions(patientid)
            else:
                messagebox.showinfo(title="all fields are empty", message="No test reasult were insert")

    #   diagnostic_suggestions(whiteBloodCells, neutrophil, lymphocytes, redBloodCells, HDL, HTC, urean, hemoglobin, creatinine, alkalinephosphatase)

    submit = Button(root, text="submit", padx=180, pady=1, fg="#0099ff", font=("Ariel", 14), command=try1)
    submit.place(x=30, y=750)

    root.mainloop()



#add_visit("123123")