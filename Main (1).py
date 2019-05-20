import os
import RPi.GPIO as GPIO
from time import sleep
import time
import Tkinter as t
from Tkinter import *
from Functions import *
# Creates the variable for the RFID Scanner function which is in the Function File
reader = SimpleMFRC522()
# Functions for deleting and creating the GUI 
def back1():
    screen1.destroy()

def back2():
    screen2.destroy() 

def exit():
    screen.destroy()

def delete6():
    screen6.destroy()

def delete7():
    screen7.destroy()
    
def delete8():
    screen8.destroy()
    
def delete9():
    screen9.destroy()
    
# Function to turn the servo to open the the right drawer
def open_drawerR():
    # 0.001 for counter clockwise - 4 loops - 0.001
    # 0.005 for clockwise - 7 loops - 0.005
    global screen8
    screen8.title("Close Drawer")
    screen8.attributes("-fullscreen", True)
    Label(screen8, text = "Insert drawer when done").pack()
    Button(screen8, text = "Close Drawer", command = close_drawerR).pack()
    GPIO.setmode(GPIO.BCM)
    SR = 16
    GPIO.setup(SR,GPIO.OUT)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    sleep(0.5)
    for n in range(8):
        sleep(1)
        GPIO.output(SR, GPIO.HIGH)
        sleep(0.005)
        GPIO.output(SR, GPIO.LOW)
        sleep(0.005)
    GPIO.output(R, GPIO.LOW)        
    GPIO.cleanup()
# Function to turn the servo to close the left drawer  
def close_drawerR():
    delete7()
    GPIO.setmode(GPIO.BCM)
    SR = 16
    GPIO.setup(SR,GPIO.OUT)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    sleep(0.5)
    for n in range(4):
        sleep(1)
        GPIO.output(SR, GPIO.HIGH)
        sleep(0.001)
        GPIO.output(SR, GPIO.LOW)
        sleep(0.001)
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    sleep(0.5)
    GPIO.cleanup()
# Function to turn the servo in order to open the left drawer
def open_drawerL():
    # 0.001 for counter clockwise - 4 loops - 0.001
    # 0.005 for clockwise - 7 loops - 0.005
    
    global screen9
    screen9.title("Close Drawer")
    screen9.attributes("-fullscreen", True)
    Label(screen9, text = "Insert drawer when done").pack()
    Button(screen9, text = "Close Drawer", command = close_drawerL).pack()
    GPIO.setmode(GPIO.BCM)
    SL = 17
    GPIO.setup(SL,GPIO.OUT)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    sleep(0.5)
    for n in range(4):
        sleep(1)
        GPIO.output(SL, GPIO.HIGH)
        sleep(0.001)
        GPIO.output(SL, GPIO.LOW)
        sleep(0.001)
    GPIO.output(R, GPIO.LOW)
    GPIO.cleanup()
# Function to turn the servo in order to close and lock the left drawer   
def close_drawerL():
    delete7()
    GPIO.setmode(GPIO.BCM)
    SL = 17
    GPIO.setup(SL,GPIO.OUT)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    sleep(0.5)
    for n in range(9):
        sleep(1)
        GPIO.output(SL, GPIO.HIGH)
        sleep(0.005)
        GPIO.output(SL, GPIO.LOW)
        sleep(0.005)
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    sleep(0.5)
    delete9()
    GPIO.cleanup()
# Function to close the Admin Drawer otherwise known as the bottom drawer which requires both servos to turn 
def close_drawerA():
    
    GPIO.setmode(GPIO.BCM)
    SR = 16
    GPIO.setup(SR,GPIO.OUT)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    sleep(0.5)
    for n in range(8):
        sleep(1)
        GPIO.output(SR, GPIO.HIGH)
        sleep(0.005)
        GPIO.output(SR, GPIO.LOW)
        sleep(0.005)
    GPIO.cleanup()
    
    sleep(1)
    
    GPIO.setmode(GPIO.BCM)
    SL = 17
    GPIO.setup(SL,GPIO.OUT)
    for n in range(4):
        sleep(1)
        GPIO.output(SL, GPIO.HIGH)
        sleep(0.001)
        GPIO.output(SL, GPIO.LOW)
        sleep(0.001)
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    sleep(0.5)
    GPIO.cleanup()
    
# Function to open the Admin Drawer which requires both servos to turn
def open_drawerA():
    GPIO.setmode(GPIO.BCM)
    SR = 16
    GPIO.setup(SR,GPIO.OUT)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    sleep(0.5)
    for n in range(4):
        sleep(1)
        GPIO.output(SR, GPIO.HIGH)
        sleep(0.001)
        GPIO.output(SR, GPIO.LOW)
        sleep(0.001)
    GPIO.cleanup()
    
    sleep(1)
    
    GPIO.setmode(GPIO.BCM)
    SL = 17
    GPIO.setup(SL,GPIO.OUT)
    for n in range(9):
        sleep(1)
        GPIO.output(SL, GPIO.HIGH)
        sleep(0.005)
        GPIO.output(SL, GPIO.LOW)
        sleep(0.005)
    GPIO.output(R, GPIO.LOW)
    GPIO.cleanup()
# Creates the screens of the GUI
def session1():
    global screen6
    GPIO.output(R, GPIO.HIGH)
    sleep(0.5)
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.attributes("-fullscreen", True)
    Label(screen6, text = "Welcome to the dashboard").pack()
    Button(screen6, text = "Open Drawer 1", command = open_drawerL).pack()
    Button(screen6, text = "Logout", command = delete6).pack()
    back2()
    
def session2():
    global screen6
    GPIO.output(R, GPIO.HIGH)
    sleep(0.5)
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.attributes("-fullscreen", True)
    Label(screen6, text = "Welcome to the dashboard").pack()
    Button(screen6, text = "Open Drawer 2", command = open_drawerR).pack()
    Button(screen6, text = "Logout", command = delete6).pack()
    back2()
    
def session3():
    global screen6
    GPIO.output(R, GPIO.HIGH)
    sleep(0.5)
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.attributes("-fullscreen", True)
    Label(screen6, text = "Welcome to the dashboard").pack()
    Button(screen6, text = "Open Drawer 1", command = open_drawerL).pack()
    Button(screen6, text = "Open Drawer 2", command = open_drawerR).pack()
    Button(screen6, text = "Logout", command = delete6).pack()
    back2()
    
def session4():
    global screen6
    GPIO.output(R, GPIO.HIGH)
    sleep(0.5)
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.attributes("-fullscreen", True)
    Label(screen6, text = "Welcome to the dashboard").pack()
    Button(screen6, text = "Open Drawer 1", command = open_drawerL).pack()
    Button(screen6, text = "Open Drawer 2", command = open_drawerR).pack()
    Button(screen6, text = "Open Bottom Drawer", command = open_drawerA).pack()
    Button(screen6, text = "Close Bottom Drawer", command = close_drawerA).pack()
    Button(screen6, text = "Logout", command = delete6).pack()
    back2()
# Functions to check user login and the creation of users
def login_success(clearance):
    if clearance == "1":
        session1()
    elif clearance == "2":
        session2()
    elif clearance == "3":
        session3()
    elif clearance == "4":
        session4()

def incorrect_password():
    ip = t.Label(screen2, text = "Incorrect password or ID!", fg = "red", font = ("Calibri", 11))
    ip.pack()
    screen2.after(1500, ip.destroy)

def user_not_found():
    unf = t.Label(screen2, text = "User not found!", fg = "red", font = ("Calibri", 11))
    unf.pack()
    screen2.after(1500, unf.destroy)
 
def register_user():
    # Creates a file which has the username, password, and clearance level in it
    read = Read()
    i1 = read.prtID()
    i1 = str(i1)
    if i1 == "522734291168": 
        username_info = username.get()
        password_info = password.get()
        clearance_info = clearance.get()
        
        read1 = Read()
        id_info = read1.prtID()
        id_info = str(id_info)
        write1 = Write(password_info)
    
        file = open(username_info, "w")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        file.write(id_info+"\n")
        file.write(clearance_info)
        file.close()
        
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        clearance_entry.delete(0, END)
        
        rs = t.Label(screen1, text = "Registration Successful", fg = "green", font = ("Calibri", 11))
        rs.pack()
        screen1.after(1500, rs.destroy)
    else:
        incorrect_password()        

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    global clearance
    global clearance_entry
    username = StringVar()
    password = StringVar()
    clearance = StringVar()

    Label(screen1, text = "Please enter details below to create a new account").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "Clearance *").pack()
    clearance_entry = Entry(screen1, textvariable = clearance)
    clearance_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
    Button(screen1, text = "Back", width = 10, height = 1, command = back1).pack()

def login_verify():
    # Checks to see if the user that is trying to log in is on the file with the username, password, and clearance
    global username_verify
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    DIR = os.path.dirname(__file__) #Path
    list_of_files = os.listdir(DIR)
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            read = Read()
            p1 = read.prtTXT()
            i1 = read.prtID()
            i1 = str(i1)
            dif = len(p1) - len(password1)
            pass1 = password1 + " " * dif
            if p1 == pass1 :
                if i1 in verify:
                    f1 = verify[3]
                    login_success(f1)
            else:
                incorrect_password()
        else:
            incorrect_password()        
    else:
        user_not_found()
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.attributes("-fullscreen", True)
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
    screen.attributes("-fullscreen", True)
    Label(text = "Green Light", bg="green", width="300", height ="2", font = ("Times New Roman", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text= "Register", height = "2", width = "30", command = register).pack()
    Label(text="").pack()
    Button(text= "Exit", height = "2", width = "30", command = exit).pack()

    screen.mainloop()
    
################################################MAIN###################################################################################
R = 18
G = 19
B = 20
main_screen()
