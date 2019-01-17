from django.db import models

# Create your models here.

PUNTOS = {
	'ganado' : 3,
	'empadato' : 1,
	'perdido' : 0
}
ESTADOS = (
	('NJ', 'No Jugado'),
	('EV', 'En Vivo'),
	('TE', 'Terminado')
) 

class Jugado(models.Model):
	nombre = models.CharField(max_length=100, blank=False, Null=False)
	goles = models.PositiveSmallIntegerField(default=0)
	t_amarillas = models.PositiveSmallIntegerField(default=0)
	t_rojas = models.PositiveSmallIntegerField(default=0)
	equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)

class Equipo(models.Model):
	nombre = models.CharField(max_length=100, blank=False, Null=False)
	p_ganados = models.PositiveSmallIntegerField(default=0)
	p_empatados = models.PositiveSmallIntegerField(default=0)
	p_perdidos = models.PositiveSmallIntegerField(default=0)
	grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)

class Grupo(models.Model):
	numero = models.PositiveSmallIntegerField(blank=False, Null=False)

class Partido(models.Model):
	fecha = models.DateTimeField()
	equipo1 = models.OneToOneField('Equipo', models.SET_NULL)
	equipo2 = models.OneToOneField('Equipo', models.SET_NULL)
	estado = models.CharField(max_length=2, choices=ESTADOS, default='NJ')
