#importing Libraries

from tkinter import *
import random, string
import pyperclip
import hashlib
import os
import re


###initialize window

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("DataFlair - PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='DataFlair', font ='arial 15 bold').pack(side = BOTTOM)


pass_label_text = "Password length"
###select password length
pass_label = Label(root, text = pass_label_text, font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()



#####define function

pass_str = StringVar()
passwordsafety="Parooli turvalisuse tase"

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
    #password length difficulty
    x = True
    while x:
        if (len(password) < 6 or len(password) > 20):
            break
        elif not re.search("[a-z]", password):
            TestLabel['text'] = "Nõrk parool"
            break
        elif not re.search("[0-9]", password):
            TestLabel['text'] = "Keskmine parool"
            break
        elif not re.search("[A-Z]", password):
            TestLabel['text'] = "Tugev parool"
            break
        elif not re.search("[$#@]", password):
            TestLabel['text'] = "Väga tugev parool"
            break
        elif re.search("\s", password):
            break
        else:

# re.search("[a-z]" - nõrk
    # TestLabel['text'] = "nõrk"
# re.search("[a-z]" and re.search("[0-9]" - keskmine
    # TestLabel['text'] = "keskmine"
# re.search("[a-z]" and re.search("[0-9]" and re.search("[A-Z]" - tugev
    # TestLabel['text'] = "tugev"


            print("Valid Password")

            x = False
            break

    if x:

        print("Not a Valid Password")

   


###button

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

##password difficulty text box

TestLabel = Label(root, text =passwordsafety, font ='arial 15 bold')
TestLabel.pack(pady = 6)



# loop to run program
root.mainloop()
