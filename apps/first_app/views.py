from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Activity
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):

    results = User.objects.register_valdiation(request.POST)

    if results[0]:

        request.session['user_id'] = results[1].id
        print "******* You registered yo! ******"
        return redirect('/dashboard')
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/')

def login(request):
    results = User.objects.login_validation(request.POST)
    
    if results[0]:
        request.session['user_id'] = results[1].id 
        print "******* logged in yo! ******"
        return redirect('/dashboard')
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/')

def logout(request):
    request.session.flush()
    print "++++++++ You logged out ++++++++++"
    return redirect('/')

#Home Page
def dashboard(request):
    me = User.objects.get(id=request.session['user_id'])
    activity = Activity.objects.filter(creater=me)
    other = Activity.objects.exclude(creater=me)
    leave = Activity.objects.filter(join=me)
    order = Activity.objects.order_by('from_date')
    context = {
        "username": User.objects.get(id=request.session['user_id']),
        "activity": activity,
        "other": other,
        "leave": leave,
        "order": order,
    }
    return render(request, "dashboard.html", context)

def new(request):
    return render(request, "new.html")

def added(request):

    user = User.objects.get(id=request.session['user_id'])
    new_activity = Activity.objects.create(
        creater = user,
        title = request.POST['title'],
        from_date = request.POST['from_date'],
        to_date = request.POST['to_date'],
        description = request.POST['description'],
    )
    print "activity has been added"
    return redirect('/dashboard')

def delete(request, id):
    user = User.objects.get(id=request.session['user_id'])
    del_this = Activity.objects.get(id=id)
    Activity.objects.filter(id=id).delete()
    
    return redirect("/dashboard")

def activity(request, id):
    user = User.objects.get(id=request.session['user_id'])
    activity = Activity.objects.get(id=id)
    context = {
        "activity" : activity,

    }
    return render(request, "activity.html", context)

def join(request, id):
    user = User.objects.get(id=request.session['user_id'])
    joining = Activity.objects.get(id=id)
    joining.join.add(user)
    print "you have joined the event"
    return redirect("/dashboard")

def leave(request, id):
    user = User.objects.get(id=request.session['user_id'])
    leave = Activity.objects.get(id=id)
    leave.join.remove(user)
    return redirect("/dashboard")