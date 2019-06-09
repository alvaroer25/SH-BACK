# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
#import pyhdb
import mysql.connector
from mysql.connector import Error
#import cx_Oracle
import json
from core.models import img_enf,Enfermedad
#from core.models import Enfermedad
from django_project.settings import P_SERVER,P_PORT,P_USER_SERVER,P_PASSWD_SERVER
from django_project.settings import ESQUEMA_BD
# Create your views here.
def enfermedad(request):

	imagen = img_enf.objects.all()
	context = {
		'enf_list': imagen
	}

	return render(request,'core/enfermedad.html', context)

def about(request):
    return HttpResponse("""
        <h1>Mi Web Personal</h1>
        <h2>Acerca de</h2>
        <p> {"nom_enf": "Tos", "descripcion": "Definici\u00f3n de tos. Del lat\u00edn tussis, tos es un movimiento sonoro y convulsivo del aparato respiratorio de los seres humanos y de los animales. ... La presi\u00f3n dentro del t\u00f3rax hace que se estreche la tr\u00e1quea y se abra la glotis, con una diferencia de presi\u00f3n entre las v\u00edas respiratorias y la atm\u00f3sfera", "tip_enf": "MEN"}</p>
    """)

def Busqueda_img_prueba(request,cod_enf):

	possible_enf = Enfermedad.objects.filter(id_enf=cod_enf)

	enf = possible_enf[0] if len(possible_enf)==1 else None

	if enf is not None:
		context = {
			'cod_enf':cod_enf
		}
		return render(request,'core/busqueda_enfermedad.html',context)
	else:
		return HttpResponse("Enfermedad no registrada")

def Busqueda_enfermedad(request):

	lista_reporte=[]
	connection = mysql.connector.connect(
            host=P_SERVER,
            port=P_PORT,
            user=P_USER_SERVER,
            password=P_PASSWD_SERVER)
	cursor = connection.cursor()
	sql=""" SELECT * FROM %s.core_enfermedad """%(ESQUEMA_BD)
	print('---------SQL-------------')
	print(sql)
	cursor.execute(sql)
	listado = cursor.fetchall()
	
	try:
	    connection.close()
	except:
	    pass
	for s in listado:  	
		lista_reporte.append({
			'nom_enf':s[1],
			'descripcion':s[2],
			'tip_enf':s[3]
			})
	print('lista_reporte',lista_reporte)
	data = json.dumps(lista_reporte)
	return HttpResponse(data, content_type='application/json')
	#return render (request,json.dumps(lista_reporte))
def enf_imagen(request):

#	if request.method=='GET'
	lista_img=[]
	connection = mysql.connector.connect(
            host=P_SERVER,
            port=P_PORT,
            user=P_USER_SERVER,
            password=P_PASSWD_SERVER)
	cursor = connection.cursor()
	sql=""" SELECT * FROM %s.core_img_enf """%(ESQUEMA_BD)
	print('---------SQL-------------')
	print(sql)
	cursor.execute(sql)
	img = cursor.fetchall()
	
	try:
	    connection.close()
	except:
	    pass
	for s in img:  	
		lista_img.append({
			'nom_img':s[1],
			'url':s[2],
			'id_enf':s[3]
			})
	print('lista_img',lista_img)
	data = json.dumps(lista_img)
	return HttpResponse(data, content_type='application/json')

def Busqueda_por_letra(request,p_enfermedad):

	lista_enf_letra=[]
	connection = mysql.connector.connect(
            host=P_SERVER,
            port=P_PORT,
            user=P_USER_SERVER,
            password=P_PASSWD_SERVER)
	cursor = connection.cursor()

	sql="""SELECT NOMBRE, DESCRIPCION, TIPO, URL FROM %s.busqueda_x_letra_v
	 		WHERE NOMBRE LIKE '%s'"""%(ESQUEMA_BD,'%'+p_enfermedad+'%')

	print('---------SQL-------------')
	print(sql)
	cursor.execute(sql)
	lista_enf = cursor.fetchall()
	
	try:
	    connection.close()
	except:
	    pass
	for s in lista_enf:  	
		lista_enf_letra.append({
			'nomre_enf':s[1],
			'descr_enf':s[2],
			'tipo_enf':s[3],
			'url_enf':s[4]
			})
	print('lista_enf_letra',lista_enf_letra)
	data = json.dumps(lista_enf_letra)
	return HttpResponse(data, content_type='application/json')


# Create your views here.
