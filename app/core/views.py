
from django.shortcuts import render, redirect
from core.forms import EquipoForm
from core.models import Equipos

# Create your views here.
def home(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EquipoForm()
    return render(request, "index.html", {'form': form})

def show(request):
    eq = Equipos.objects.all()
    return render(request, "show.html", {'equipo': eq})

def edit(request, id):
    eq = Equipos.objects.get(id = id)
    return render(request, "edit.html", {'equipo': eq})

def update(request, id):
    eq = Equipos.objects.get(id = id)
    form = EquipoForm(request.POST, instance = eq)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {'equipo': eq})

def delete(request, id):
    eq = Equipos.objects.get(id = id)
    eq.delete()
    return redirect("/show")