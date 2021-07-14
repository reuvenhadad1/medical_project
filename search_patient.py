#312264781 Reuven Hadad
#313577595 Dan Monsonego
#203956321 Yahalomit Levi
import PIL
from tkinter import *
from tkinter import messagebox
from add_visit import *
from PIL import ImageTk, Image
patientid= ""
txt=""
def search():
    root = Tk()
    root.geometry("420x550")
    root.title("Search Patient")

    logo = ImageTk.PhotoImage(PIL.Image.open('icon.jpeg'))
    root.iconphoto(False, logo)

    label1 = Label(root, text="patient ID:", font=("Times", 20, "italic"), fg="#0099ff").place(x=90, y=20)
    field1 = Entry(root, font=("Arial", 18))
    field1.place(x=90, y=90)

    pic = ImageTk.PhotoImage(PIL.Image.open("medic.jpeg"))
    picLabel = Label(root, image=pic, height=236, width=200)
    picLabel.place(x=110, y=170)

    def search_for_patient():
        global patientid
        patientid = str(field1.get())
        filename = patientid + ".txt"
        print(filename)
        try:
            f = open(filename)
            f.close()
            patient_detials1(patientid)
            # root.quit()
        except IOError:
            messagebox.showinfo(title=" Error 404 ", message="no patient found  ")



    def patient_detials1(patientid):
        new_window = Tk()
        new_window.geometry("500x600")
        new_window.title("Patient Details")

        root.destroy()

        def fix1():
            new_window.destroy()
            add_visit(patientid)


        label2 = Label(new_window, text="patient details", font=("Times", 20,"bold"), fg="#0099ff")
        label2.place(x=45, y=20)
        frame = Frame(new_window, width=500, height=450)
        frame.place(x=45, y=100)
        scroll_bar = Scrollbar(frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        f = open(patientid + ".txt", "r")
        Lines = f.readlines()
        mylist = Listbox(frame, yscrollcommand=scroll_bar.set)
        mylist.config(width=65 ,height=22)
        for line in Lines: mylist.insert(END, str(line))
        mylist.pack(fill=BOTH)
        scroll_bar.config(command=mylist.yview)
        f.close()

        myButton = Button(new_window, text="add visit to patient", padx=70, pady=12, fg="#0099ff", command=fix1, font=("Ariel", 14))
        myButton.place(x=40, y=500)

        root.mainloop()


    myButton = Button(root, text="search patient", padx=70, pady=12, fg="#0099ff",command= search_for_patient, font=("Ariel", 14))
    myButton.place(x=90, y=450)


    root.mainloop()

#search()