import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = task_entry.get().strip()
        if task:
            self.tasks.append(task)
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
        task_index = selected_index[0]
        task_listbox.delete(task_index)
        del self.tasks[task_index]

    def clear_list(self):
        task_listbox.delete(0, tk.END)
        self.tasks.clear()

    def mark_completed(self):
        selected_index = task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
            return
        task_index = selected_index[0]
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        task_listbox.insert(tk.END, f"{task} (Completed)")
        self.tasks[task_index] = f"{task} (Completed)"


app = tk.Tk()
app.title("To-Do List")

# Task Entry
task_entry = tk.Entry(app, width=40, font=("Helvetica", 12))
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(app, text="Add Task", command=TodoListApp().add_task)
add_button.pack()

# Task List
task_listbox = tk.Listbox(app, width=40, height=10, font=("Helvetica", 12))
task_listbox.pack(pady=10)

# Delete Task Button
delete_button = tk.Button(app, text="Delete Task", command=TodoListApp().delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Mark Completed Button
complete_button = tk.Button(app, text="Mark Completed", command=TodoListApp().mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

# Clear List Button
clear_button = tk.Button(app, text="Clear List", command=TodoListApp().clear_list)
clear_button.pack()

app.mainloop()
