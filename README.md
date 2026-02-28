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

For full testing documentation including HTML/CSS/JS/Python validation, Lighthouse audits, and bug tracking — see the dedicated **[TESTING.md](TESTING.md)** file.

### Manual Feature Testing

**Test Group** | **Test Label** | **Action** | **Expected Outcome** | **Outcome**
--- | --- | --- | --- | ---
**Navigation/UX** | Logo home link | From any page, click the ToDoBot logo in the header. | The user will be taken back to the home page. | PASS
 | Home nav link | From any page, click the Home link in the navbar. | The user will be taken to the task list (home) page. | PASS
 | Home link active state | Visit the home page and check the Home nav link. | The Home link appears highlighted/active. | PASS
 | Register link (logged out) | From any page whilst logged out, click the Register link in the navbar. | The user will be taken to the sign up page. | PASS
 | Login link (logged out) | From any page whilst logged out, click the Login link in the navbar. | The user will be taken to the sign in page. | PASS
 | Logout link (logged in) | From any page whilst logged in, click the Logout link in the navbar. | The user will be taken to the sign out confirmation page. | PASS
 | Auth links visibility (logged in) | Log in and check the navbar. | Register and Login links are hidden; Logout link is shown. | PASS
 | Auth links visibility (logged out) | Log out and check the navbar. | Logout link is hidden; Register and Login links are shown. | PASS
 | Navbar toggler (mobile) | On a small screen, click the hamburger menu icon. | The navbar menu expands and collapses. | PASS
 | Navbar slogan | From any page, view the navbar text. | "ORGANIZE YOUR TASKS EFFECIENTLY" is displayed on the right side. | PASS
 | Logged-in indicator | Log in and check the top-right area below the navbar. | "You are logged in as [username]" is displayed. | PASS
 | Logged-out indicator | Log out and check the top-right area below the navbar. | "You are not logged in" is displayed. | PASS
 | Footer copyright | From any page, scroll to the footer. | "© ToDoBot" is displayed. | PASS
 | Footer tagline | From any page, scroll to the footer. | "Stay productive!" with a tasks icon is displayed. | PASS
 | Footer position | Visit a page with minimal content. | The footer stays at the bottom of the viewport. | PASS
**Authentication** | Register | Visit the sign up form and create a new account with valid data. | The account is created and the user is logged in and redirected to the home page. | PASS
 | Register with existing username | Attempt to register with a username that already exists. | An error message is displayed and the form is not submitted. | PASS
 | Register with mismatched passwords | Attempt to register with two different passwords. | An error message is displayed and the form is not submitted. | PASS
 | Register with empty fields | Attempt to submit the sign up form with required fields empty. | Browser validation prevents submission and prompts the user. | PASS
 | Sign in | Sign in with valid credentials. | The user is logged in and redirected to the home page. | PASS
 | Sign in with invalid credentials | Attempt to sign in with incorrect username or password. | An error message is displayed and the user is not logged in. | PASS
 | Sign in with empty fields | Attempt to submit the sign in form with fields empty. | Browser validation prevents submission and prompts the user. | PASS
 | Sign out | Click Logout in the navbar, then click the Sign Out button. | The user is logged out and redirected to the home page. | PASS
 | Sign out cancel | Click Logout in the navbar, then click the Cancel button. | The user is returned to the home page and remains logged in. | PASS
 | Protected page — create task | Attempt to visit `/create/` without being logged in. | The user is redirected to the sign in page. | PASS
 | Protected page — task detail | Attempt to visit a task detail URL without being logged in. | The user is redirected to the sign in page. | PASS
 | Protected page — other user's task | Attempt to visit another user's task detail by slug whilst logged in. | A 404 page is returned (tasks are filtered by user). | PASS
**Task List (Home)** | Task cards displayed | Log in with tasks created and visit the home page. | All of the user's tasks are displayed as cards with title, description, due date, and status. | PASS
 | Empty task list | Log in with no tasks created and visit the home page. | An info alert reading "No tasks found. Add a new task to get started!" is displayed. | PASS
 | Create Task button | From the home page whilst logged in, click the Create Task button. | The user is taken to the create task form. | PASS
 | Create Task button hidden | Visit the home page whilst logged out. | The Create Task button is not shown. | PASS
 | View Details link | From the home page, click the View Details link on a task card. | The user is taken to the task detail page for that task. | PASS
 | Status badge — Completed | View a user task that has been marked as completed. | A green "Completed" badge is shown on the card. | PASS
 | Status badge — Pending | View a user task that is not completed and not overdue. | A yellow "Pending" badge is shown on the card. | PASS
 | Status badge — Overdue | View a user task with a scheduled time in the past that is not completed. | A red "Overdue" badge is shown on the card. | PASS
 | Status badge — Recurring | View an automation task with recurrence days set. | A blue "Recurring" badge is shown on the card. | PASS
 | Status badge — Completed for today | View an automation task that has been completed for today. | A green "Completed for today" badge is shown. | PASS
 | Status badge — Pending for today | View an automation task due today that has not yet been completed. | A yellow "Pending for today" badge is shown. | PASS
 | Status badge — Not scheduled | View an automation task not scheduled for today. | A grey "Not scheduled for today" badge is shown. | PASS
 | Task ordering | View the task list with multiple tasks. | Tasks are ordered by most recently created first. | PASS
 | Card layout (desktop) | View the task list on a desktop screen. | Tasks are displayed in a 3-column grid layout. | PASS
 | Card layout (mobile) | View the task list on a mobile screen. | Tasks stack vertically in a single column. | PASS
 | Pagination controls | Add more than 6 tasks and visit the home page. | Pagination controls (PREV / NEXT) appear below the task list. | PASS
 | Pagination — NEXT | On page 1 with more pages available, click NEXT. | The user is taken to the next page of tasks. | PASS
 | Pagination — PREV | On page 2, click PREV. | The user is taken to the previous page of tasks. | PASS
 | Pagination — page indicator | View the pagination area. | "Page X of Y" is displayed between the navigation buttons. | PASS
**Create Task** | Create task form display | Click Create Task from the home page. | The form displays fields for title, description, category, scheduled time, task type, and recurrence. | PASS
 | Is completed field hidden | View the create task form. | The "Is completed" checkbox is not shown on the creation form. | PASS
 | Create with valid data | Fill in all fields with valid data and click Create. | The task is created and the user is redirected to the task detail page. | PASS
 | Create with duplicate title | Attempt to create a task with a title that already exists. | An error message is displayed ("Task with this Title already exists"). | PASS
 | Create with empty title | Attempt to submit the form with the title field empty. | Browser validation prevents submission. | PASS
 | Create with empty description | Submit the form with a valid title but no description. | The task is created successfully with a blank description. | PASS
 | Category dropdown | Select a category from the dropdown and submit. | The selected category is saved to the task. | PASS
 | Scheduled time picker | Select a date and time using the datetime picker and submit. | The scheduled time is saved to the task. | PASS
 | Task type — User Task | Select "User Task" from the task type dropdown. | Recurrence fields (time and days) are hidden. | PASS
 | Task type — Home Automation | Select "Home Automation" from the task type dropdown. | Recurrence fields (time and days) are shown. | PASS
 | Category → Task type sync (automation) | Select "Appliances" or "Home Automation" from the category dropdown. | The task type is automatically set to "Home Automation". | PASS
 | Category → Task type sync (user) | Select "Entertainment" or "General Task" from the category dropdown. | The task type is automatically set to "User Task". | PASS
 | Recurrence time | Enter a time (e.g. 08:00) in the recurrence time field. | The recurrence time is saved to the task. | PASS
 | Recurrence days | Enter days (e.g. "mon,wed,fri") in the recurrence days field. | The recurrence days are saved to the task. | PASS
 | Slug auto-generation | Create a task with the title "My New Task". | The slug is auto-generated as "my-new-task". | PASS
 | Notification on create | Create a task successfully. | A notification is created: "Task '[title]' was created." | PASS
 | Back to Task List link | Click the "Back to Task List" link on the create form. | The user is returned to the home page. | PASS
**Task Detail & Edit** | Masthead display | Visit a task detail page. | The masthead shows the task title, author, creation date, description, and status badge. | PASS
 | Scheduled time shown | View a task that has a scheduled time set. | The scheduled date and time are displayed in the masthead. | PASS
 | Scheduled time hidden | View a task that has no scheduled time. | The scheduled time section is not displayed. | PASS
 | Status badges on detail | View task detail for tasks in different states. | The correct badge is shown (Completed, Pending, Overdue, Recurring, etc.). | PASS
 | Update form displayed (logged in) | Visit a task detail page whilst logged in. | The update form is displayed with all fields pre-populated with the task's current data. | PASS
 | Update form hidden (logged out) | Visit a task detail page whilst logged out. | A message reading "Log in to update this task." is shown instead of the form. | PASS
 | Is completed shown (user task) | View the edit form for a user task. | The "Is completed" checkbox is visible. | PASS
 | Is completed hidden (automation) | View the edit form for an automation task. | The "Is completed" checkbox is not shown. | PASS
 | Edit title | Change the title field and click Update. | The task title is updated. | PASS
 | Edit description | Change the description field and click Update. | The task description is updated. | PASS
 | Edit category | Change the category and click Update. | The task category is updated. | PASS
 | Edit scheduled time | Change the scheduled time and click Update. | The task scheduled time is updated. | PASS
 | Task type toggle to automation | Switch the task type to "Home Automation". | Recurrence fields appear in the form. | PASS
 | Task type toggle to user | Switch the task type to "User Task". | Recurrence fields are hidden in the form. | PASS
 | Update button | Click Update with valid data. | The task is updated and the page refreshes with the updated data. | PASS
 | Notification on update | Update a task successfully. | A notification is created: "Task '[title]' was updated." | PASS
 | Delete Task button | Click the Delete Task button on the detail page. | The user is taken to the delete confirmation page. | PASS
**Delete Task** | Confirmation message | Visit the delete confirmation page. | The message "Are you sure you want to delete the task: [title]?" is displayed. | PASS
 | Confirm delete | Click the "Yes, delete" button. | The task is deleted and the user is redirected to the home page. | PASS
 | Cancel delete | Click the "Cancel" button. | The user is returned to the task detail page and the task is not deleted. | PASS
 | Notification on delete | Delete a task successfully. | A notification is created: "Task '[title]' was deleted." | PASS
**Notifications** | Notification panel appears | Perform a task action (create, update, or delete). | The notification panel appears at the top-right with the notification message. | PASS
 | Notification auto-hide | Wait 3 seconds after the notification panel appears. | The panel automatically hides. | PASS
 | Notification bell click | Click the notification bell icon after the panel has auto-hidden. | The notification panel reappears. | PASS
 | Notification bell hidden | View the navbar when there are no notifications. | The bell icon is not displayed. | PASS
 | Close button (X) | Click the X button on the notification panel. | The notification panel closes. | PASS
 | Clear All button | Click the "Clear All" button on the notification panel. | All notifications are deleted and the panel closes. | PASS
 | Clear All persistence | Click "Clear All", then refresh the page. | Notifications remain cleared (deleted from the database). | PASS
 | Notification content | View a notification in the panel. | The notification shows the action message and a timestamp. | PASS
 | Unread highlight | View unread notifications in the panel. | Unread notifications are highlighted with a warning background colour. | PASS
 | Multiple notifications | Perform several task actions. | Up to 10 of the most recent notifications are shown in the panel. | PASS
**Management Commands** | Notify upcoming tasks | Run `python3 manage.py notify_upcoming_tasks` with tasks due within 12 hours. | Notifications are created for each due task. | PASS
 | Notify — no tasks due | Run `python3 manage.py notify_upcoming_tasks` with no tasks due soon. | "No upcoming tasks to notify." is displayed. | PASS
 | Notify — duplicate prevention | Run `notify_upcoming_tasks` twice within 1 hour for the same task. | A duplicate notification is not created. | PASS
 | Run automation tasks | Run `python3 manage.py run_automation_tasks` when an automation task matches the current day and time. | The task is marked as completed for today. | PASS
 | Run automation — no match | Run `run_automation_tasks` when no tasks match the current time. | "No automation tasks to run at this time." is displayed. | PASS
 | Run automation — already completed | Run `run_automation_tasks` twice on the same day for the same task. | The task is not marked as completed again (already done for today). | PASS
**Admin** | Admin login | Navigate to `/admin/` and sign in as a superuser. | The Django admin dashboard is displayed. | PASS
 | Task list in admin | View the Task list in the admin panel. | Tasks are listed showing title, user, category, is_completed, slug, task_type, recurrence_time, recurrence_days. | PASS
 | Task search in admin | Search for a task by title, description, or slug. | Matching tasks are displayed. | PASS
 | Task edit in admin | Edit a task in the admin panel. | All fields are editable and the slug is auto-populated from the title. | PASS
 | Summernote editor | Edit a task description in the admin panel. | The Summernote rich text editor is displayed for the description field. | PASS
 | Category list in admin | View the Category list in the admin panel. | All categories are listed. | PASS
 | Add category in admin | Add a new category in the admin panel. | The category is created successfully. | PASS
**Responsive Design** | Mobile navbar | View the site on a screen smaller than 992px. | The navbar collapses to a hamburger menu. | PASS
 | Mobile task cards | View the task list on a mobile screen. | Task cards stack vertically in a single column. | PASS
 | Mobile forms | View the create/edit task form on a mobile screen. | Form fields are full width and stack vertically. | PASS
 | Mobile footer | View the footer on a mobile screen. | Footer text is centred and readable. | PASS
 | Tablet task cards | View the task list on a tablet screen (576px–992px). | Task cards display in 1–2 columns. | PASS
 | Desktop navbar | View the site on a screen wider than 992px. | The full horizontal navbar is displayed. | PASS
 | Desktop task cards | View the task list on a desktop screen. | Task cards display in a 3-column grid. | PASS
 | Desktop forms | View the create/edit task form on a desktop screen. | The form is centred with a max-width container. | PASS

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
