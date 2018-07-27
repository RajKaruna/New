from django.shortcuts import render,redirect
from django.contrib import messages
from .models import List


def home(request):
	if request.method == "POST": 
		if "taskAdd" in request.POST:
			todos = List.objects.all() 
			item=request.POST["description"]
			date = str(request.POST["date"]) #date
			
			Todo = List(item=item, date=date)
			Todo.save() #saving the todo 
			messages.success(request,('Item Has Been Added..!!'))
			return render(request, "base.html", {"todos": todos,})
	else:
		todos = List.objects.all() 
		return render(request, "base.html", {"todos": todos,})


def delete(request,list_id):
	todos=List.objects.get(pk=list_id)
	todos.delete()
	messages.success(request,('Item Has Been Deleted..!!'))
	return redirect ('base.html')



def cross_off(request,list_id):
	todos = List.objects.get(pk=list_id)
	todos.completed = True
	messages.success(request,('Item Has Been Done..!!'))
	todos.save()
	return redirect('base.html')

def uncross(request,list_id):
	todos = List.objects.get(pk=list_id)
	todos.completed = False
	messages.success(request,('Item again marked as Pending..!!'))
	todos.save()
	return redirect('base.html')


def edit(request,list_id):

	if request.method == "POST":
		todos = List.objects.get(pk=list_id)
		data = request.POST
		item = data['item']
		Todo = List(item=item, pk=list_id)
		Todo.save()
	

		
		messages.success(request,('Item Has Been Edited..!!'))
		return redirect ('base.html')

	else:
		item = List.objects.get(pk = list_id)
		return render (request, 'edit.html', {'item': item})










