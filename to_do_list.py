import tkinter as tk 
from tkinter import messagebox, simpledialog
def add_task():
    task=task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task")
def delete_task():
    task_indices=task_listbox.curselection()
    if task_indices:
        task_listbox.delete(task_indices[0])
    else:
        messagebox.showwarning("Warning","You must enter a task")
def edit_task():
    task_indices=task_listbox.curselection()
    if task_indices:
        selected_task_index = task_indices[0]
        task = task_listbox.get(selected_task_index)
        new_task=simpledialog.askstring("Update Task","Edit the task:", initialvalue=task)
        if new_task:
                task_listbox.delete(selected_task_index)
                task_listbox.insert(selected_task_index, new_task)
    else:
        messagebox.showwarning("Warning", "You must select a task to edit.")
root= tk.Tk()
root.title("To-Do List Application")
root.geometry('350x600')
root.config(bg='pink')
root.resizable(False,False)
add_title=tk.Label(root,text='To-Do List Application')
add_title.pack(pady=10)
task_listbox=tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)
task_entry=tk.Entry(root, width=50,)
task_entry.pack(pady=10)
add_task_button=tk.Button(root,text="Add Task",bg="yellow",font="Ariel" ,command=add_task)
add_task_button.pack(pady=5)
delete_task_button=tk.Button(root,text="Delete Task",bg="yellow", font="Ariel",command=delete_task)
delete_task_button.pack(pady=5)
update_task_button=tk.Button(root,text="Update Task",bg="yellow",font="Ariel",command=edit_task)
update_task_button.pack(pady=5)
root.mainloop()

