
from tkinter import *

import os
def none():
    screen1.destroy()

def no_mistake():
    os.system("sleep.bat")

def yes():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Ready to shutdown")
    screen1.geometry("450x450")
    Label(screen1, text = "Are you sure you want to proceed? ", bg = "white", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Yes, shutdown", height = "2", width = "30",bg = "red", ).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Sleep instead", height = "2", width = "30",bg = "green", command = no_mistake).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "None, It is a mistake", height = "2", width = "30",bg = "lightblue", command = none).pack()
    

    
def no():
    screen.destroy()
    

def main_screen ():
    global screen
    screen=Tk()
    screen.geometry("500x550")
    screen.title("Shutdown Application")
    Label(text = "Shutdown Application", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text = "Do you want to completely shutdown your system?", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text = "Yes", height = "2", width = "30", command = yes).pack()
    Label(text = "").pack()
    Button(text = "No", height = "2", width = "30", command = no).pack()
    
    screen.mainloop() 
    
main_screen()
