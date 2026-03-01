# ToDoBot Database Data Dictionary

## Table Reference

### Table: todo_task
**Purpose**: Core task management table storing user tasks and home automation tasks.
**Related Tables**: References auth_user (M:1), todo_category (M:1)

| Column Name | Data Type | Null? | Default | Constraints | Description |
|---|---|---|---|---|---|
| id | BIGINT | No | AUTO-INCREMENT | PRIMARY KEY | Unique identifier for each task |
| user_id | INTEGER | No | - | FK→auth_user(id) ON DELETE CASCADE | The user who created/owns this task |
| category_id | BIGINT | Yes | NULL | FK→todo_category(id) ON DELETE SET NULL | Optional task category for organization |
| title | VARCHAR(255) | No | - | UNIQUE | Task title/name (must be unique) |
| description | TEXT | No | Empty String | - | Detailed task description or instructions |
| slug | VARCHAR(200) | Yes | NULL | UNIQUE | URL-safe slug derived from title |
| task_type | VARCHAR(20) | No | 'user' | - | Task classification: 'user' (one-time) or 'automation' (recurring) |
| scheduled_time | TIMESTAMP WITH TZ | Yes | NULL | - | When the task is scheduled to be due (user tasks only) |
| is_completed | BOOLEAN | No | FALSE | - | Completion status: TRUE when task is done |
| recurrence_time | TIME | Yes | NULL | - | Daily time for automation task execution (e.g., 09:30:00) |
| recurrence_days | VARCHAR(20) | Yes | NULL | - | Comma-separated days for execution (e.g., 'mon,tue,wed,fri') |
| last_completed_date | DATE | Yes | NULL | - | Most recent date automation task was marked complete |
| created_at | TIMESTAMP WITH TZ | No | NOW() | - | Record creation timestamp (UTC) |
| updated_at | TIMESTAMP WITH TZ | No | NOW() | - | Record last update timestamp (UTC) |

**Indexes**:
- todo_task_user_id_69f329a5 (user_id) - Speed up user lookups
- todo_task_category_id_fb0c0926 (category_id) - Speed up category filtering
- todo_task_slug_e7a5bf53_like (slug) - Support slug-based lookups
- todo_task_title_fe9014fc_like (title) - Support title searches

**Example Data**:
```
id | user_id | title | description | task_type | scheduled_time | is_completed
---|---------|-------|-------------|-----------|----------------|---------------
1  | 1       | "Grocery Shopping" | "Buy milk, eggs, bread" | user | 2025-03-05 15:00:00+00 | FALSE
2  | 1       | "Morning Exercise" | "30 min jog" | automation | NULL | FALSE
3  | 2       | "Project Report" | "Q1 status report" | user | 2025-03-03 17:00:00+00 | TRUE
```

---

### Table: todo_category
**Purpose**: Stores task categories for organizing tasks.
**Related Tables**: Referenced by todo_task (1:M)

| Column Name | Data Type | Null? | Default | Constraints | Description |
|---|---|---|---|---|---|
| id | BIGINT | No | AUTO-INCREMENT | PRIMARY KEY | Unique category identifier |
| name | VARCHAR(100) | No | - | UNIQUE | Category name (must be unique) |

**Indexes**:
- todo_category_name_124c74fd_like (name) - Support category name searches

**Example Data**:
```
id | name
---|---
1  | "Personal"
2  | "Work"
3  | "Home Maintenance"
4  | "Shopping"
```

---

### Table: todo_notification
**Purpose**: Stores notifications for users (e.g., task reminders, alerts).
**Related Tables**: References auth_user (M:1)

| Column Name | Data Type | Null? | Default | Constraints | Description |
|---|---|---|---|---|---|
| id | BIGINT | No | AUTO-INCREMENT | PRIMARY KEY | Unique notification identifier |
| user_id | INTEGER | No | - | FK→auth_user(id) ON DELETE CASCADE | User receiving the notification |
| message | VARCHAR(255) | No | - | - | Notification content/text (max 255 chars) |
| is_read | BOOLEAN | No | FALSE | - | Read status: TRUE if user has seen it |
| created_at | TIMESTAMP WITH TZ | No | NOW() | - | When notification was created (UTC) |

**Indexes**:
- todo_notification_user_id_d5944080 (user_id) - Retrieve user's notifications

**Example Data**:
```
id | user_id | message | is_read | created_at
---|---------|---------|---------|---
1  | 1       | "Task 'Grocery Shopping' is due in 1 hour" | TRUE | 2025-03-05 14:00:00+00
2  | 1       | "Task 'Morning Exercise' is pending" | FALSE | 2025-03-05 07:30:00+00
```

---

## User's Auth Table (Reference)
**Table**: auth_user (Django built-in)
**Purpose**: Stores user authentication and profile data
**Relevant Fields**:
- id (INTEGER) - User ID referenced by tasks and notifications
- username (VARCHAR) - User login name
- email (VARCHAR) - User's email address
- is_active (BOOLEAN) - Account active status
- date_joined (TIMESTAMP) - Account creation date

---

## Field Type Specifications

### Temporal Fields

**DateTimeField** (TIMESTAMP WITH TIME ZONE):
- Stores both date and time
- Timezone-aware (UTC)
- Used for: created_at, updated_at, scheduled_time
- Format: 2025-03-05 14:30:45.123456+00:00
- Range: Year 1 to Year 9999

**DateField** (DATE):
- Stores date only (no time component)
- Used for: last_completed_date
- Format: 2025-03-05
- Example use: Check if automation task completed "today"

**TimeField** (TIME):
- Stores time only (no date component)
- Used for: recurrence_time
- Format: 14:30:00 (24-hour format)
- Example: Task runs daily at 09:00:00

### Text Fields

**CharField** (VARCHAR):
- Fixed max length declared at schema level
- title: max 255 characters (task name)
- task_type: max 20 characters ('user' or 'automation')
- slug: max 200 characters (URL-safe identifier)
- recurrence_days: max 20 characters (e.g., 'mon,tue,wed')

**TextField** (TEXT):
- Unlimited length (within database limits)
- description: Task details/instructions
- Supports rich text and long descriptions
- No length constraint at schema level

### Boolean Fields

**BooleanField** (BOOLEAN):
- Values: TRUE or FALSE (1 or 0 in some systems)
- is_completed: Task completion status
- is_read: Notification read status
- Never NULL (always has a default value)

### Numeric Fields

**BigAutoField** (BIGINT with IDENTITY):
- Auto-incremented integer
- Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
- Provides virtually unlimited IDs
- GENERATED BY DEFAULT AS IDENTITY syntax

**ForeignKey** (INTEGER):
- References another table's primary key
- user_id: Links to auth_user.id
- category_id: Links to todo_category.id
- Can be NULL for optional relationships (category_id)
- Enforces referential integrity

---

## Data Validation Rules

### Task Model Validation
1. **title**: Required, must be unique, 1-255 characters
2. **user_id**: Required, must exist in auth_user table
3. **category_id**: Optional, if provided must exist in todo_category table
4. **slug**: Optional if provided, must be unique, URL-safe format
5. **description**: Optional, can be empty string
6. **scheduled_time**: Optional, must not be in the past for user tasks
7. **task_type**: Required, must be 'user' or 'automation', defaults to 'user'
8. **is_completed**: Defaults to FALSE
9. For automation tasks:
   - recurrence_days: Optional comma-separated list
   - recurrence_time: Optional time of day
   - At least one should be set for meaningful automation

### Category Model Validation
1. **name**: Required, must be unique, 1-100 characters

### Notification Model Validation
1. **user_id**: Required, must exist in auth_user table
2. **message**: Required, 1-255 characters
3. **is_read**: Defaults to FALSE

---

## Relationships and Cardinality

### Task Types and Behavior

**User Tasks** (task_type = 'user'):
- Single execution at a specific scheduled_time
- Has scheduled_time field populated
- recurrence_time and recurrence_days should be NULL
- last_completed_date is not used
- Properties: is_overdue, is_due_soon, is_pending status

**Automation Tasks** (task_type = 'automation'):
- Recurring execution based on recurrence_days and recurrence_time
- scheduled_time is not used (NULL)
- recurrence_time: What time of day to run
- recurrence_days: Which days to run (e.g., 'mon,tue,wed')
- last_completed_date: Tracks daily completion
- Properties: is_pending_for_today, is_completed_for_today, is_recurring

---

## Common Queries

### Find All Tasks for a User
```sql
SELECT * FROM todo_task WHERE user_id = 1;
```

### Find Overdue Tasks
```sql
SELECT * FROM todo_task 
WHERE is_completed = FALSE 
AND scheduled_time < NOW() 
AND task_type = 'user';
```

### Find Tasks Due in Next 24 Hours
```sql
SELECT * FROM todo_task 
WHERE scheduled_time BETWEEN NOW() AND NOW() + INTERVAL '1 day' 
AND is_completed = FALSE
AND task_type = 'user';
```

### Find Automation Tasks to Run Today
```sql
SELECT * FROM todo_task 
WHERE task_type = 'automation' 
AND (last_completed_date IS NULL OR last_completed_date < TODAY());
```

### Get User Notifications
```sql
SELECT * FROM todo_notification 
WHERE user_id = 1 
ORDER BY created_at DESC;
```

### Get Unread Notifications Count
```sql
SELECT COUNT(*) FROM todo_notification 
WHERE user_id = 1 AND is_read = FALSE;
```

---

## Notes for Assessment

1. **Scalability**: Schema uses BIGINT IDs suitable for large-scale applications
2. **Timezone Awareness**: All timestamps use UTC timezone for consistency
3. **Audit Trail**: created_at and updated_at fields track record lifecycle
4. **Soft Deletes**: Not implemented; uses CASCADE and SET NULL policies
5. **Referential Integrity**: Foreign keys use DEFERRABLE INITIALLY DEFERRED
6. **Uniqueness Constraints**: title and slug ensure no duplicate tasks
7. **Category Optional**: Tasks can exist without categories (NULL allowed)
8. **Automation Support**: Dedicated fields for recurring task scheduling
9. **Multi-user**: Design supports multiple users with proper FK relationships
10. **Index Strategy**: Indexes on foreign keys and unique fields for performance
