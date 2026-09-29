# Learning Log

A full-stack web application built with Python and Django that allows users to track topics they are learning about and maintain a journal of detailed entries for each topic.

---

## Technologies Used

* **Backend**: Python 3.10+, Django
* **Frontend**: HTML5, CSS3, Bootstrap 5 (`django-bootstrap5`)
* **Database**: SQLite (Development)
* **Authentication**: Django Contrib Auth System

---

## Key Features

### User Management & Security
- **Authentication**: User registration, login, and logout workflows.
- **Data Privacy & Ownership**: Strict per-user access control—users can only view, create and edit their own topics and entries.
- **Error Handling**: Graceful `Http404` handling for nonexistent records or unauthorized access attempts.
- **Topic Management**: Create new topics and browse an overview of all active learning topics.
- **Entry Timeline**: Dedicated detail view per topic showing associated log entries.
- **Content Editing**: Edit existing entries.

### Modern Responsive UI
- **Bootstrap 5 Integration**: Responsive navigation bar, card-based entry layouts, and clean list groups.
- **Template Inheritance**: Centralized `base.html` shell ensuring uniform navigation and styling across all views.
- **Django Admin Portal**: Built-in administration panel for superuser model management (`Topic` and `Entry`).

---

## Project Structure

```text
├── learnlog_project/    # Project configuration, root URLs, and global settings
├── learning_log/        # Core app: models, views, URL routes, forms
│   └── templates/       # App-specific HTML templates (topics, topic, entries, add and edit entries)
├── accounts/            # Authentication app: login, registration forms & views
├── manage.py            # Django CLI management script
└── requirements.txt     # Python project dependencies

```
## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

* **Python 3.10+**
* **Git**

---

### Step-by-Step Installation

1. **Clone the repository:**
  ```bash
  git clone https://github.com/rupashrimohan/learning_log.git
  cd learning_log
  ```   
2. **Create and activate a virtual environment:**
    On macOS / Linux:
    ```bash
    python3 -m venv ll_env
    source ll_env/bin/activate
    ```
    On Windows:
    ```bash
    python -m venv ll_env
    ll_env\Scripts\activate
    ```
    
3. **Install required dependencies:**
  ```bash
   pip install -r requirements.txt
   ```
   
4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    
6. **Start the local development server:**
    ```bash
    python manage.py runserver
    ```
    
7. **Access the application:**
    Open your browser and visit:

    Plaintext
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)