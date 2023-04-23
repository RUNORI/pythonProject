from tkinter import *
from tkinter import messagebox, filedialog
import os
import shutil


root = Tk()
root.geometry("900x550+100+30")
root.title("file manager app")
root.config(background="black")

def open_file():
    file = filedialog.askopenfilename()
    os.startfile(file)
    messagebox.showinfo('open file', file+" opened successfully")

def arr_file():
    files = os.listdir(path)

    for i in files:
        filename, extension = os.path.splitext(i)
        extension_1 = extension[1:]
        folder_path = path + "\\" + extension_1
        if os.path.exists(folder_path):
            shutil.move(path + "\\" + i, path + "\\" + extension_1 + "\\" + i)
        else:
            os.makedirs(folder_path)
            shutil.move(path + "\\" + i, path + "\\" + extension_1 + "\\" + i)
source_location = StringVar()
def source_browse():
    global files_list
    files_list = list(filedialog.askopenfilenames())
    path.insert('1', files_list)


open_btn = Button(root, text="Open File",command=open_file, width=15,font=('bold',14))
open_btn.grid(row=2, column=0,pady=20, padx=20)
root.mainloop()