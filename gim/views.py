from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from paginaweb.models import Instrucciones


# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')

def buscar(request):
    if "busca" in request.GET and request.GET['busca']:
        consulta = request.GET["busca"]
        clase = Instrucciones.objects.all(clase__icontains=consulta)
        return render(request, 'resultados.html', {'instrucciones': clase })
    else:
        return render(request, 'resultados.html')

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = "Correo desde la biblioteca"
            contenido = formulario.cleaned_data['mensaje'] + '\n\n'
            contenido += 'Comunicarse al correo: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['jmendez@bios.edu.uy'])
            try:
                correo.send()
                return render(request, 'correo_enviado.html')
            except:
                return render(request, 'correo_no_enviado.html')
    else:
        formulario = ContactoForm()
        return render(request, 'contacto.html', {'formulario':formulario})

def usuario_nuevo(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        try:
            formulario.save()
            return render(request, 'usuario_agregado.html')
        except:
            return render(request, 'usuario_nuevo.html', {'formulario': formulario})
    else:
        formulario = UserCreationForm()
        return render(request, 'usuario_nuevo.html', {'formulario': formulario})

def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/privado')
    elif request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
            else:
                return render(request, 'no_usuario.html')
    else:
        formulario = AuthenticationForm()
        return render(request, 'ingresar.html', {'formulario':formulario})



@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render(request, 'privado.html', {'usuario': usuario})

def salir(request):
    if not request.user.is_anonymous:
        logout(request)
        return HttpResponseRedirect('/ingresar')
    else:
        return HttpResponseRedirect('')

def error_404(request, exception):
    return render(request, '404.html', {})

def error_500(request):
    return render(request, '500.html', {})

def agregar(request):
    if request.method == 'POST':
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = AutorForm()
        return render(request, 'agregar.html', {'formulario':formulario})
    