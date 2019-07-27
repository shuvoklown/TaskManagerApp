# importing modules
import tkinter as tk
import WelcomeScreen
import DataModel
import EditTaskScreen

# delete the selected task and update the JSON file
def deleteSelection(listbox, index):
    listbox.delete(listbox.curselection())
    updatedData = DataModel.DataModel.modifyJson(index)
    DataModel.DataModel.updateDeletedJson(updatedData)

# user interface
def deltasks_window():
    main_window = tk.Toplevel()
    main_window.title("Task Tracker App")
    main_window.geometry("500x500")

    tk.Label(main_window, text="Delete existing task:").pack()

    scroll_bar = tk.Scrollbar(main_window)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    selecttask_box = tk.Listbox(master=main_window, yscrollcommand=scroll_bar.set)
    index = EditTaskScreen.insertText(selecttask_box)
    scroll_bar.config(command=selecttask_box.yview)

    done_btn = tk.Button(main_window, text="Done", command=lambda: WelcomeScreen.closeWindow(main_window))
    done_btn.pack(side=tk.BOTTOM)
    delete_btn = tk.Button(main_window, text="Delete", command=lambda: deleteSelection(selecttask_box, index))
    delete_btn.pack(side=tk.BOTTOM)
    selecttask_box.config(height=200, width=60)
    selecttask_box.pack()

    tk.mainloop()