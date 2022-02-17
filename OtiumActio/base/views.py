from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Category
from.forms import CategoryForm
# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id': 2, 'name': 'second room python'},
    {'id': 3, 'name': 'third room python'},
]
def home(request):
    #return HttpResponse('Home page')
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'base/home.html', context)

def category(request, pk):
    #category = None
    category = Category.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'category': category}
    return render(request, 'base/category.html', context)

def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        #print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/category_form.html', context)

def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/category_form.html', context)
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj':category})
