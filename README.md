# Task Scheduler - A Python Django Web Application for Easy Task Management

Hosted on pythonanywhere [link](http://markzhang.pythonanywhere.com/login/?next=/)

# Introduction:

Task Scheduler is a feature-rich web application built using Python Django that allows users to efficiently manage their tasks and events. This user-friendly tool provides a simple and intuitive interface to schedule, view, and edit tasks effortlessly. The application supports user authentication and includes additional features like email reminders for upcoming events and user profile management.

## Key Features

1. **User Authentication System:**
   - Task Scheduler comes with a robust login/logout system to secure user data and ensure a personalized experience.
   - Users can also explore the app through the demo feature without creating a new account.

2. **Task Management:**
   - The main layout comprises a calendar and a sidebar, making it easy for users to organize their events and tasks.
   - The sidebar displays selected dates and the corresponding scheduled events.

3. **Profile Management:**
   - Users can access their profiles to make changes to their username, email, and password settings.
   - To enable email reminders for upcoming events, users can add an "App Password" for their email account, ensuring timely notifications.

4. **Automated Email Reminders:**
   - Task Scheduler integrates with `stmplib`, `ssl` libraries, and the `APScheduler` package to send automated email reminders.
   - Users can provide their email address and the app password to receive reminders about upcoming events, ensuring timely follow-ups.
   - In order to do this, the app needs the user’s email and an app password which can be generated via [Google App Passwords](myaccount.google.com/apppasswords). Once you obtain an app password for your email, go to Profile to add the password.  

# Getting Started

1. **Installation:**
   - Clone this repository to your local machine using `git clone https://github.com/username/task-scheduler.git`
   - Create a virtual environment and activate it.
   - Install the required dependencies using `pip install -r requirements.txt`

2. **Database Setup:**
   - Task Scheduler is currently linked to PythonAnywhere's free MySQL server.
   - If you want to use your own MySQL server or a different database, you can modify the database settings in `settings.py`.
   - Run migrations using `python manage.py migrate` to set up the database.

3. **Create Superuser:**
   - Create a superuser account to access the Django admin panel using `python manage.py createsuperuser`.

4. **Running the Application:**
   - Start the development server using `python manage.py runserver`.
   - Access the web app through your browser at `http://localhost:8000/`.

## Usage

- **Register/Login:** Users can create an account or log in using their credentials.

- **Demo Mode:** Explore the app's functionality without registering by using the demo feature.

- **Calendar View:** The main page displays a calendar, and users can click on specific dates to view and manage events.

- **Profile Settings:** Users can access their profiles to modify their username, email, and password settings.

- **App Password:** To enable email reminders, add an "App Password" for your email account.


## Next steps
- Add feature to see which day is clicked on inside the calendar 
- Display events inside the calendar 
- Better css formatting 
- Toggling whether app sends email
