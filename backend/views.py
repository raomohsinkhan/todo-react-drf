from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
# Create your views here.

def home(request):
	return render(request, 'home.html', {'name':'I am a good boy.'})
	#return HttpResponse("Hello World!<br>I am Rao Mohsin learning Python Django.")
def index(request):
    return render(request, 'home.html')

def add(request):
	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	myres = val1 + val2
	return render(request, 'result.html', {'results':myres})

def home2(request):
	return render(request, 'home2.html', {'name':'I am a good boy. and this is a home2 page'})
	#return HttpResponse("Hello World!<br>I am Rao Mohsin learning Python Django.")

def divide(request):
	return render(request, 'home2.html', {'name':'I am a good boy. and this is a divide page'})

def multiplay(request):
	return render(request, 'home2.html', {'name':'I am a good boy. and this is a multiplay page'})



@api_view(['GET'])
def api_details(request):
    api_endpoints = {
        "api_version" : "v1",
        "get all tasks" : "/task-list/",
        "Create task" : "/task-create/",
        "Read task" : "/task/<int:pk>/",
        "Update task" : "/task-update/<int:pk>/",
        "Delete task" : "/task-delete/<int:pk>/",
    }
    return Response(api_endpoints)

@api_view(['GET'])
def get_all_tasks(request):
    tasks = Task.objects.all()
    task_list= []

    for task in tasks:
        result = {
            "pk":task.pk,
            "title":task.title,
            "completed":task.completed
        }
        task_list.append(result)
    
    return Response(task_list)

@api_view(['GET'])
def get_task(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        return Response({"message":"Task does not exist"},status=404)

    result = {
        "pk":task.pk,
        "title":task.title,
        "completed":task.completed
    }
    return Response(result)

@api_view(['POST'])
def create_task(request):
    title = request.data['title']

    task = Task.objects.create(title=title)
    task.save()
    return Response({"message":"Task inserted successfully"})

@api_view(['PUT'])
def update_task(request,pk):
    title = request.data['title']
    completed = request.data['completed']

    task = Task.objects.get(pk=pk)
    task.title = title
    task.completed = completed
    task.save()
    return Response({"message":"Task updated successfully"})

@api_view(['DELETE'])
def delete_task(request,pk):
    task = Task.objects.filter(pk=pk).delete()
    return Response({"message":"Task deleted successfully"})

