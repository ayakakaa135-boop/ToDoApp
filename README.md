[todo_readme.md](https://github.com/user-attachments/files/23563124/todo_readme.md)
# TODO Manager (GUI + SQLite)

Simple task manager app built with **Python**, **Tkinter**, and **SQLite**.
The app lets users:
- Add tasks
- Update tasks
- Delete tasks
- Search tasks by name
- View all tasks in a clean GUI

## Features
- Lightweight and fast
- Local SQLite database (no setup needed)
- Elegant and simple GUI
- Search functionality (partial match supported)
- Auto-refresh task list after every action

## Requirements
- Python 3.10+
- No external libraries needed (Tkinter + SQLite are built‑in)

## How to Run
1. Clone the repository:
```
git clone https://github.com/yourusername/todo-gui-app.git
```
2. Open the folder:
```
cd todo-gui-app
```
3. Run the app:
```
python app.py
```

A local database file named **ToDoDataBase.db** will be created automatically if it doesn't exist.

## Project Structure
```
📂 todo-gui-app
│── app.py               # Main application (GUI + logic)
│── ToDoDataBase.db      # SQLite DB (auto-created)
│── README.md            # Project documentation
```

## Screenshots
(You can add these later after you take screenshots of your GUI)
```
📸 ui_home.png       # Main interface
📸 ui_search.png     # Search example
📸 ui_edit.png       # Edit popup
```

## GitHub Repository Description
A simple Python GUI Todo App using Tkinter and SQLite. Supports adding, updating, deleting, and searching tasks with a clean interface.

## .gitignore
Add this file to avoid committing local DB files:
```
# Ignore SQLite database
*.db
__pycache__/
*.pyc
```

## Recommended Commit Messages
- "Initialize project structure and main app"
- "Add GUI layout and database setup"
- "Implement CRUD operations"
- "Add search by name feature"
- "Clean code and update README"

## Notes
- You can safely upload this project to GitHub.
- No sensitive information is stored or required.
- The database path is relative so the app works on any machine.

## License
This project is free to use and modify.

