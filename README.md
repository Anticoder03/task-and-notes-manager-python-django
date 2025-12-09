

# 📝 Notes & Tasks Manager  
A clean and modern productivity web app built using **Django**, **Tailwind CSS**, and **Font Awesome**, allowing users to manage their personal notes and daily tasks in one simple dashboard.

---

## 🚀 Features

### ✅ Notes Module
- Add new notes  
- View all notes  
- Edit notes  
- Delete notes  
- Neat card layout with Tailwind UI  
- Timestamp for each note  

### ✅ Tasks Module
- Add tasks with due date  
- View all tasks (Pending/Done)  
- Mark tasks as completed  
- Edit tasks  
- Delete tasks  
- Status badges for quick visibility  

### ✅ Dashboard
- Total notes count  
- Total tasks count  
- Pending vs Completed tasks  
- Quick actions (Add Note / Add Task)  
- Latest notes & latest tasks section  
- Greeting based on time  
- Fully responsive UI  

### ✅ Authentication
- Login required for adding/viewing notes & tasks  
- Each user can only see their own data  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Django** | Backend framework |
| **SQLite / MySQL (optional)** | Database |
| **Tailwind CSS CDN** | Styling |
| **Font Awesome** | Icons |
| **Python 3** | Core runtime |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Project

```bash
git clone https://github.com/Anticoder03/task-and-notes-manager-python-django.git
cd task-and-notes-manager-python-django
````

### 2️⃣ Create Virtual Environment (Optional but recommended)

```bash
python -m venv env
env\Scripts\activate   # for Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Server

```bash
python manage.py runserver
```

### 7️⃣ Visit App

```
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

```
myproject/
│── manage.py
│── myproject/
│   │── urls.py
│   │── settings.py
│
└── core/
    │── views.py
    │── models.py
    │── urls.py (optional)
    │── templates/
        │── index.html
        │── add_note.html
        │── view_notes.html
        │── add_task.html
        │── view_tasks.html
```

---

## ✨ UI Highlights

* Tailwind-based dashboard
* Beautiful cards for notes & tasks
* Icons everywhere using Font Awesome
* Fully responsive
* Minimal, clean, and modern UI

---

## 🔮 Future Enhancements (Optional Ideas)

* Add categories for notes
* Add task reminders via email
* Add dark mode
* Add search filters
* Add tags for notes
* Convert to REST API using Django REST Framework
* Build a React frontend for this backend

---

## 🤝 Contributing

Pull requests are welcome!
Fork the repository → make changes → open a PR.

---

## 📄 License

This project is open-source and free to use under the **MIT License**.

---

## 👨‍💻 Developer

**Ashish Prajapati**
Aka **Anticoder03**
Loves coding, anime, and crafting clean UI 🔥

GitHub: [https://github.com/Anticoder03](https://github.com/Anticoder03)
