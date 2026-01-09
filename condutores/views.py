from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Condutor
from .forms import CondutorForm

@login_required
def condutor_list(request):
    condutores = Condutor.objects.all()
    return render(request, 'condutores/list.html', {'condutores': condutores})


@login_required
def condutor_create(request):
    if request.method == 'POST':
        form = CondutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('condutor_list')
    else:
        form = CondutorForm()

    return render(request, 'condutores/form.html', {'form': form})


@login_required
def condutor_update(request, id):
    condutor = get_object_or_404(Condutor, id=id)

    if request.method == 'POST':
        form = CondutorForm(request.POST, request.FILES, instance=condutor)
        if form.is_valid():
            form.save()
            return redirect('condutor_list')
    else:
        form = CondutorForm(instance=condutor)

    return render(request, 'condutores/form.html', {'form': form})


@login_required
def condutor_delete(request, id):
    condutor = get_object_or_404(Condutor, id=id)

    if request.method == 'POST':
        condutor.delete()
        return redirect('condutor_list')

    return render(request, 'condutores/delete.html', {'condutor': condutor})

@login_required
def condutor_avaliar(request, pk):
    condutor = get_object_or_404(Condutor, pk=pk)

    return render(request, 'condutores/avaliar.html', {
        'condutor': condutor
    })