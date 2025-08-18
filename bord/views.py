from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FltHrsForm
from .models import *


# Create your views here.


@login_required
def service_life_limited_view(request):
    airplanes = Airplane.objects.all()
    conditions = ServiceLifeLimited.objects.all()
    context = {
        'airplanes': airplanes,
        'conditions': conditions,
    }
    return render(request, 'bord/service_life_limited.html', context)


@login_required
def mp_view(request):
    airplanes = Airplane.objects.all()
    mp = MP.objects.all()
    context = {
        'airplanes': airplanes,
        'mp': mp,
    }
    return render(request, 'bord/mp_view.html', context)

@login_required
def flt(request):
    airplanes = Airplane.objects.all()
    flt = FltHrs.objects.all()
    context = {
        'airplanes': airplanes,
        'flt': flt,
    }

    return render(request, 'bord/flt.html', context)

@login_required
def flt_view(request):
    if request.method == 'POST':
        form = FltHrsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flt')
    else:
        form = FltHrsForm()
    context = {
        'form': form,
    }
    return render(request, 'bord/flt_form.html', context)

