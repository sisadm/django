from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from models import Task

# Create your views here.

def task_list(request):
	tasks = Task.objects.all()

	return HttpResponse(f"List of Tasks: {tasks}")

def task_details(request, id):
	task = get_object_or_404(Task, id=id)
	return HttpResponse(f"task details: {task}")

