from email import message
from itertools import count
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projects
from .forms import ProjectsForm
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.urls import reverse

def proj1(request):
    project  = Projects.objects.all()
    New_proj = Projects.objects.filter(completed = True).count()
    print(New_proj)
    print(type(New_proj))
    New_id = New_proj+1
    project1 = Projects.objects.get(id = New_id)
    print(project1)
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
    return render(request, "first/app/proj1.html", {'form': form, 'proj':project, 'project1':project1})



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


def csvfile(request):
    return render(request, 'first/csv/csv.html')

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "myapp/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("myapp:upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("myapp:upload_csv"))

		file_data = csv_file.read().decode("utf-8")		

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:						
			fields = line.split(",")
			data_dict = {}
			data_dict["name"] = fields[0]
			data_dict["start_date_time"] = fields[1]
			data_dict["end_date_time"] = fields[2]
			data_dict["notes"] = fields[3]
			try:
				form = EventsForm(data_dict)
				if form.is_valid():
					form.save()					
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("myapp:upload_csv"))