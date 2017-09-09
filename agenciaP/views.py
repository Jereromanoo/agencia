from django.shortcuts import render

# Create your views here.
def desocupados_list(request):
        return render(request, 'agenciaP/desocupados_list.html', {})