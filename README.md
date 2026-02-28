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
*   Schedule automation tasks with daily recurrence
*   Receive in-app notifications for task changes

All interactions happen seamlessly via Django templates ensuring a responsive and user-friendly experience.

* * *

**🎯 Intended Users**
---------------------

*   **Individuals** looking to organize personal tasks
*   **Teams** collaborating on shared to-do lists
*   **Project Managers** tracking task progress
*   **Developers** evaluating Django-based CRUD functionality

* * *

**📖 User Stories**
-------------------

### Visitors

1. As a visitor, I would like to see what ToDoBot offers so I can decide if it's right for me.
2. As a visitor, I would like to register an account so I can start managing my tasks.
3. As a visitor, I would like the site to be responsive so I can use it on my phone, tablet, or desktop.

### Registered Users

1. As a registered user, I would like to sign in to my account so I can access my tasks.
2. As a registered user, I would like to create a new task with a title, description, category, and scheduled time so I can track things to do.
3. As a registered user, I would like to view a list of all my tasks so I can see what needs to be done.
4. As a registered user, I would like to view the full details of a task so I can see all its information.
5. As a registered user, I would like to edit a task so I can update its details when things change.
6. As a registered user, I would like to delete a task so I can remove tasks I no longer need.
7. As a registered user, I would like to mark a task as completed so I can track my progress.
8. As a registered user, I would like to see status badges (Completed, Pending, Overdue) so I can quickly identify task states.
9. As a registered user, I would like to create automation tasks with recurrence days and times so I can schedule recurring home activities.
10. As a registered user, I would like to see if an automation task has been completed for today so I know its daily status.
11. As a registered user, I would like to receive notifications when I create, update, or delete a task so I am informed of changes.
12. As a registered user, I would like to clear all notifications so I can dismiss old alerts.
13. As a registered user, I would like to paginate through my tasks so I can browse large task lists easily.
14. As a registered user, I would like to sign out of my account so my information stays secure.

### Admin / Site Owner

1. As an admin, I would like to manage all tasks and categories via the Django admin panel so I can oversee the application.
2. As an admin, I would like task slugs to be auto-generated from titles so URLs are clean and readable.
3. As an admin, I would like to run a management command to notify users of tasks due within 12 hours so they receive timely reminders.
4. As an admin, I would like to run a management command to mark automation tasks as completed for the day so recurring tasks are tracked automatically.

* * *

**🧱 Features**
---------------

*   📝 Create, update, and delete tasks (full CRUD)
*   ✅ Mark tasks as completed or pending
*   🔍 View detailed task pages
*   🏷️ Categorise tasks (General Task, Entertainment, Appliances, Home Automation)
*   🤖 Automation tasks with daily recurrence scheduling
*   🔔 In-app notification system for task changes
*   ⏰ Management command to notify users of upcoming tasks
*   🎨 Responsive design using Bootstrap 5 and Django templates
*   📂 Custom management commands for automation
*   🔒 Secure data handling with Django's ORM and PostgreSQL
*   🔑 User authentication via django-allauth

* * *

**📁 Folder Structure**
-----------------------

    📁 todo/                    # Main Django app (models, views, forms, templates)
    📁 ToDoBot/                 # Project configuration (settings, urls, wsgi)
    📁 templates/               # Project-level templates (base, allauth overrides)
    📁 static/                  # Static files (CSS, JS, images)
    📁 staticfiles/             # Collected static files for deployment
    📁 docs/                    # Documentation and testing screenshots
    📄 manage.py                # Django CLI
    📄 requirements.txt         # Python dependencies
    📄 Procfile                 # Heroku deployment config
    📄 README.md                # Project README
    📄 TESTING.md               # Testing & validation documentation
    📄 .gitignore               # Git ignore rules

* * *

**🔍 Pages Breakdown**
----------------------

### `index.html` — Task List (Home)

Provides a list of all tasks with options to:

*   ➕ Add new task via the **Create Task** button
*   🔍 View task details via the **View Details** link
*   📊 See status badges (Completed, Pending, Overdue, Recurring, etc.)
*   📄 Paginate through tasks (6 per page)

### `task_detail.html` — Task Detail

Displays full details of a selected task:

*   Title, description, and creation date
*   Current status with badge
*   Update form to edit all task fields
*   Delete button with confirmation
*   Recurrence fields toggle for automation tasks

### `task_form.html` — Create Task

Used for creating new tasks:

*   Title, description, category, scheduled time
*   Task type selection (User Task / Home Automation)
*   Recurrence fields (time and days) for automation tasks
*   Form validation with error display

### `task_confirm_delete.html` — Delete Confirmation

Confirmation page before deleting a task:

*   Displays task title
*   Confirm or cancel deletion

### Authentication Pages

*   **Sign Up** — Register a new account
*   **Sign In** — Log in to access tasks
*   **Sign Out** — Log out with confirmation

* * *

**🧰 Technologies Used**
------------------------

*   Python 3
*   Django 5.2
*   PostgreSQL (via Neon, configured with DATABASE_URL)
*   django-allauth (authentication)
*   django-crispy-forms + crispy-bootstrap5 (form rendering)
*   django-summernote (rich text in admin)
*   django-environ (environment variable management)
*   WhiteNoise (static file serving)
*   Gunicorn (WSGI server)
*   HTML5, CSS3, JavaScript
*   Bootstrap 5
*   Font Awesome 5

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

4. **Create a `.env` file** in the project root with:

        SECRET_KEY=your-secret-key
        DEBUG=True
        DATABASE_URL=your-database-url

5. **Apply database migrations**

        python3 manage.py migrate

6. **Run the development server**

        python3 manage.py runserver

7. **Open in browser**

   Visit `http://127.0.0.1:8000/` to start using ToDoBot.

8. **Notify upcoming tasks**

        python3 manage.py notify_upcoming_tasks

   Triggers notifications for tasks due within the next 12 hours. Typically you'd schedule this with a task scheduler (e.g., Heroku Scheduler or cron), but to avoid extra dyno hours and charges on Heroku, run it manually when needed.

9. **Run automation tasks**

        python3 manage.py run_automation_tasks

   Marks automation tasks as completed for today if their scheduled recurrence time matches the current time.

* * *

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

**🧪 Testing & Validation**
---------------------------

For full testing documentation including HTML/CSS/JS/Python validation, Lighthouse audits, manual feature testing, user story testing, and bug tracking — see the dedicated **[TESTING.md](TESTING.md)** file.

* * *

**🤝 Acknowledgments**
---------------------

*   Photo assets sourced from [Unsplash](https://unsplash.com/)
*   Bootstrap 5
*   Font Awesome 5
*   Django documentation
*   Code Institute for project guidance

* * *

**📬 Contact**
--------------

Built and maintained by Christopher Quinones.  
Have questions or suggestions? Open an issue or reach out at 517996@waes.ac.uk.
