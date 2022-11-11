from django.shortcuts import render
import calendar, datetime
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    user = request.user
    yy = datetime.date.today().year
    mm = datetime.date.today().month
    dates = [i.split() for i in calendar.month(yy, mm).split('\n')]
    month = ' '.join(dates.pop(0))
    dates.pop(0)
    dates[0] = [' '] * (7 - len(dates[0])) + dates[0]
    content = {
        "month": month, 
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "dates": dates,
    }
    return render(request, 'index.html', content)