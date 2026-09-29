# Learning Log Specifications

## 1. User Features & Access Control
* **Authentication**: Users can register an account, log in, and log out.
* **Homepage**: Welcomes visitors, describes the purpose of the application, and links to registration and login forms.
* **Topic Management**: Authenticated users can create new topics and view a list of all their created topics.
* **Entry Management**: Authenticated users can view entries grouped by topic, add new entries, and modify existing entries.
* **Data Privacy**: Users can only see and modify their own topics and entries.

## 2. Layout & User Interface
* **Framework**: Built with Bootstrap 5 (via `django_bootstrap5`).
* **Base Template**: Responsive navigation header containing brand identity and dynamic navigation controls.
* **Topics View**: Clean list group display linking to individual topic detail views.
 