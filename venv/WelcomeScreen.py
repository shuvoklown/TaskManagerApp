# importing modules
import tkinter.ttk as tk
import CreateTaskScreen
import EditTaskScreen
import DeleteTaskScreen
import DataModel

# action function to close window
def closeWindow(window):
    window.destroy()

# check if file exists, if true then read it, else create a file with empty parameters
def checkReminders():
    check = DataModel.DataModel.checkfile()
    if check:
        return DataModel.DataModel.readJson()
    else:
        DataModel.DataModel.createJson(reminders=None, name=None, time=None, desc=None)

# user interface
def launch(main_window):
    main_window.title("Reminder App")
    main_window.geometry("300x200")

    reminders = checkReminders()
    tk.Label(main_window, text = "Welcome to TaskManager App", font = ('Helvetica', '14')).pack()
    tk.Button(main_window, text = "Create New Task", command=lambda: CreateTaskScreen.createTask(reminders)).place(x=100, y=40)
    tk.Button(main_window, text = "Edit Existing Task", command=EditTaskScreen.selecttask_window).place(x=98, y=80)
    tk.Button(main_window, text = "Delete Existing Task", command=DeleteTaskScreen.deltasks_window).place(x=92, y=120)
    tk.Button(main_window, text = "Exit", command=lambda: closeWindow(main_window)).place(x=115, y=160)
    main_window.mainloop()