import os
import time
import Tkinter as t
from Tkinter import *


def back1():
    screen1.destroy()


def back2():
    screen2.destroy()
    
    

def exit():
    screen.destroy()


def delete3():
    screen3.destroy()


def delete4():
    screen4.destroy()


def delete5():
    screen5.destroy()


def saved():
    saved = t.Label(screen7, text = "Note saved", fg = "green", font = ("Calibri", 11))
    saved.pack()
    screen7.after(1500, saved.destroy)

def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()


def open_drawer():
    pass
    


def session():
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("400x400")
    Label(screen6, text = "Welcome to the dashboard").pack()
    ################## input ######################
    Button(screen6, text = "Open Drawer", command = open_drawer).pack()


def login_success():
    session()


def incorrect_password():
    ip = t.Label(screen2, text = "Incorrect password!", fg = "red", font = ("Calibri", 11))
    ip.pack()
    screen2.after(1500, ip.destroy)


def user_not_found():
    unf = t.Label(screen2, text = "User not found!", fg = "red", font = ("Calibri", 11))
    unf.pack()
    screen2.after(1500, unf.destroy)

    
def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    ################### input #######################

    rs = t.Label(screen1, text = "Registration Successful", fg = "green", font = ("Calibri", 11))
    rs.pack()
    screen1.after(1500, rs.destroy)


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below to create a new account").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
    Button(screen1, text = "Back", width = 10, height = 1, command = back1).pack()


def login_verify():
    global username_verify
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            incorrect_password()
            

    else:
        user_not_found()
    

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to log in").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username *").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password *").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    Button(screen2, text = "Back", width = 10, height = 1, command = back2).pack()
    


def main_screen():
    global screen
    screen = Tk()
    screen.title ("Green Light")
    screen.geometry ("300x250")
    screen.resizable(False,False)
    Label(text = "Green Light", bg="green", width="300", height ="2", font = ("Times New Roman", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text= "Register", height = "2", width = "30", command = register).pack()
    Label(text="").pack()
    Button(text= "Exit", height = "2", width = "30", command = exit).pack()


    screen.mainloop()

main_screen()
