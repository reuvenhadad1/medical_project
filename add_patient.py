#312264781 Reuven Hadad
#313577595 Dan Monsonego
#203956321 Yahalomit Levi
import PIL
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime

lastname=""
id=""
gender=""

def add_patient():

    root = Tk()
    root.geometry("600x650")
    root.title("Add Patient")

    icon = ImageTk.PhotoImage(PIL.Image.open("icon.jpeg"))
    root.iconphoto(True, icon)
    x = IntVar()
    y = IntVar()
    z = IntVar()


    backgroundChecked = False

    header = Label(root, text="insert patient details:", font=("Times", 18, "italic"), fg="#0099ff").place(x=90, y=20)

    pic= ImageTk.PhotoImage(PIL.Image.open("medic.jpeg"))
    picLabel= Label(root, image=pic, height=239, width=200)
    picLabel.place(x=320, y=30)

    FnameLabel = Label(root, text="first name:", font=("Ariel",13))
    FnameLabel.place(x=90, y=65)
    FnameField = Entry(root)
    FnameField.place(x=90, y=95)
    # save the name
    firstname = FnameField.get()
    print(firstname)
    LnameLabel = Label(root, text="last name:", font=("Ariel",13))
    LnameLabel.place(x=90, y=135)
    LnameField = Entry(root)
    LnameField.place(x=90, y=165)

    IDLabel = Label(root, text="ID:", font=("Ariel",13))
    IDLabel.place(x=90, y=200)
    IDField = Entry(root)
    IDField.place(x=90, y=230)
    # save the id
    id = IDField.get()

    genderLabel = Label(root, text="gender:", font=("Ariel",13))
    genderLabel.place(x=85, y=275)
    gender = Radiobutton(root, text="Male", variable=x, value=0, font=("Ariel",13))
    gender.place(x=90, y=310)
    gender = Radiobutton(root, text="Female", variable=x, value=1, font=("Ariel",13))
    gender.place(x=90, y=340)


    ageLabel = Label(root, text="patient birth date:", font=("Ariel",13))
    today = datetime.today()
    cal = Calendar(root, selectmode="day", day=today.day, year=today.year, month=today.month)
    cal.place(x=300, y=300)

    originLabel = Label(root, text="patient origins:", font=("Ariel",13))
    originLabel.place(x=85, y=400)
    origin = Radiobutton(root, text="ethiopian", variable=z, value=0, font=("Ariel",13))
    origin.place(x=90, y=440)
    origin = Radiobutton(root, text="south africans", variable=z, value=1, font=("Ariel",13))
    origin.place(x=90, y=470)
    origin = Radiobutton(root, text="none specific", variable=z, value=2, font=("Ariel",13))
    origin.place(x=90, y=500)


    def write():
        firstname = FnameField.get()
        # save the last name
        lastname = LnameField.get()
        # save the id
        birthday = cal.get_date()
        print(birthday)
        if (firstname!=""or lastname!=""or id!=""):
            id = IDField.get()
            f = open(id+".txt", "w")
            f.write("full name  :" + FnameField.get() + "  "+lastname+"\n")
            f.write("id: " + id+ "\n")
            if(x.get() == 0):
                f.write("gender: male\n")
            elif(x.get() == 1):
                f.write("gender: female\n")
            f.write("birthday date: " + birthday + "\n")
            if (z.get()==0):
                f.write("origins areethiopian\n")
            elif(z.get()==1):
                f.write("origins are south africans\n")
            else:
                f.write("origins are not specifics\n")
                f.close()
        else :
            messagebox.showinfo(title="wrong input", message="must fill in all feilds ")
        root.destroy()


    submit = Button(root, text="submit", padx=150, pady=12, fg="#0099ff",command= write, font=("Ariel",14))
    submit.place(x=90, y=550)
    root.mainloop()


#add_patient()



