import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

# --- Database Setup ---
# Define database path


db_path = Path("ToDoDataBase.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name VARCHAR(50),
    description TEXT
)
""")
conn.commit()


# --- Functions ---
def clear_entries():
    """Clears the task name and description entry fields."""
    entry_name.delete(0, tk.END)
    entry_desc.delete(0, tk.END)


def refresh_tasks(query=None):
    """
    Refreshes the task list in the Treeview.
    Performs search if a query is provided.
    """
    # Clear current items to prevent duplication
    for row in task_list.get_children():
        task_list.delete(row)

    if query:
        # Search by Name, Description, or ID
        search_term = f"%{query}%"
        # CAST user_id to TEXT for generalized search
        cursor.execute("""
            SELECT * FROM tasks 
            WHERE task_name LIKE ? OR description LIKE ? OR CAST(user_id AS TEXT) LIKE ?
        """, (search_term, search_term, search_term))
    else:
        # Fetch all tasks
        cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    # Insert fetched tasks into the Treeview
    for r in rows:
        task_list.insert("", tk.END, values=r)


def add_task():
    """Adds a new task to the database."""
    name = entry_name.get().strip()
    desc = entry_desc.get().strip()

    if not name:
        messagebox.showerror("Error", "Task Name is required.")
        return

    cursor.execute("INSERT INTO tasks(task_name, description) VALUES (?,?)", (name, desc))
    conn.commit()
    refresh_tasks()
    messagebox.showinfo("Success", "Task added successfully.")
    clear_entries()


def delete_task():
    """Deletes the selected task from the database."""
    selected = task_list.focus()
    if not selected:
        messagebox.showerror("Error", "Select a task first!")
        return

    # Get the ID of the selected task (first element in values tuple)
    task_id = task_list.item(selected)['values'][0]
    cursor.execute("DELETE FROM tasks WHERE user_id=?", (task_id,))
    conn.commit()
    refresh_tasks()
    messagebox.showinfo("Deleted", "Task deleted successfully.")
    clear_entries()


def update_task():
    """Updates the selected task's details in the database."""
    selected = task_list.focus()
    if not selected:
        messagebox.showerror("Error", "Select a task first!")
        return

    task_id = task_list.item(selected)['values'][0]
    new_name = entry_name.get().strip()
    new_desc = entry_desc.get().strip()

    if not new_name:
        messagebox.showerror("Error", "Task Name cannot be empty.")
        return

    cursor.execute("UPDATE tasks SET task_name=?, description=? WHERE user_id=?", (new_name, new_desc, task_id))
    conn.commit()
    refresh_tasks()
    messagebox.showinfo("Updated", "Task updated successfully.")
    clear_entries()


def search_tasks():
    """Executes the search based on the content of the search field."""
    search_term = entry_search.get().strip()
    refresh_tasks(query=search_term)


def on_task_select(event):
    """Populates entry fields with the selected task's data."""
    selected = task_list.focus()
    if not selected:
        return

    # Get the values (ID, Name, Description)
    values = task_list.item(selected, 'values')

    # Clear and insert Name and Description into entries
    clear_entries()

    # values[1] is Task Name, values[2] is Description
    entry_name.insert(0, values[1])
    entry_desc.insert(0, values[2])


# --- UI Setup ---
root = tk.Tk()
root.title("TODO Manager")
root.geometry("650x500")
root.configure(bg="#f4f4f4")

# Inputs Frame
frame_inputs = tk.Frame(root, bg="#f4f4f4")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Task Name:", bg="#f4f4f4", font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky="w")
entry_name = tk.Entry(frame_inputs, width=30)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Description:", bg="#f4f4f4", font=("Arial", 12)).grid(row=1, column=0, padx=5, sticky="w")
entry_desc = tk.Entry(frame_inputs, width=30)
entry_desc.grid(row=1, column=1, padx=5)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#f4f4f4")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add", width=12, command=add_task, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=8)
tk.Button(frame_buttons, text="Update", width=12, command=update_task, bg="#2196F3", fg="white").grid(row=0, column=1,
                                                                                                      padx=8)
tk.Button(frame_buttons, text="Delete", width=12, command=delete_task, bg="#F44336", fg="white").grid(row=0, column=2,
                                                                                                      padx=8)

# --- Search Section ---
frame_search = tk.Frame(root, bg="#f4f4f4")
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search (ID/Name/Desc):", bg="#f4f4f4", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_search = tk.Entry(frame_search, width=35)
entry_search.grid(row=0, column=1, padx=5)
tk.Button(frame_search, text="Search", width=8, command=search_tasks, bg="#FFC107").grid(row=0, column=2, padx=5)
tk.Button(frame_search, text="View All", width=10, command=lambda: refresh_tasks(None), bg="#9E9E9E").grid(row=0,
                                                                                                           column=3,
                                                                                                           padx=5)

# Tasks Table
cols = ("ID", "Task", "Description")
task_list = ttk.Treeview(root, columns=cols, show="headings", height=12)

# Column Formatting
task_list.column("ID", width=50, anchor=tk.CENTER)
task_list.column("Task", width=180, anchor=tk.W)
task_list.column("Description", width=380, anchor=tk.W)

task_list.heading("ID", text="ID")
task_list.heading("Task", text="Task Name")
task_list.heading("Description", text="Task Description")

task_list.pack(pady=10, padx=10, fill=tk.X)

# Bind the selection event to the function
task_list.bind("<<TreeviewSelect>>", on_task_select)

# Load tasks on startup
refresh_tasks()
root.mainloop()

# Closing database connection 
conn.close()
