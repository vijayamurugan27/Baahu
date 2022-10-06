# from email import message
from itertools import count
# from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages

from .models import Projects
from .forms import ProjectsForm
# from django.db.models import Q

# from django.http import HttpResponseRedirect
from django.urls import reverse

def proj1(request):
    project  = Projects.objects.all()
    New_proj = Projects.objects.filter(completed = True).count()
    # print(New_proj)
    # print(type(New_proj))
    New_id = New_proj+1
    project1 = Projects.objects.get(id = New_id)
    
    if request.method =="POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ProjectsForm()
    return render(request, "first/app/proj1.html", {'form': form, 'proj':project, 'project1':project1})

def det(request, id):
    project = Projects.objects.get(id = id)
    context = {'project':project}
    print(project)
    return render(request, 'first/app/det.html', context)

def det1(request, id):
    project = Projects.objects.get(id = id)
    context = {'project':project}
    print(project)
    return render(request, 'first/app/det1.html', context)

def det2(request, id):
    project = Projects.objects.get(id = id)
    context = {'project':project}
    print(project)
    return render(request, 'first/app/det2.html', context)


def det3(request, id):
    project = Projects.objects.get(id = id)
    context = {'project':project}
    print(project)
    return render(request, 'first/app/det3.html', context)


def det4(request, id):
    project = Projects.objects.get(id = id)
    context = {'project':project}
    print(project)
    return render(request, 'first/app/det4.html', context)


def det5(request, id):
    project = Projects.objects.get(id = id)
    context = {'project':project}
    print(project)
    return render(request, 'first/app/det5.html', context)


def import_data(request,id):
    project = Projects.objects.get(id = id)
    context = {'project': project}
    return render(request, 'first/in/import.html', context)    


def view_data(request,id):
    project = Projects.objects.get(id = id)
    context = {'project': project}
    return render(request, 'first/in/view.html', context)    


def transform_data(request,id):
    project = Projects.objects.get(id = id)
    context = {'project': project}
    return render(request, 'first/in/transform.html', context)    


def createtransformation(request):
    return render(request,'first/tr/create.html')

def executetransformation(request):
    return render(request, 'first/tr/execute.html')

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a+b
	context = {'result': c }
	return render(request,'first/tr/create.html',context)

def post2(request):
	a = request.POST['num1']
	# b = int(request.POST['num2'])
	c = a
	context = {'result1': c }
	return render(request,'first/tr/create.html',context)

def post3(request):
	a = request.POST['num1']
	# b = int(request.POST['num2'])
	c = a
	context = {'result2': c }
	return render(request,'first/tr/create.html',context)


def post4(request):
	a = request.POST['num1']
	# b = int(request.POST['num2'])
	c = a
	context = {'result3': c }
	return render(request,'first/tr/create.html',context)


from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import context
import csv

# add this line
from django.templatetags.static import static
def csvfile(request):
    # context = {'name':'xyz'}
    # file = open('static/csv/books.csv')
    # csvreader = csv.reader(file)
    # rows = []
    # d = dict()
    # for row in csvreader:
    #     rows.append(row)
    # for r in rows:
    #     d.update({r[0]:r[1]})
    #     print(r[0])

    # print(d["Prescot"])
    # file.close()
    context ={}
    return render(request, 'first/csv/csv.html', context)

