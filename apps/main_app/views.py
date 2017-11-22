from django.shortcuts import render,redirect
from ..login_app.models import User
from .models import Quote
from django.contrib import messages
# Create your views here.
def index(request):
    cur_user = User.objects.get(id=request.session['id'])
    context={
        'cur_user': User.objects.get(id=request.session['id']),
        'myquotes': cur_user.quotes.all(),
        'allquotes': Quote.objects.all(),
    }

    return render(request,'main_app/index.html',context)

def create(request):
    if len(request.POST['quoted_by'].strip()) < 2:
        messages.error(request, 'Enter a valid Author Name of this Quote')
        return redirect('/main/')
    if len(request.POST['message'].strip()) < 10:
        messages.error(request, 'Message should be at least 10 chars long')
        return redirect('/main/')
    else:
        user = User.objects.get(id=request.session['id'])        
        quote=Quote.objects.create(owner = user, quoted_by = request.POST['quoted_by'], message = request.POST['message'])
    return redirect('/main/')

def addQuote(request,id):
    quote=Quote.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    user.favorites.add(quote)
    return redirect('/main/')

def removeQuote(request,id):
    quote = Quote.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.favorites.remove(quote)
    return redirect('/main/')

def showUser(request,id):
    user = User.objects.get(id=id)
    context = {
        'myquotes': user.quotes.all(),
        'user' : user,
        'count' : len(user.quotes.all())
    }
    return render(request, "main_app/show.html", context)