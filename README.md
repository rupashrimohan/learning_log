# Learning Log

A web application built with Python and Django (web framework) that allows users to track topics they are learning about and keep a journal of specific entries for those topics.

## Technologies Used
* Python
* Django

## Features 

- **Home Page**: Welcoming landing page introducing the application.
- **Topic Management**:
  - View a list of all active learning topics.
  - Dedicated detail view for each topic displaying all associated log entries in chronological order.
- **Error Handling**: Graceful 404 handling for invalid or nonexistent topic IDs.
- **Admin Portal**: Integrated Django admin site for managing data models (`Topic` and `Entry`).
- **Template Inheritance**: Consistent site-wide navigation and layout via a base master template.

---

## Project Structure

- `learnlog_project/`: Project configuration, global settings, and root URL routing.
- `learning_log/`: Main application directory containing models, views, templates, and app-specific routes.

### Prerequisites
- Python 3.10+
- Virtual environment (`venv`)