from django.shortcuts import render, redirect
from . forms import CreateForm
from django.contrib import messages




def home(request):
	context = {}
	return render(request, 'index.html', context)


def create(request):
	form = CreateForm()
	if request.method == "POST":
		form = CreateForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'File uploaded successfully..!')
			return redirect('create')
		else:
			print("not valid")
	context = {'form':form}
	return render(request, 'create.html', context)