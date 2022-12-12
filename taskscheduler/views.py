from django.shortcuts import render, redirect
import calendar, datetime
from django.http import HttpResponse
from django.template import loader
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    user = request.user
    yy = datetime.date.today().year
    mm = datetime.date.today().month
    dates = [i.split() for i in calendar.month(yy, mm).split('\n')]
    month = ' '.join(dates.pop(0))
    dates.pop(0)
    dates[0] = [' '] * (7 - len(dates[0])) + dates[0]
    content = {
        'year': yy,
        'month_numeric': mm,
        "month": month, 
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "dates": dates,
    }
    return render(request, 'index.html', content)


def get_previous(request, yy, mm):
    if mm == 1:
        mm = 12
        yy -= 1
    else:
        mm -= 1
    dates = [i.split() for i in calendar.month(yy, mm).split('\n')]
    month = ' '.join(dates.pop(0))
    dates.pop(0)
    dates[0] = [' '] * (7 - len(dates[0])) + dates[0]
    content = {
        'year': yy,
        'month_numeric': mm,
        "month": month, 
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "dates": dates,
    }
    return render(request, 'index.html', content)


def get_next(request, yy, mm):
    if mm == 12:
        mm = 1
        yy += 1
    else:
        mm += 1
    dates = [i.split() for i in calendar.month(yy, mm).split('\n')]
    month = ' '.join(dates.pop(0))
    dates.pop(0)
    dates[0] = [' '] * (7 - len(dates[0])) + dates[0]
    content = {
        'year': yy,
        'month_numeric': mm,
        "month": month, 
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "dates": dates,
    }
    return render(request, 'index.html', content)


def get_date(request, year, month, day):
    date = datetime.date(year, month, day)
    all_events = Event.objects.all()
    events = [event for event in all_events if (event.start_date <= date <= event.end_date)]
    content = {
        'date': date,
        'events': events,
    }
    return render(request, 'index.html', content)


def add_event(request):
    sd = list(map(int, request.POST.get('start_date').split('-')))
    st = list(map(int, request.POST.get('start_time').split(':')))
    ed = list(map(int, request.POST.get('end_date').split('-')))
    et = list(map(int, request.POST.get('end_time').split(':')))
    e = Event.objects.create(
        user = request.user,
        text = request.POST.get('event_text'),
        start_date = datetime.date(sd[0], sd[1], sd[2]),
        start_time = datetime.time(st[0], st[1]),
        end_date = datetime.date(ed[0], ed[1], ed[2]),
        end_time = datetime.time(et[0], et[1]),
        completed = False
    )
    return index(request)


def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return index(request)


def details(request, id):
    event = Event.objects.get(id=id)
    content = {
        'event': event,
    }
    return render(request, 'details.html', content)


def update_event(request, id):
    event = Event.objects.get(id=id)
    changeList = request.POST
    if changeList['event_text'] != '':
        event.text = changeList['event_text']
    if changeList['start_date'] != '':
        d = list(map(int, changeList['start_date'].split('-')))
        event.start_date = datetime.date(d[0], d[1], d[2])
    if changeList['start_time'] != '':
        t = list(map(int, changeList['start_time'].split(':')))
        event.start_time = datetime.time(t[0], t[1])
    if changeList['end_date'] != '':
        d = list(map(int, changeList['end_date'].split('-')))
        event.start_date = datetime.date(d[0], d[1], d[2])
    if changeList['end_time'] != '':
        t = list(map(int, changeList['end_time'].split(':')))
        event.start_time = datetime.time(t[0], t[1])
    event.save()
    return index(request)

