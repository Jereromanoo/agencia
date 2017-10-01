from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from app.core.forms import RegistroDesocupado, RegistroEmpresa

@login_required
def home(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'home.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})

def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})

# Estas son las que ya estaban, las comento porque con el cambio alguna cosa
# podría tener que cambiarse o adaptarse. Notece ademas el uso de login_required
# en el views en lugar de urls, los decorators de hecho son esas cosas que
# comienzan con @ y van arriba de la función
"""
@login_required
def desocupados_list(request):
    return render(request, "agenciaP/desocupados_list.html")

@login_required
def trabajos_list(request):
    return render(request, "agenciaP/trabajos_list.html")

def trabajos_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('redireccion', request=request)
    else:
        form =JobForm()
    return render(request, 'agenciaP/registrartrabajo.html', {'form':form})

def editar(request, user):
    desocupado = Perfiles.objects.get(usuario=user)
    if request.method == 'GET':
        form = UserForm(instance=desocupado)
    else:
        form = UserForm(request.POST, instance=desocupado)
        if form.is_valid:
            form.save()
        return redirect('redireccion')
    return render(request, 'agenciaP/registrar.html', {'form':form})
"""