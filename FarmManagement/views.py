# myapp/views.py
from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Animal
from .forms import AnimalForm, RemoveAnimalForm
from django.utils import timezone
from django.db.models import Count
from calendar import calendar



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def calender(request):
    return render(request, 'calender.html')

def farm_register(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_register')
    else:
        form = AnimalForm()
    
    animals = Animal.objects.filter(removal_reason__isnull=True)
    total_animals = animals.count()
    counts = {
        'cows': animals.filter(type='cow').count(),
        'goats': animals.filter(type='goat').count(),
        'camels': animals.filter(type='camel').count(),
    }

    gender_counts = {
        'cows': {'male': animals.filter(type='cow', gender='male').count(), 'female': animals.filter(type='cow', gender='female').count()},
        'goats': {'male': animals.filter(type='goat', gender='male').count(), 'female': animals.filter(type='goat', gender='female').count()},
        'camels': {'male': animals.filter(type='camel', gender='male').count(), 'female': animals.filter(type='camel', gender='female').count()},
    }

    context = {
        'animals': animals,
        'counts': counts,
        'total_animals': total_animals,
        'gender_counts': gender_counts,
        'form': form,
    }

    return render(request, 'farm_register.html', context)

def remove_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        form = RemoveAnimalForm(request.POST)
        if form.is_valid():
            removal_reason = form.cleaned_data['removal_reason']
            removal_date = timezone.now()

            animal.removal_reason = removal_reason
            if removal_reason == 'sold':
                animal.sold_date = removal_date
            elif removal_reason == 'death':
                animal.death_date = removal_date
            animal.save()
            return redirect('farm_register')
    else:
        form = RemoveAnimalForm()

    context = {
        'animal': animal,
        'form': form,
    }

    return render(request, 'remove_animal.html', context)

def sold_animals(request):
    sold_animals = Animal.objects.filter(removal_reason='sold').exclude(sold_date=None)


    sold_per_month = {}
    for animal in sold_animals:
            month =animal.sold_date.month
            if month not in sold_per_month:
                sold_per_month[month] = 0
            sold_per_month[month] += 1

    sold_per_month =[{'month':calender.month_name[month], 'count':Count} for month, count in sorted(sold_per_month.items())]
    total_sales = sum(animal.price for animal in sold_animals)
    context = {
                'sold_animals': sold_animals,
                'sold_per_month': sold_per_month,
                'total_sales': total_sales,
    }
    return render(request, 'sold_animals.html', context)

def losses(request):
    death_animals = Animal.objects.filter(removal_reason='death').exclude(death_date=None)

    death_per_month = {}
    for animal in death_animals:
        month = animal.death_date.month
        if month not in death_per_month:
            death_per_month[month] = 0
        death_per_month[month] += 1

    death_per_month =[{'month': calendar.month_name[month], 'count':Count}for month, count in sorted(death_per_month.items())]
    context = {
        'death_animals': death_animals,
        'death_per_month': death_per_month,
    }
    return render(request, 'losses.html', context)
def market_trends(request):
    return render(request, 'market_trends.html')











