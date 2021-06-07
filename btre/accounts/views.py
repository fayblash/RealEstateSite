from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from contacts.models import Contact
# Create your views here.

def register(request):
    form = CustomCreationForm()
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'accounts/register.html', {'form': form})
    
def login(request):
    return render(request,'accounts/login.html')

def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)

def logout(request):
    return redirect ('index')