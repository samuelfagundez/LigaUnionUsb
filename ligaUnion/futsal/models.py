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

class Jugador(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	goles = models.PositiveSmallIntegerField(default=0)
	t_amarillas = models.PositiveSmallIntegerField(default=0)
	t_rojas = models.PositiveSmallIntegerField(default=0)
	equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	p_ganados = models.PositiveSmallIntegerField(default=0)
	p_empatados = models.PositiveSmallIntegerField(default=0)
	p_perdidos = models.PositiveSmallIntegerField(default=0)
	grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Grupo(models.Model):
	numero = models.PositiveSmallIntegerField(blank=False, null=False)

	def __str__(self):
		return "Grupo Nº%s" % str(self.numero)

class Partido(models.Model):
	fecha = models.DateTimeField()
	equipo1 = models.OneToOneField('Equipo', models.SET_NULL, related_name='Equipo1', null=True)
	equipo2 = models.OneToOneField('Equipo', models.SET_NULL, related_name='Equipo2', null=True)
	estado = models.CharField(max_length=2, choices=ESTADOS, default='NJ')
	resultado1 = models.PositiveSmallIntegerField(blank=True, null=True)
	resultado2 = models.PositiveSmallIntegerField(blank=True, null=True)

	def __str__(self):
		return self.equipo1 + ' vs ' + self.equipo2
