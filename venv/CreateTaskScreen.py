# importing modules
import tkinter as tk
import WelcomeScreen
import DataModel
import teek as te

# user interface
def createTask(reminders):
    childwindow = tk.Toplevel()
    childwindow.title("Reminder App")
    childwindow.geometry("300x300")

    tk.Label(childwindow, text = "Create new task:").pack()
    tk.Label(childwindow, text = "Add task name:").place(x=35, y=35)
    taskname_entry = tk.Entry(childwindow)
    taskname_entry.place(x=35, y=70)
    tasktime_lbl = tk.Label(childwindow, text = "Add task time:")
    tasktime_lbl.place(x=35, y=105)
    tasktime_entry = tk.Entry(childwindow)
    tasktime_entry.place(x=35, y=140)
    taskdesc_lbl = tk.Label(childwindow, text = "Add task description:")
    taskdesc_lbl.place(x=35, y=175)
    taskdesc_entry = tk.Entry(childwindow)
    taskdesc_entry.place(x=35, y=210)
    taskbutton = tk.Button(childwindow, text="Create Task", command=lambda: storeData(taskname_entry.get(), tasktime_entry.get(), taskdesc_entry.get(), childwindow, reminders))
    taskbutton.place(x=55, y=245)
    childwindow.mainloop()

# update json file and close window
def storeData(name, time, desc, window, object):
    DataModel.DataModel.createJson(object, name, date, time)
    WelcomeScreen.closeWindow(window)