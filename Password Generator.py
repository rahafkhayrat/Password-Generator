from tkinter import *
import random , string
import pyperclip


root = Tk()
root.geometry("400x400")  
root.resizable(0, 0)
root.configure(background="white")
root.title("Password Generator")

# Adding a label
Label(root, text="Password Generator",background="white",font=("arial", 20, "bold")).pack()


pass_label=Label(root,text="Password Length",font="arial 15 bold").pack()
pass_str=IntVar()
Spinbox(root, from_=8, to_=32, textvariable=pass_str,width=20).pack()

def Generator():
    password=" "
    for x in range(0,4):
        password=random.choice(string.ascii_uppercase) +random.choice(string.ascii_lowercase) +random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_str.get()-4):    
    
        password=password+random.choice(string.ascii_uppercase +string.ascii_lowercase +string.digits+string.punctuation)
    pass_str.set(password)
Button(root,text="Generate Password",command=Generator).pack(pady=8)
Entry(root,textvariable=pass_str).pack()

def copy_password():
    pyperclip.copy(pass_str.get())

Button(root , text="Copy", command=copy_password).pack(pady=8)

  
root.mainloop()
