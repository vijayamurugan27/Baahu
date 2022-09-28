from email import message
from itertools import count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projects
from .forms import ProjectsForm
from django.db.models import Q

def proj1(request):
    project  = Projects.objects.all()
    # print(project)
    # print('a') 
    # proj = [project]
    # for i in proj:
    #     print(proj)
    # #     print(proj)
    # print('b')
    # queryset = Projects.objects.filter(
    # Q(completed ='True') & Q(val1='True')
    # ).values_list('id', 'name', 'completed', 'val1')
    # print(queryset) 
    # print('d')
    # qs = Projects.objects.values('name').annotate(name_count=count('name')).filter(Q(completed ='True') & Q(val1='True'))

    if request.method =="POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ProjectsForm()
    return render(request, "first/app/proj1.html", {'form': form, 'proj':project})



def detail_product(request, id): # detail view
    project  = Projects.objects.get(id=id)
    print(project)
    context = {"project" :project}
    return render(request, "first/app/proj2.html", context)


def update(request, id):
	project  = Projects.objects.get(id=id)
	form = ProjectsForm(request.POST or None, instance = project)
	data = Projects.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('proj1')

	context = {'form':form, 'data':data}
	return render(request,'first/app/proj3.html', context )

def delete(request, id): # detail view
    project  = Projects.objects.get(id=id)
    context = {"project" :project}
    if request.method =='POST':
        project.delete()
        return redirect('home')
    return render(request, "first/app/proj4.html", context)


    
