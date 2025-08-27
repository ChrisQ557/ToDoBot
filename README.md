**📝 ToDoBot**
========================

Effortless task management powered by Django. ToDoBot lets you create, edit, track, and complete tasks through a clean web interface.

* * *

**🌟 Overview**
---------------

ToDoBot is a Django-based web application for managing your to-do tasks with ease. It provides a simple yet powerful interface to:

*   Add new tasks with titles and descriptions
*   Edit existing tasks
*   Mark tasks as completed or pending
*   View task details
*   Delete tasks when no longer needed

All interactions happen seamlessly via Django templates ensuring a responsive and user-friendly experience.

* * *

**🎯 Intended Users**
---------------------

*   **Individuals** looking to organize personal tasks
*   **Teams** collaborating on shared to-do lists
*   **Project Managers** tracking task progress
*   **Developers** evaluating Django-based CRUD functionality

* * *

**🧱 Features**
---------------

*   📝 Create, update, and delete tasks
*   ✅ Mark tasks as completed or pending
*   🔍 View detailed task pages
*   🎨 Responsive design using Django templates
*   📂 Custom management commands for automation
*   🔒 Secure data handling with Django's ORM and SQLite

* * *

**📁 Folder Structure**
-----------------------

    📁 ToDoBot/
    ├── 📂 todo/                    # Main Django app
    │   ├── 📂 migrations/          # Database migrations
    │   ├── 📂 management/commands/ # Custom management commands
    │   ├── 📂 templates/todo/      # HTML templates
    │   ├── 📂 staticfiles/         # Static assets (CSS, JS)
    │   ├── models.py              # Task model definition
    │   ├── views.py               # View functions
    │   └── urls.py                # App routes
    ├── 📂 ToDoBot/                 # Project configuration
    │   ├── settings.py            # Django settings
    │   ├── urls.py                # Root URL configurations
    │   └── wsgi.py                # WSGI entry point
    ├── 📄 manage.py               # Django CLI
    ├── 📄 requirements.txt        # Python dependencies
    └── 📄 README.md               # Project README

* * *

**🔍 Pages Breakdown**
----------------------

`index.html`
------------

Provides a list of all tasks with options to:

*   ➕ Add new task via the **`Add Task`** button
*   🔍 View task details via the **`View Details`** link


`task_detail.html`
------------------

Displays full details of a selected task:

*   Title and description
*   Current status
*   Actions to edit or delete task

`task_form.html`
----------------

Used for both creating and updating tasks:

*   Title (`<input type="text">`)
*   Description (`<textarea>`)
*   Submit button: **Save Task**

* * *

**🧰 Technologies Used**
------------------------

*   Python 3
*   Django Web Framework
*   PostgreSQL (configured via the DATABASE_URL environment variable)
*   HTML5, CSS3 (Django templates)
*   Bootstrap 4 (optional for styling)

* * *

**🌐 How to Use**
-----------------

1. **Clone the repository**

        git clone https://github.com/ChrisQ557/ToDoBot.git

2. **Create and activate a virtual environment**

        python3 -m venv venv
        source venv/bin/activate    # Windows: venv\\Scripts\\activate

3. **Install dependencies**

        pip install -r requirements.txt

4. **Apply database migrations**

        python3 manage.py migrate

5. **Run the development server**

        python3 manage.py runserver

6. **Open in browser**

   Visit `http://127.0.0.1:8000/` to start using ToDoBot.

**🛠️ Environment & Admin**
--------------------------

To create a Django superuser for accessing the admin interface:

```bash
python3 manage.py createsuperuser
```

* * *

**📬 Contact**
--------------

Built and maintained by Christopher Quinones.  
Have questions or suggestions? Open an issue or reach out at 517996@waes.ac.uk.