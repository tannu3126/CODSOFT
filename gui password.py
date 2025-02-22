import random
import string
import tkinter as tk
from tkinter import messagebox

def gen_pass():
    try:
        lenght=int(entry_lenght.get())
        if lenght<8:
            messagebox.showerror("ERROR....","Password must be at least 8")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password=''.join(random.choice (characters)for _ in range (lenght))
        entry_password.delete(0,tk.END)
        entry_password.insert(0,password)
    except ValueError:
        messagebox.showerror("ERROR...","Enter a valid number")

root = tk.Tk()
root.title("GUI PASSWORD GENERATOR")
root.geometry("400x200")
root.resizable(False,True)
tk.Label( root,text="Enter password length:").pack(pady=5)
entry_lenght=tk.Entry(root,width=10)
entry_lenght.pack(pady=5)
btn_generate=tk.Button(root,text="password",command=gen_pass)
btn_generate.pack(pady=10)
entry_password=tk.Entry(root,width=40)
entry_password.pack(pady=5)
root.mainloop()