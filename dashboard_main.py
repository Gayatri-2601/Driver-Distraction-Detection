 
from PIL import ImageTk
from matplotlib import pyplot as plt
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
from tkinter import *
import mysql.connector as con
import tkinter.messagebox
from PIL import ImageTk,Image
global var
#import TrainModule
global screen


def main_screen():
    
    
    global screen3
    screen3=Tk()
    #screen3=Toplevel(screen)
   # var = StringVar()
    C = Canvas(screen3, bg="blue", height=140, width=320)
    filename = PhotoImage(file = "186040.gif")
    background_label = Label(screen3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.pack()
    screen3.configure(background='white')
    screen3.title("DASHBOARD")
    screen3.geometry('1280x720')
    
    Label(screen3, text="DRIVER DISTRACTION DETECTION", bg="Grey", height=1, width=100,font=("Arial Bold", 20)).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    


    Label(screen3, text="", bg="white").pack()
    b0 =  Button(screen3,text="Detect Driver Status",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13),command=dd)
    b0.pack()

    
   

    
    



def admin_login():
    global screen5
    global user_id
    global passw_id
    
    screen5=Tk()
   # screen2=Toplevel(screen5)
    screen5.configure(background='white')
    screen5.geometry('1280x720')
    Label(screen5, text="Admin Login", font=("Arial Bold", 25),bg="grey",width=250,height=2).pack()
    Label(screen5, text="", bg="white").pack()
    Label(screen5, text="", bg="white").pack()
    name = Label(screen5, text="User Id", height=2, bg="white",font=("Arial Bold", 11))
    name.pack()
    user_id = Entry(screen5, width=20)
    user_id.pack()

    name = Label(screen5, text="Password", height=2, bg="white",font=("Arial Bold", 11))
    name.pack()
    passw_id = Entry(screen5, width=20)
    passw_id.pack()
    
    
    Label(screen5, text="", bg="white").pack()
    Label(screen5, text="", bg="white").pack()
    login1 = Button(screen5, text="Login", height=2, width=30,command=login,bg="black",fg="white",font=("Arial Bold", 13))
    login1.pack()




def login():
    name=user_id.get()
    password=passw_id.get()
    if name=="admin" and password=="admin":
        messagebox.showinfo("Information", "Login Successfull")
        screen5.destroy()
        main_screen()
        
    else:
        messagebox.showinfo("Information", "Wrong Credentials try again")
        


def dd():
    import drowsiness_detection
    screen5.destroy()
   
   


    cv2.destroyAllWindows()
admin_login()


    







