from django.shortcuts import redirect, render
from weasyprint import HTML
from Aplicaciones.Cartelera.models import Director, Genero, Pais, Peliculas, Cine
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Creamos una nueva vista
def home(request):
    return render(request, "home.html")

def gestionCines(request):
    return render(request, "gestionCines.html")

def ListadoGenero(request):
    generosBdd = Genero.objects.all()
    return render(request, "ListadoGenero.html", {'genero': generosBdd})

def EliminarGenero(request, id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, "Eliminado exitosamente.")
    return redirect('ListadoGenero')

def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')

def guardarGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get("foto")
    nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, "Género registrado exitosamente.")
    return redirect('ListadoGenero')

def editarGenero(request, id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar': generoEditar})

def procesoActualizacionGenero(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = descripcion
    generoConsultado.save()
    messages.success(request, 'Género actualizado exitosamente.')
    return redirect('ListadoGenero')

def ListadoPelicula(request):
    peliculasBdd = Peliculas.objects.all()
    return render(request, "ListadoPelicula.html", {'peliculas': peliculasBdd})

def ListadoPais(request):
    paisBdd = Pais.objects.all()
    return render(request, "ListadoPais.html", {'pais': paisBdd})

def EliminarPais(request, id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "Eliminado exitosamente.")
    return redirect('ListadoPais')

def nuevoPais(request):
    return render(request, 'nuevoPais.html')

def guardarPais(request):
    nombre = request.POST["nombre"]
    continente = request.POST["continente"]
    capital = request.POST["capital"]
    nuevoPais = Pais.objects.create(nombre=nombre, continente=continente, capital=capital)
    messages.success(request, "País registrado exitosamente.")
    return redirect('ListadoPais')

def editarPais(request, id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar': paisEditar})

def procesoActualizacionPais(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']
    paisConsultado = Pais.objects.get(id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request, 'País actualizado exitosamente.')
    return redirect('ListadoPais')

def ListadoDirector(request):
    directorBdd = Director.objects.all()
    return render(request, "ListadoDirector.html", {'director': directorBdd})

def EliminarDirector(request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Eliminado exitosamente.")
    return redirect('ListadoDirector')

def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')

def guardarDirector(request):
    dni = request.POST["dni"]
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    estado = request.POST["estado"] == "True"
    fot = request.FILES.get("foto")
    nuevoDirector = Director.objects.create(dni=dni, apellido=apellido, nombre=nombre, estado=estado, foto=fot)
    messages.success(request, "Director registrado exitosamente.")
    return redirect('ListadoDirector')

def editarDirector(request, id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

def procesoActualizacionDirector(request):
    id = request.POST['id']
    dni = request.POST['dni']
    apellido = request.POST['apellido']
    nombre = request.POST['nombre']
    estado = request.POST['estado'] == "True"
    directorConsultado = Director.objects.get(id=id)
    directorConsultado.dni = dni
    directorConsultado.apellido = apellido
    directorConsultado.nombre = nombre
    directorConsultado.estado = estado
    directorConsultado.save()
    messages.success(request, 'Director actualizado exitosamente.')
    return redirect('ListadoDirector')

#insertando cine mediante AJAX en la base de datos

@csrf_exempt
def guardarCine(request):
    
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
                
            if isinstance(data, list):
                respuesta = []
                for cine_data in data:
                    nom = cine_data.get("nombre")
                    dir = cine_data.get("direccion")
                    tel = cine_data.get("telefono")
                    nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
                    respuesta.append({
                        'estado': True,
                        'mensaje': 'Cine registrado exitosamente.',
                        'cine': nuevoCine.id
                    })
                return JsonResponse(respuesta, safe=False)
            else:
                nom = data.get("nombre")
                dir = data.get("direccion")
                tel = data.get("telefono")
                nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
                return JsonResponse({
                    'estado': True,
                    'mensaje': 'Cine registrado exitosamente.',
                    'cine': nuevoCine.id
                })
        except json.JSONDecodeError:
            return JsonResponse({
                'estado': False,
                'mensaje': 'JSON inválido.'
            })
    elif request.method == 'GET':
        cines = Cine.objects.all()
        cines_json = serializers.serialize('json', cines)
        return JsonResponse(cines_json, safe=False)
    else:
        return JsonResponse({
            'estado': False,
            'mensaje': 'Método no permitido.'
        })
    
    
def listadoCines(request):
    cinesBdd=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines':cinesBdd})

def exportCines(request):
    cinesBdd = Cine.objects.all()
    return render(request,"exportCines.html", {'cines': cinesBdd})

def exportCinesPDF(request):
    #llamar a todos los datos del modelo cina
    cines = Cine.objects.all()
    #llamar al template con el render string
    html_string = render_to_string('exportCines.html', {'cines': cines}) # type: ignore
    #almacenar como un archivo html
    html = HTML(string=html_string)
    #leer todo el html guardado y convvertirlo en un pdf
    pdf = html.write_pdf()
    #dar una respuesta como pdf(archivo)
    response = HttpResponse(pdf, content_type='application/pdf')
    #nombrar y dar una extension al archivo expotado
    response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
    #exportar archivo
    return response