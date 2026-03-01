# ToDoBot Database Schema

## Overview
This document describes the database schema for the ToDoBot application, a Django-based task management system with support for user authentication, task categorization, and automated home automation tasks.

## Tables

### 1. todo_task
Core table for storing tasks. Each task belongs to a user and may belong to a category.

| Column | Type | Constraints | Description |
|--------|------|-----------|-------------|
| id | BIGINT | PRIMARY KEY, AUTO-INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY (auth_user.id) | User who owns the task |
| category_id | BIGINT | FOREIGN KEY (todo_category.id), NULL | Task category |
| title | VARCHAR(255) | UNIQUE, NOT NULL | Task title |
| slug | VARCHAR(200) | UNIQUE, NULL | URL-friendly slug |
| description | TEXT | NOT NULL | Task description/details |
| task_type | VARCHAR(20) | NOT NULL, DEFAULT='user' | Type: 'user' or 'automation' |
| scheduled_time | TIMESTAMP WITH TZ | NULL | When task is scheduled |
| is_completed | BOOLEAN | NOT NULL, DEFAULT=FALSE | Completion status |
| created_at | TIMESTAMP WITH TZ | NOT NULL, AUTO | Timestamp when created |
| updated_at | TIMESTAMP WITH TZ | NOT NULL, AUTO | Timestamp when updated |
| recurrence_time | TIME | NULL | Time of day for automation recurrence |
| recurrence_days | VARCHAR(20) | NULL | Comma-separated days (mon,tue,wed) |
| last_completed_date | DATE | NULL | Last completion date for automation tasks |

**Indexes:**
- Primary Key: id
- Foreign Key: user_id (todo_task_user_id_69f329a5)
- Foreign Key: category_id (todo_task_category_id_fb0c0926)
- Unique: title (todo_task_title_fe9014fc_like)
- Unique: slug (todo_task_slug_e7a5bf53_like)

### 2. todo_category
Category table for organizing tasks.

| Column | Type | Constraints | Description |
|--------|------|-----------|-------------|
| id | BIGINT | PRIMARY KEY, AUTO-INCREMENT | Unique identifier |
| name | VARCHAR(100) | UNIQUE, NOT NULL | Category name |

**Indexes:**
- Primary Key: id
- Unique: name (todo_category_name_124c74fd_like)

### 3. todo_notification
Notification table for user notifications.

| Column | Type | Constraints | Description |
|--------|------|-----------|-------------|
| id | BIGINT | PRIMARY KEY, AUTO-INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY (auth_user.id), NOT NULL | User receiving notification |
| message | VARCHAR(255) | NOT NULL | Notification message |
| is_read | BOOLEAN | NOT NULL, DEFAULT=FALSE | Read status |
| created_at | TIMESTAMP WITH TZ | NOT NULL, AUTO | Timestamp when created |

**Indexes:**
- Primary Key: id
- Foreign Key: user_id (todo_notification_user_id_d5944080)

## Entity Relationship Diagram

```
┌─────────────────────┐
│   auth_user         │
│  (Django Auth)      │
│─────────────────────│
│ id (PK)             │
│ username            │
│ email               │
│ password            │
└──────────┬──────────┘
           │
           │ (1:N)
           │
    ┌──────┴──────────────────────┐
    │                             │
    │                    ┌────────▼──────────────┐
    │                    │   todo_task           │
    │                    │──────────────────────│
    │                    │ id (PK)              │
    │                    │ user_id (FK) ◄──────┤
    │                    │ category_id (FK) ────┐
    │                    │ title (UNIQUE)       │
    │                    │ description          │
    │                    │ slug (UNIQUE)        │
    │                    │ task_type            │
    │                    │ scheduled_time       │
    │                    │ is_completed         │
    │                    │ recurrence_time      │
    │                    │ recurrence_days      │
    │                    │ last_completed_date  │
    │                    │ created_at           │
    │                    │ updated_at           │
    │                    └──────────────────────┘
    │                             ▲
    │                             │ (1:N)
    │                             │
    │                    ┌────────┴──────────────┐
    │                    │   todo_category       │
    │                    │──────────────────────│
    │                    │ id (PK)              │
    │                    │ name (UNIQUE)        │
    │                    └──────────────────────┘
    │
    │ (1:N)
    │
    └──────────────────────────┐
                               │
                    ┌──────────▼──────────────┐
                    │ todo_notification       │
                    │──────────────────────│
                    │ id (PK)              │
                    │ user_id (FK) ◄──────┤
                    │ message              │
                    │ is_read              │
                    │ created_at           │
                    └──────────────────────┘
```

## Relationships

1. **auth_user ← → todo_task** (One-to-Many)
   - A user can have many tasks
   - Foreign Key: user_id in todo_task references auth_user.id
   - ON DELETE: CASCADE (deleting user deletes all tasks)

2. **todo_category ← → todo_task** (One-to-Many)
   - A category can have many tasks
   - Foreign Key: category_id in todo_task references todo_category.id
   - ON DELETE: SET NULL (deleting category doesn't delete tasks)
   - Nullable: True (tasks can exist without a category)

3. **auth_user ← → todo_notification** (One-to-Many)
   - A user can have many notifications
   - Foreign Key: user_id in todo_notification references auth_user.id
   - ON DELETE: CASCADE (deleting user deletes all notifications)

## Key Features

### Task Types
- **user**: Regular user tasks (can be scheduled, have deadlines)
- **automation**: Home automation tasks (can have recurring schedules)

### Task States
- **Pending**: Not completed, not overdue, scheduled in the future
- **Overdue**: Not completed and scheduled time is in the past (user tasks only)
- **Due Soon**: Scheduled within the next 24 hours
- **Completed**: is_completed = TRUE

### Automation Features
- **Recurrence Days**: Comma-separated days (e.g., 'mon,tue,wed')
- **Recurrence Time**: Time of day for execution
- **Last Completed Date**: Tracks the last execution date for daily checks

## SQL Schema (Final State)

### Create Table: todo_task
```sql
CREATE TABLE "todo_task" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "title" varchar(255) NOT NULL,
    "description" text NOT NULL,
    "scheduled_time" timestamp with time zone NULL,
    "is_completed" boolean NOT NULL,
    "task_type" varchar(20) NOT NULL DEFAULT 'user',
    "created_at" timestamp with time zone NOT NULL,
    "updated_at" timestamp with time zone NOT NULL,
    "user_id" integer NOT NULL,
    "category_id" bigint NULL,
    "slug" varchar(200) NULL UNIQUE,
    "recurrence_days" varchar(20) NULL,
    "recurrence_time" time NULL,
    "last_completed_date" date NULL,
    FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    FOREIGN KEY ("category_id") REFERENCES "todo_category" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "todo_task_user_id_69f329a5" ON "todo_task" ("user_id");
CREATE INDEX "todo_task_category_id_fb0c0926" ON "todo_task" ("category_id");
CREATE INDEX "todo_task_slug_e7a5bf53_like" ON "todo_task" ("slug" varchar_pattern_ops);
CREATE INDEX "todo_task_title_fe9014fc_like" ON "todo_task" ("title" varchar_pattern_ops);
```

### Create Table: todo_category
```sql
CREATE TABLE "todo_category" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "name" varchar(100) NOT NULL UNIQUE
);

CREATE INDEX "todo_category_name_124c74fd_like" ON "todo_category" ("name" varchar_pattern_ops);
```

### Create Table: todo_notification
```sql
CREATE TABLE "todo_notification" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "message" varchar(255) NOT NULL,
    "created_at" timestamp with time zone NOT NULL,
    "is_read" boolean NOT NULL,
    "user_id" integer NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "todo_notification_user_id_d5944080" ON "todo_notification" ("user_id");
```

## Data Types Summary

| Django Type | PostgreSQL Type | Notes |
|------------|-----------------|-------|
| BigAutoField | bigint | Auto-incrementing, identity |
| ForeignKey | integer | Links to auth_user.id |
| CharField | varchar | Variable length strings |
| TextField | text | Large text fields |
| BooleanField | boolean | TRUE/FALSE |
| DateTimeField | timestamp with time zone | UTC timestamps |
| DateField | date | Date only |
| TimeField | time | Time only |
| SlugField | varchar | URL-safe strings |

## Migration History

1. **0001_initial**: Created Task model with initial fields
2. **0002_category_task_category**: Added Category model and category_id to Task
3. **0003_default_categories**: Data migration for default categories
4. **0004_remove_task_action...**: Removed obsolete automation fields
5. **0005_enforce_default_categories**: Data migration enforcement
6. **0006_task_slug**: Added slug field to Task
7. **0007_alter_task_slug...**: Made title UNIQUE, ensured slug uniqueness
8. **0008_task_recurrence_***: Added recurrence fields for automation tasks
9. **0009_task_last_completed_date**: Added last_completed_date tracking
10. **0010_notification**: Created Notification model

## Notes

- All timestamps use UTC (timestamp with time zone)
- Database uses PostgreSQL (identity columns, timezone-aware timestamps)
- Foreign keys use DEFERRABLE INITIALLY DEFERRED for flexibility
- Soft deletes are not used; CASCADE and SET NULL policies apply
- The schema supports multi-tenant usage via auth_user relationships
- Automation tasks track execution with last_completed_date
- All models include audit timestamps (created_at, updated_at)
