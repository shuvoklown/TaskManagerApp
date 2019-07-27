# importing modules
import tkinter as tk
import WelcomeScreen
import DataModel

# read from JSON file and populate the listbox with the contents from the file
def insertText(listbox):
    data = DataModel.DataModel.readJson()
    print(len(data))
    count = 0
    for content in data:
        txt = "{}, {}, {}".format(content[0], content[1], content[2])
        listbox.insert(tk.END, txt)
        count =+1
    return count

# split string to separate the 3 variables for placeholder for modification
def splitstring(string):
    array = [x.strip() for x in string.split(',')]
    return array

# user interface: child window to modify 1 specific task
def modifyTaskWindow(listbox, parent, indexValue):
    child_window = tk.Toplevel()
    child_window.title("TaskApp")
    child_window.geometry("300x300")

    tk.Label(child_window, text="Modify Task:").pack()
    tk.Label(child_window, text="Change task name:").place(x=35, y=35)
    nameArray = listbox.get(listbox.curselection())
    array = splitstring(nameArray)
    name = array[0]
    time = array[1]
    description = array[2]
    name_entry = tk.Entry(child_window)
    name_entry.insert(0, name)
    name_entry.place(x=35, y=70)

    tk.Label(child_window, text="Change task time:").place(x=35, y=105)
    time_entry = tk.Entry(child_window)
    time_entry.insert(0, date)
    time_entry.place(x=35, y=140)

    tk.Label(child_window, text="Change task description:").place(x=35, y=175)
    desc_entry = tk.Entry(child_window)
    desc_entry.insert(0, time)
    desc_entry.place(x=35, y=210)

    tk.Button(child_window, text="Submit", command=lambda:closeWindows(child_window, parent, indexValue, name_entry.get(), time_entry.get(), desc_entry.get())).pack(side=tk.BOTTOM)
    child_window.mainloop()

# update the array with modified data and save it in the JSON file
def closeWindows(windowA, windowB, indexValue, newName, newTime, newDesc):
    updatedData = DataModel.DataModel.modifyJson(indexValue)
    DataModel.DataModel.createJson(updatedData, newName, newTime, newDesc)
    WelcomeScreen.closeWindow(windowA)
    WelcomeScreen.closeWindow(windowB)

# User Interface: show tasks existing to select and modify 1 task
def selecttask_window():
    main_window = tk.Toplevel()
    main_window.title("Reminder App")
    main_window.geometry("500x500")

    tk.Label(main_window, text = "Select existing task:").pack()
    scroll_bar = tk.Scrollbar(main_window)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    selectTask_box = tk.Listbox(master=main_window, yscrollcommand=scroll_bar.set)
    indexNumber = insertText(selectTask_box)
    scroll_bar.config(command=selectTask_box.yview)

    tk.Button(main_window, text="Edit task", command=lambda: modifyTaskWindow(selectTask_box, main_window, indexNumber)).pack(side=tk.BOTTOM)
    selectTask_box.config(height=200, width=60)
    selectTask_box.pack()

    tk.mainloop()