

    ▄▄▄█████▓░ ██▓░ ███▄ ▄███▓░▓█████  ██▓    ▓██   ██▓
    ▓  ██▒ ▓▒░▓██▒░▓██▒▀█▀ ██▒░▓█   ▀ ▓██▒     ▒██  ██▒
    ▒ ▓██░ ▒░░▒██▒░▓██    ▓██░░▒███   ▒██░      ▒██ ██░
    ░ ▓██▓ ░ ░░██░░▒██    ▒██ ░▒▓█  ▄ ▒██░      ░ ▐██▓░
      ▒██▒ ░  ░██░░▒██▒   ░██▒░░▒████▒░██████▒  ░ ██▒▓░
      ▒ ░░    ░▓  ░░ ▒░   ░  ░░░░ ▒░ ░░ ▒░▓  ░   ██▒▒▒ 
        ░      ▒ ░░░  ░      ░░ ░ ░  ░░ ░ ▒  ░ ▓██ ░▒░ 
      ░        ▒ ░░░      ░      ░     ░ ░    ▒ ▒ ░░  
               ░  ░       ░      ░  ░    ░  ░ ░ ░     
                                            ░ ░     

# Timely - Project Documentation

Timely is a robust web application developed with Python, Django, PostgreSQL, and Vue.js. This platform allows users to manage team, project, and task management with features, such as secure user authentication, precise time tracking, support for multiple task and project dependencies, Stripe payment integration, and security.

## Table of Contents

- [Overview](#overview-timely)
- [Project Mindmap](#project-mindmap)
- [Installation](#getting-started)
- [Stripe Integration](#stripe-integration)
- [Expectation](#expectation)
- [Future Work](#future-work)


## Overview: Timely

This platform provides users with an efficient way to organize their work, optimize productivity, and maintain data security. Timely provides a wide range of functionality to meet the various needs of teams and individual users.

**Key Features:**

1. **User Authentication:** Timely offers a secure user authentication system, allowing users to create accounts and log in to access the platform.

2. **Pricing Plans:** Users can choose between a Free plan and Premium ( Basic / Pro ) plan
, which offers advanced features and is available for a modest fee of $5/10. Stripe payment integration ensures a smooth and secure payment process.

3. **Team Management:** Timely supports the creation of teams, enabling users to add members by inviting them through email addresses.

4. **Comprehensive CRUD Functionality:**
   - **Projects:** Users can create, edit, and delete projects under any team, facilitating project organization.
   - **Tasks:** Users can manage tasks under each project, with the ability to create, edit, and delete tasks. Task dependencies and timers are supported to streamline workflow.

5. **Task Dependencies:** Timely allows users to establish dependencies between tasks, ensuring tasks are completed in the correct order and optimizing project efficiency.

6. **Time Tracking:** Users can add timers to tasks and projects, tracking the time spent on each activity to improve time management and project scheduling.

7. **Data Security:** Data security is a top priority. Timely implements a robust authorization system to safeguard user data.

8. **Account Management:** Users have the flexibility to edit their account information, customizing their profile to their specific needs.

## Project Mindmap

![Mindmap](https://github.com/AAhadNur/Timely/blob/main/uploads/diagrams/Timely_Mindmap.png)

## Getting Started 

Follow these steps to set up and install Timely on your local development environment:

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

- Python
- PostgreSQL
- Virtual environment (e.g., virtualenv)

### Clone the Repository

```bash
git clone https://github.com/AAhadNur/Timely.git
cd timely
```

### Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Configure the .env File

Create a `.env` file in the project root directory.
Add the following environment variables to your `.env` file with your actual values:

```
# Django settings
SECRET_KEY = django_secret_key
DEBUG = True

# Database configuration
DB_ENGINE = django.db.backends.postgresql
DB_NAME = your_database_name
DB_USER = your_database_user
DB_PASSWORD = your_database_password_here
DB_HOST = localhost
DB_PORT = 5432

# Email configuration
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = your_email_address
EMAIL_HOST_PASSWORD = your_email_password_here
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = sender-email-address

# Stripe Credentials
STRIPE_PUBLISHABLE_KEY = your-stripe-account-public-key
STRIPE_SECRET_KEY = your-stripe-account-secret-key
STRIPE_BASIC_PRICE_ID = basic-plan-price-key
STRIPE_PRO_PRICE_ID = pro-plan-price-key
STRIPE_WEBHOOK_KEY = your-stripe-webhook-key
```

### Set Up the PostgreSQL Database

1. Create a PostgreSQL database and user using the following commands:

```bash
createdb your-db-name
createuser your-db-username
```
2. Grant privileges to the user:
```bash
psql
ALTER USER your-db-username WITH PASSWORD 'your-db-password';
ALTER ROLE your-db-username SET client_encoding TO 'utf8';
ALTER ROLE your-db-username SET default_transaction_isolation TO 'read committed';
ALTER ROLE your-db-username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your-db-name TO your-db-username;
\q
```
3. Apply database migrations:
```bash
python manage.py migrate
```
4. Load initial data from the `data.json` file:
```bash
python manage.py loaddata data.json
```

### Start the Development Server
```bash
python manage.py runserver
```
( You do not need to configure any frontend cause I have integrated Vue.js in templates )

## Stripe Integration

For detailed instructions [see this](https://dev.to/documatic/integrate-stripe-payments-with-django-by-building-a-digital-products-selling-app-le5)

## Expectation

The expectations for my project "Timely" can be summarized as:

- Smooth functionality across browsers and devices.
- Efficient database management and optimization.
- Responsive design for mobile and desktop.
- High code quality and maintainability.
- API integration for future extensions.
- Cross-browser compatibility and adherence to web standards.

## Future Work

Possible future works:

- Integration with additional third-party tools.
- Advanced reporting and analytics features.
- Enhanced team collaboration and communication tools.
- Integration with other payment gateways.
- Customizable themes and templates.


