# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

LEVE = 'LEV'
GRAVE = 'GRAV'
MENOR = 'MEN'

TIPOS_ENF = (
	(LEVE,'Leve'),
	(GRAVE,'Grave'),
	(MENOR,'Menor')
	)

class Medicina(models.Model):

	nom_med = models.CharField(max_length=150)
	id_medicina = models.AutoField(primary_key=True)
	descripcion = models.TextField(default="")

	def __str__(self):
		return self.nom_med

class img_med(models.Model):

	nom_imd = models.CharField(max_length=150)
	id_med = models.AutoField(primary_key=True)
	url_md = models.URLField()
	id_med = models.ForeignKey(Medicina,on_delete=models.CASCADE,)

	def __str__(self):
		return self.nom_imd

class Enfermedad(models.Model):
	
	nom_enf = models.CharField(max_length=150)
	id_enf = models.AutoField(primary_key=True)
	descripcion = models.TextField(default="")
	tip_enf = models.CharField(max_length=3,choices=TIPOS_ENF)

	def __str__(self):
		return self.nom_enf

class Sistema(models.Model):

	nom_sis = models.CharField(max_length=150)
	id_sis = models.AutoField(primary_key=True)
	id_enf = models.ForeignKey(Enfermedad,on_delete=models.CASCADE)

	def __str__(self):
		return self.nom_sis

class img_enf(models.Model):

	nom_ime = models.CharField(max_length=150)
	id_enfimg = models.AutoField(primary_key=True)
	url_enf = models.URLField()
	id_enf = models.ForeignKey(Enfermedad,on_delete=models.CASCADE)

	def __str__(self):
		return self.nom_ime

# Create your models here.
