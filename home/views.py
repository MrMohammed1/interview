from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def create_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')  
        
    return render(request, 'create_person.html', {'form': form})

def person_list(request):
    persons = Person.objects.all()
    if persons:
        return render(request, 'person_list.html', {'persons': persons})
    else:
        return redirect('create_person')  

def person_detail(request, person_id):
    person = Person.objects.get(pk=person_id)
    return render(request, 'person_detail.html', {'person': person})


def update_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'update_person.html', {'form': form})

def delete_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'delete_person.html', {'person': person})

