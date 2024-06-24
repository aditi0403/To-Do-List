import tkinter as tk
from tkinter import messagebox
customFont=("Arimo", 15, "bold")

def addTask():
    task= entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning" , "enter a task pls")

def deleteTask():
    toBeDeletedT= listbox.curselection()
    if toBeDeletedT:
        listbox.delete(toBeDeletedT)
    else:
        messagebox.showwarning("warning", "what to delete tell")

root=tk.Tk()
root.title("To DO List Apppppp")
root.configure(bg="lightgrey")

entry= tk.Entry(root, width=40, fg="black")
entry.grid(row=0, column=0, padx=10, pady=10)

addButton= tk.Button(root, text="Add a Task", command=addTask, bg="pink", fg="white", bd='2')
addButton.grid(row=0,column=1, padx=10, pady=10)

deleteButton= tk.Button(root, text="Delete Task", command=deleteTask, bg="white", fg="pink", bd='2')
deleteButton.grid(row=0,column=2, padx=10, pady=10)

listbox= tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=20)
listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()