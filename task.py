import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        selected_task = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task)
        listbox_tasks.delete(selected_task)
        listbox_tasks.insert(tk.END, f"(DONE) {task_text}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter Task:").pack(pady=5)
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)
btn_done = tk.Button(root, text="Mark Done", command=mark_done)
btn_done.pack(pady=5)
btn_remove = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove.pack(pady=5)


root.mainloop()
