
#imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Animals
from .forms import AnimalForm
#views
def animals(request):
    animals=Animals.objects.all()
    return render(request,'animals/home.html',{'animals':animals})
    
def detail(request,id):
    detail=get_object_or_404(Animals,id=id)
    return render(request,'animals/detail.html',{'detail':detail})

def edit(request,id):
    
    animal=get_object_or_404(Animals,id=id)
    if request.method=='POST':


        animal_form=AnimalForm(request.POST,instance=animal)
        if animal_form.is_valid(): 
            animal_form.save()
            return redirect('aplication:animals')
    else:
        animal_form=AnimalForm()
        return render(request,'animals/edit.html',{'animal_form':animal_form})

def create(request):
    if request.method == 'POST':
        animal_form= AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save()
            return redirect('aplication:animals')
    else:
        animal_form=AnimalForm()
    return render(request,'animals/create.html',{'animal_form':animal_form})
def delete(request,id):
    animal=get_object_or_404(Animals,id=id)
    if animal:
        animal.delete()
        return redirect('aplication:animals')
def home(request):
    pass
