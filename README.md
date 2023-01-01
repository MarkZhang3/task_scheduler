# Task Scheduler

You can see it live [here](MarkZhang.pythonanywhere.com)  

## Motivation
I have a hard time keeping track of what I need to do day to day. Often I’ll think of things to do for my day in the morning but then forget everything I planned out by the afternoon. I wanted to make a simple website where I can keep track of tasks I want to get done and also send myself email reminders to actually complete the tasks. 

## Features
Task scheduler has a Login/Logout and user authentication system. (There is a demo feature to use the app without needing to make a new user)  
After logging in, the main layout of task scheduler consists of a calendar and sidebar, where the side bar displays the day you click on and the events you saved/planned for that day.   
Users can view their profile to see and make changes to their username, email and password, and add an App Password for their email so that the web app can send email reminders on the days that events are due.   

## Email
Task Scheduler uses stmplib and ssl libraries and APScheduler package to send an automated email through python.   
In order to do this, the app needs the user’s email and an app password which can be generated via [Google App Passwords](myaccount.google.com/apppasswords). Once you obtain an app password for your email, go to Profile to add the password.  

## Next steps
- Add feature to see which day is clicked on inside the calendar 
- Display events inside the calendar 
- Better css formatting 
- Toggling whether app sends email