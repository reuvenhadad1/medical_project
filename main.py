#312264781 Reuven Hadad
#313577595 Dan Monsonego
#203956321 Yahalomit Levi
import PIL
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
import add_patient
from add_patient import *
import search_patient
from search_patient import *

def accept():
    username = field1.get()
    password = field2.get()
    print(username + password)


    if (doc1==username and passwordfordoc1==password):
        new_window = Tk()
        new_window.geometry("400x150")
        root.destroy()
        new_window.title("Medical Aid")
        myButton1 = Button(new_window, text="search patient", padx=120, pady=12, fg="#0099ff", command=search, font=("Ariel", 20))
        myButton1.place(x=0, y=0)
        myButton2 = Button(new_window, text="add patient", padx=140, pady=12, fg="#0099ff", command=add_patient, font=("Ariel", 20))
        myButton2.place(x=0, y=80)
        new_window.mainloop()

    elif(doc2==username and passwordfordoc2==password):
        new_window = Tk()
        new_window.geometry("400x150")
        root.destroy()
        new_window.title("Medical Aid")
        myButton1 = Button(new_window, text="search patient", padx=120, pady=12, fg="#0099ff", command=search, font=("Ariel", 20))
        myButton1.place(x=0, y=0)
        myButton2 = Button(new_window, text="add patient", padx=140, pady=12, fg="#0099ff", command=add_patient, font=("Ariel", 20))
        myButton2.place(x=0, y=80)
        new_window.mainloop()

    else:
         messagebox.showinfo(title="worng pass",message="username or password is incorrect")




"log in for the doctor "
doc1 = "reuven"
passwordfordoc1="r!1234"
doc2 = "dan"
passwordfordoc2="d!1234"

root = Tk()
root.geometry("420x650")
root.title("Medical Aid")

logo = ImageTk.PhotoImage(PIL.Image.open('icon.jpeg'))
root.iconphoto(False, logo)


helloLabel = Label(root, text="WELCOME", font=("Times", 22, "italic", "bold"), fg="#0099ff").place(x=90, y=25)

pic = ImageTk.PhotoImage(PIL.Image.open("medic.jpeg"))
picLabel = Label(root, image=pic, height=256, width=200)
picLabel.place(x=90, y=90)

label1 = Label(root, text="user name:", font=("Arial", 16))
label1.place(x=90, y=350)
field1 = Entry(root, font=("Arial", 14))
field1.place(x=90, y=400)
label2 = Label(root, text="password:", font=("Arial", 16))
label2.place(x=90, y=450)
field2 = Entry(root, font=("Arial", 14), show="*")
field2.place(x=90, y=500)
myButton = Button(root, text="submit", padx=100, pady=12, font=("Ariel", 14), fg="#0099ff", command=accept).place(x=90, y=550)
root.mainloop()


