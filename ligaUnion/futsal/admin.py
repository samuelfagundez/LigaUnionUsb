from django.contrib import admin
from .models import Jugador, Equipo, Grupo, Partido

# Register your models here.

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Grupo)
admin.site.register(Partido)