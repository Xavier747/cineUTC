from django.contrib import admin
from .models import Genero
admin.site.register(Genero)
from .models import Director
admin.site.register(Director)
from .models import Pais
admin.site.register(Pais)
from .models import Peliculas
admin.site.register(Peliculas)
from .models import Cine
admin.site.register(Cine)


# Register your models here.
