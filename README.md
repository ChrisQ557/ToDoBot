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
*   🔒 Secure data handling with Django's ORM and PostgreSQL (configured via the DATABASE_URL environment variable)

* * *

**📁 Folder Structure**
-----------------------

    📁 todo/                    # Main Django app
    📁 ToDoBot/                 # Project configuration
    📁 templates/               # Project-level templates
    📁 staticfiles/             # Collected static files
    📄 manage.py                # Django CLI
    📄 requirements.txt         # Python dependencies
    📄 README.md                # Project README
    📄 .gitignore               # Git ignore rules

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
        source venv/bin/activate    # Windows: venv\Scripts\activate

3. **Install dependencies**

        pip install -r requirements.txt

4. **Apply database migrations**

        python3 manage.py migrate

5. **Run the development server**

        python3 manage.py runserver

6. **Open in browser**

   Visit `http://127.0.0.1:8000/` to start using ToDoBot.

7. **Notify upcoming tasks**

        python3 manage.py notify_upcoming_tasks

   Triggers notifications for tasks due within the next 12 hours. Typically you'd schedule this with a task scheduler (e.g., Heroku Scheduler or cron), but to avoid extra dyno hours and charges on Heroku, run it manually when needed.



**📦 Exporting Data for Assessment**
-------------------------------

To share your database contents without including the raw database file, you can export Django fixtures in JSON format:

    # Export only the todo app's data
    python3 manage.py dumpdata todo --indent 2 > todo_data.json

    # Or export the entire database
    python3 manage.py dumpdata --indent 2 > full_data.json

Share the generated JSON file (`todo_data.json` or `full_data.json`) with your assessor for evaluation.

* * *

**🛠️ Environment & Admin**
--------------------------

To create a Django superuser for accessing the admin interface:

```bash
python3 manage.py createsuperuser
```

* * *

**🤝 Acknowledgments**
---------------------

* Photo assets sourced from Unsplash.

* * *

**📬 Contact**
--------------

Built and maintained by Christopher Quinones.  
Have questions or suggestions? Open an issue or reach out at 517996@waes.ac.uk.