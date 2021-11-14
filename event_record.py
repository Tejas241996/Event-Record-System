from tkinter import *
from tkinter import ttk, messagebox
from csv import DictWriter
import os
import tkinter as tk
import smtplib

root = Tk()
root.title('Event Record System')
root.geometry("300x350")

#creating  labels

label_head = tk.Label(root, text='')
label_head.grid(row=0, column=0)

label1 = ttk.Label(root, text="Enter Your Name :")
label1.grid(row=1, column=0, sticky=tk.W)

label_head = tk.Label(root, text='Enter Your Collage Name')
label_head.grid(row=2, column=0)

label2 = tk.Label(root, text="Enter Your Email :")
label2.grid(row=3, column=0, sticky=tk.W)

label3 = tk.Label(root, text="Enter Your Age :")
label3.grid(row=4, column=0, sticky=tk.W)

label4 = tk.Label(root, text="Enter Your number :")
label4.grid(row=5, column=0, sticky=tk.W)

label5 = tk.Label(root, text="Select Your gender :")
label5.grid(row=6, column=0, sticky=tk.W)

label_head = tk.Label(root, text='')
label_head.grid(row=7, column=0)

label_head = tk.Label(root, text='')
label_head.grid(row=10, column=0)
#  Creating Entry box

entrybox_1_var = tk.StringVar()
entrybox_1 = ttk.Entry(root, width = 16, textvariable = entrybox_1_var)
entrybox_1.grid(row=1, column=1, sticky=tk.W)
entrybox_1.focus()

entrybox_2_var = tk.StringVar()
entrybox_2 = tk.Entry(root, width = 16, textvariable = entrybox_2_var)
entrybox_2.grid(row=2, column=1, sticky=tk.W)

entrybox_3_var = tk.StringVar()
entrybox_3 = tk.Entry(root, width = 16, textvariable = entrybox_3_var)
entrybox_3.grid(row=3, column=1, sticky=tk.W)

entrybox_4_var = tk.StringVar()
entrybox_4 = tk.Entry(root, width = 16, textvariable = entrybox_4_var)
entrybox_4.grid(row=4, column=1, sticky=tk.W)

entrybox_5_var = tk.StringVar()
entrybox_5 = tk.Entry(root, width = 16, textvariable = entrybox_5_var)
entrybox_5.grid(row=5, column=1, sticky=tk.W)

#creating combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root,width=13, textvariable = gender_var, state='readonly')
gender_combobox['values']= ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=6, column=1)

# creating radio button

usertype = StringVar()
radio_btn1 = ttk.Radiobutton(root, text='Project', value='Project', variable=usertype)
radio_btn1.grid(row=8, column=0)

radio_btn2 = ttk.Radiobutton(root, text='Seminar', value='Seminar', variable=usertype)
radio_btn2.grid(row=8, column=1)

#creating check button
checkvar = IntVar()
check_btn = ttk.Checkbutton(root, text='check if you want to participated on event', variable=checkvar)
check_btn.grid(row=9, columnspan=3)

def action():
    user_name = entrybox_1_var.get()
    user_collage = entrybox_2_var.get()
    user_email = entrybox_3_var.get()
    user_age = entrybox_4_var.get()
    user_number = entrybox_5_var.get()
    gender_vari = gender_var.get()
    event_type = usertype.get()
    if checkvar.get()==0:
        Participated = 'No'
    else:
        Participated = 'yes'

# writing to csv file

    with open("Event_records.csv", 'a', newline='') as file:
        dict_writer = DictWriter(file, fieldnames=['UserName', 'UserCollage', 'User email address', 'User age', 'User number', 'User gender', 'Event type', 'Participated'])

        if os.stat("Event_records.csv").st_size==0: #checks if file contains the header or not
            DictWriter.writeheader(dict_writer)

        dict_writer.writerow({'UserName': user_name, 'UserCollage': user_collage , 'User email address': user_email, 'User age': user_age, 'User number': user_number , 'User gender': gender_vari, 'Event type': event_type, 'Participated': Participated})

        messagebox.showinfo('Message', 'Record added Successfully')  #creating message box

    name = entrybox_1.delete(0, tk.END)
    collage = entrybox_2.delete(0, tk.END)
    age = entrybox_3.delete(0, tk.END)
    email = entrybox_4.delete(0, tk.END)
    number = entrybox_5.delete(0, tk.END)
    label1.configure(foreground='Blue')

#Sending a confirmation email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('fegadetejas@gmail.com', 'ygsrnprujwmjpmxj')
    server.sendmail('fegadetejas@gmail.com',
                    user_email,
                    "Thank you for participating in our event !")

#creating buttons
submit_btn = tk.Button(root, text='Submit', command= action)
submit_btn.grid(row=11, columnspan=3)

root.mainloop()




