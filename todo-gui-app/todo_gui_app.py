import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

# --- Database Setup ---
db_path = Path("ToDoDataBase.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name VARCHAR(20),
    description TEXT
)
""")
conn.commit()

# --- Functions ---
def refresh_tasks():
    for row in task_list.get_children():
        task_list.delete(row)

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    for r in rows:
        task_list.insert("", tk.END, values=r)


def add_task():
    name = entry_name.get().strip()
    desc = entry_desc.get().strip()

    if not name:
        messagebox.showerror("Error", "Task name is required")
        return

    cursor.execute("INSERT INTO tasks(task_name, description) VALUES (?,?)", (name, desc))
    conn.commit()
    refresh_tasks()
    messagebox.showinfo("Success", "Task added")


def delete_task():
    selected = task_list.focus()
    if not selected:
        messagebox.showerror("Error", "Select a task first!")
        return

    task_id = task_list.item(selected)['values'][0]
    cursor.execute("DELETE FROM tasks WHERE user_id=?", (task_id,))
    conn.commit()
    refresh_tasks()
    messagebox.showinfo("Deleted", "Task deleted")


def update_task():
    selected = task_list.focus()
    if not selected:
        messagebox.showerror("Error", "Select a task first!")
        return

    task_id = task_list.item(selected)['values'][0]
    new_name = entry_name.get().strip()
    new_desc = entry_desc.get().strip()

    if not new_name:
        messagebox.showerror("Error", "Task name cannot be empty")
        return

    cursor.execute("UPDATE tasks SET task_name=?, description=? WHERE user_id=?", (new_name, new_desc, task_id))
    conn.commit()
    refresh_tasks()
    messagebox.showinfo("Updated", "Task updated successfully")


# --- UI Setup ---

def search_task():
    keyword = entry_search.get().strip()
    if not keyword:
        refresh_tasks()
        return

    for row in task_list.get_children():
        task_list.delete(row)

    cursor.execute("SELECT * FROM tasks WHERE task_name LIKE ?", (f"%{keyword}%",))
    rows = cursor.fetchall()

    if not rows:
        messagebox.showinfo("Not Found", "No task found with this name")
        return

    for r in rows:
        task_list.insert("", tk.END, values=r)
        task_list.insert("", tk.END, values=r)


root = tk.Tk()
root.title("TODO Manager")
root.geometry("600x450")
root.configure(bg="#f4f4f4")

# Search Frame
frame_search = tk.Frame(root, bg="#f4f4f4")
frame_search.pack(pady=5)

tk.Label(frame_search, text="Search by ID", bg="#f4f4f4", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_search = tk.Entry(frame_search, width=15)
entry_search.grid(row=0, column=1, padx=5)

tk.Button(frame_search, text="Search", width=10, command=search_task).grid(row=0, column=2, padx=5)

# Inputs Frame
frame_inputs = tk.Frame(root, bg="#f4f4f4")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Task Name", bg="#f4f4f4", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_name = tk.Entry(frame_inputs, width=25)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Description", bg="#f4f4f4", font=("Arial", 12)).grid(row=1, column=0, padx=5)
entry_desc = tk.Entry(frame_inputs, width=25)
entry_desc.grid(row=1, column=1, padx=5)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#f4f4f4")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update", width=10, command=update_task).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete", width=10, command=delete_task).grid(row=0, column=2, padx=5)

# Tasks Table
cols = ("ID", "Task", "Description")
task_list = ttk.Treeview(root, columns=cols, show="headings", height=12)

for col in cols:
    task_list.heading(col, text=col)
    task_list.column(col, width=150)

task_list.pack(pady=10)

refresh_tasks()
root.mainloop()
