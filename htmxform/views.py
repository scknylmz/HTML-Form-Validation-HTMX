from django.shortcuts import redirect, render
from .forms import SimpleForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            return render(request, 'redirect.html')
        else:
            print(form.errors) # Now we have unvalid form and validation error messages. 
            context ={
                'form' : form,
            }
            return render(request,'index.html', context)
    form = SimpleForm()
    context ={
        'form' : form,
    }
    return render(request,'index.html', context)

def check_name(request):
    form = SimpleForm(request.GET)
    if form.is_valid():
        valid = True
    else:
        valid = False

    try:
        error = form.errors['name']
    except KeyError:
        error = "No Error"
 
    context = {
        'form' : error,
        'valid' : valid
    }
    return render(request, 'partials/field.html', context)

def check_email(request):
    form = SimpleForm(request.GET)
    if form.is_valid():
        valid = True
    else:
        valid = False

    try:
        error = form.errors['email']
    except KeyError:
        error = "No Error"
    
    context = {
        'form' : error,
        'valid' : valid
    }
    return render(request, 'partials/field.html', context)

def check_password(request):
    form = SimpleForm(request.GET)
    print(form.errors)
    if form.is_valid():
        valid = True
    else:
        valid = False

    try:
        error = form.errors['password']
    except KeyError:
        error = "No Error"
    
    context = {
        'form' : error,
        'valid' : valid
    }
    return render(request, 'partials/field.html', context)