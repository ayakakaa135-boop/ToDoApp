# ToDo Manager Application 📋

A simple ToDo list management application built with **Python**, **Tkinter** for the graphical user interface, and **SQLite** for database storage.

## ✨ Features

* **Add Tasks:** Easily add new tasks with a name and description.
* **View Tasks:** Display all tasks in a clear, tabular view.
* **Update Tasks:** Select a task from the list, modify its details in the input fields, and save the changes.
* **Delete Tasks:** Remove completed or unwanted tasks from the list.
* **Search Functionality:** Search tasks by Task Name, Description, or their unique ID.
* **Database Persistence:** All tasks are saved to a local SQLite database file.
* **Arabic Interface:** The user interface elements (buttons, labels) are displayed in Arabic for user convenience.

## 🚀 Getting Started

### Prerequisites

You need to have **Python 3.x** installed. Tkinter is usually included with standard Python installations.

### Installation and Setup

1.  **Clone the repository** (if hosted, otherwise save the code above as a Python file, e.g., `todo_app.py`).

2.  **Run the application** from your terminal:

    ```bash
    python todo_app.py
    ```

3.  The application will automatically create the SQLite database file named `ToDoDataBase.db` in the specified path:
    
    > **Note:** Make sure to adjust the `db_path` variable in the Python file to a path relevant to your machine, or simply use `db_path = Path("ToDoDataBase.db")` to create the file in the same directory as the script.

## 🛠 Project Structure

* `todo_app.py`: The main Python script containing the application logic (GUI, SQLite connection, and CRUD functions).
* `ToDoDataBase.db`: The SQLite database file where tasks are stored (automatically generated on first run).

## 💡 How to Use

1.  **Adding a Task:** Enter the **اسم المهمة** (Task Name) and **الوصف** (Description) and click the **إضافة** (Add) button.
2.  **Viewing/Selecting:** Click any row in the table to display its details in the input fields.
3.  **Updating a Task:** Select a task, edit the text in the input fields, and click the **تحديث** (Update) button.
4.  **Searching:** Use the search bar to filter tasks by ID, Name, or Description. Click **عرض الكل** (View All) to reset the search.

---
