

from django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
#from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 


@login_required(login_url = 'login')
def home(request):
    return render(request, 'first/home3.html')


def register(request):
  	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('login')


	context = { 'form': form }
	return render (request, 'first/register.html', context)
    


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'first/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('login')

from .models import Projects
def list(request):
    project = Projects.objects.all()
    context = {  'project' : project }
    return render (request, 'first/list.html', context)

def detail(request, id):
	project = Projects.objects.get(id = id)	
	context = {'proj':project }
	return render(request,'first/detail.html', context)
