from .models import User, Table, Event 
from datetime import datetime
import smtplib, ssl 

# must have two factor auth enabled 
# password is given from App Passwords -> 'myaccount.google.com/apppasswords'
# password is not email password 

PORT = 465
SMTP_SERVER = 'smtp.gmail.com'


def send(user, message):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context)
        server.login(str(user.email), str(user.apppassword.app_password))
        server.sendmail(str(user.email), str(user.email), str(message))
    except Exception as e:
        print(str(e))

def job():
    # get all tables and user from table
    # get events from table 
    # search for user and matching app password 
    # send email 
    dateToday = datetime.today().strftime('%Y-%m-%d')
    tables = Table.objects.all()
    for table in tables:
        user = User.objects.get(username=str(table.user))
        for event in table.event_set.all():
            if str(event.start_date) == str(dateToday):
                send(user, event.text)


