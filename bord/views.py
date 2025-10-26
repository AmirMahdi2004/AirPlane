from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .services import *


# Create your views here.
@login_required
def airplane_list(request):
    airplanes = Airplane.objects.filter(owner=request.user)
    context = {'airplanes': airplanes}
    return render(request, 'bord/airplane_list.html', context)


@login_required
def sll_view(request, pk):
    airplane = Airplane.objects.get(id=pk)
    conditions = ServiceLifeLimited.objects.all()
    context = {
        'airplane': airplane,
        'conditions': conditions,
    }
    return render(request, 'bord/service_life_limited.html', context)


@login_required
def mp_view(request, pk):
    airplane = Airplane.objects.get(id=pk)
    mp = MP.objects.all()

    context = {
        'airplane': airplane,
        'mp': mp,
    }
    return render(request, 'bord/mp_view.html', context)


@login_required
def flt_view(request, pk):
    airplane = Airplane.objects.get(id=pk)
    flt = FltHrs.objects.all()
    context = {
        'airplanes': airplane,
        'flt': flt,
    }

    return render(request, 'bord/flt.html', context)


@login_required
def sll_form(request):
    airplanes = Airplane.objects.filter(owner=request.user)
    if request.method == 'POST':
        form = SLLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bord:airplane')
    else:
        form = SLLForm()
    context = {
        'form': form,
        'airplanes': airplanes,
    }
    return render(request, 'bord/sll_form.html', context)


@login_required
def mp_form(request):
    airplanes = Airplane.objects.filter(owner=request.user)
    if request.method == 'POST':
        form = MpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bord:airplane')
    else:
        form = MpForm()
    context = {
        'form': form,
        'airplanes': airplanes,
    }
    return render(request, 'bord/mp_form.html', context)


@login_required
def flt_form(request):
    airplanes = Airplane.objects.filter(owner=request.user)
    if request.method == 'POST':
        form = FltHrsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bord:airplane')
    else:
        form = FltHrsForm()
    context = {
        'form': form,
        'airplanes': airplanes,
    }
    return render(request, 'bord/flt_form.html', context)


@login_required
def input_bord(request):
    if request.method == 'POST':
        form = InputBordForm(request.POST)
        if form.is_valid():
            form.save()
            MaintenanceService(form).save_sll()
            return redirect('bord:airplane')
    else:
        form = InputBordForm()
    context = {
        'form': form,
    }
    return render(request, 'bord/input_bord.html', context)
