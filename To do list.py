from tkinter import *
import os

root = Tk()
root.title("💜 Ranim's Elegant To-Do List 💜")
root.geometry("520x580")
root.resizable(False, False)
root.configure(bg="#f9f0ff")  

tasks = []
FILE_NAME = "tasks.txt"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        for line in f:
            t = line.strip()
            if t:
                tasks.append(t)


def save_tasks():
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def add_task():
    t = task_entry.get().strip()
    if t:
        tasks.append(t)
        task_listbox.insert(END, t)
        task_entry.delete(0, END)
        save_tasks()

def delete_task():
    sel = task_listbox.curselection()
    if sel:
        i = sel[0]
        task_listbox.delete(i)
        tasks.pop(i)
        save_tasks()

def clear_tasks():
    task_listbox.delete(0, END)
    tasks.clear()
    save_tasks()

def mark_complete():
    sel = task_listbox.curselection()
    if sel:
        i = sel[0]
        task = tasks[i]
        if not task.startswith("✅ "):
            tasks[i] = "✅ " + task
            task_listbox.delete(i)
            task_listbox.insert(i, tasks[i])
            task_listbox.itemconfig(i, fg="#28a745")  # أخضر جذاب
            save_tasks()

def on_enter(e):
    e.widget['bg'] = '#d8b4ff'  

def on_leave(e, original_color):
    e.widget['bg'] = original_color

main_frame = Frame(root, bg="#f9f0ff")
main_frame.pack(expand=True)

title_label = Label(
    main_frame, 
    text="📝 Ranim's Elegant To-Do List", 
    font=("Helvetica", 22, "bold"), 
    bg="#f9f0ff", fg="#8b2be2"
)
title_label.pack(pady=(20,15))

task_entry = Entry(main_frame, width=40, font=("Helvetica", 14))
task_entry.pack(pady=(0,15))

row1_frame = Frame(main_frame, bg="#f9f0ff")
row1_frame.pack(pady=(0,5))

add_btn = Button(row1_frame, text="Add Task", width=22, bg="#c29fff", fg="white", font=("Helvetica", 12, "bold"), command=add_task)
add_btn.pack(side=LEFT, padx=5)
add_btn.bind("<Enter>", on_enter)
add_btn.bind("<Leave>", lambda e: on_leave(e, "#c29fff"))

del_btn = Button(row1_frame, text="Delete Task", width=22, bg="#ff7f91", fg="white", font=("Helvetica", 12, "bold"), command=delete_task)
del_btn.pack(side=LEFT, padx=5)
del_btn.bind("<Enter>", on_enter)
del_btn.bind("<Leave>", lambda e: on_leave(e, "#ff7f91"))

row2_frame = Frame(main_frame, bg="#f9f0ff")
row2_frame.pack(pady=(0,15))

clear_btn = Button(row2_frame, text="Clear All", width=22, bg="#ffbf7f", fg="white", font=("Helvetica", 12, "bold"), command=clear_tasks)
clear_btn.pack(side=LEFT, padx=5)
clear_btn.bind("<Enter>", on_enter)
clear_btn.bind("<Leave>", lambda e: on_leave(e, "#ffbf7f"))

complete_btn = Button(row2_frame, text="Mark Complete", width=22, bg="#4db6ac", fg="white", font=("Helvetica", 12, "bold"), command=mark_complete)
complete_btn.pack(side=LEFT, padx=5)
complete_btn.bind("<Enter>", on_enter)
complete_btn.bind("<Leave>", lambda e: on_leave(e, "#4db6ac"))

list_frame = Frame(main_frame)
list_frame.pack(pady=(0,20))

scroll = Scrollbar(list_frame)
scroll.pack(side=RIGHT, fill=Y)

task_listbox = Listbox(list_frame, width=52, height=18, font=("Helvetica", 12), yscrollcommand=scroll.set, bg="#fffafa")
task_listbox.pack()

scroll.config(command=task_listbox.yview)

for idx, t in enumerate(tasks):
    task_listbox.insert(END, t)
    if t.startswith("✅ "):
        task_listbox.itemconfig(idx, fg="#28a745")

root.mainloop()