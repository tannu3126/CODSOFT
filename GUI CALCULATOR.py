import tkinter as Tk
def click(value):
    current_text = Tk.entry.get()
    Tk.entry.delete(0, Tk.END)
    Tk.entry.insert(Tk.END, current_text + value)

def equal():
    try:
        y = eval(Tk.entry.get())
        Tk.entry.delete(0, Tk.END)
        Tk.entry.insert(Tk.END, y)
    except Exception:
        Tk.entry.delete(0, Tk.END)
        Tk.entry.insert(Tk.END, "ERROR")
def clear():
    Tk.entry.delete(0, Tk.END)
root = Tk.Tk()
root.title("CALCULATOR")
entry = Tk.Entry(root, width=20, font=('arial', 25), borderwidth=5, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('=',4,0), ('0', 4, 1), ('.', 4, 2), ('-', 4, 3),
    ('C', 5,0)
]
for (text, row, col) in buttons:
    if text == "=":
        button = Tk.Button(root, text=text, font=('arial', 20), command=equal)
    elif text == "C":
        button = Tk.Button(root, text=text, font=('arial', 20), command=clear)
    else:
        button = Tk.Button(root, text=text, font=('arial', 20), command=lambda value=text: click(value))
    
    button.grid(row=row, column=col, sticky="nsew", ipadx=20, ipady=20)
for i in range(6):  # 5 rows + 1 for the entry
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 columns
    root.grid_columnconfigure(i, weight=1)
root.mainloop()
