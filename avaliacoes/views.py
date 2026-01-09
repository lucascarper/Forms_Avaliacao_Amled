from django.shortcuts import render, get_object_or_404, redirect
from condutores.models import Condutor
from .models import Condutor, Avaliacao

def condutor_avaliar(request, id):
    condutor = get_object_or_404(Condutor, id=id)

    if request.method == 'POST':
        resultado = request.POST.get('resultado')
        observacoes = request.POST.get('observacoes')

        Avaliacao.objects.create(
            condutor=condutor,
            resultado=resultado,
            observacoes=observacoes
        )

        return redirect('condutores_listar')

    return render(request, 'condutores/avaliar.html', {
        'condutor': condutor
    })