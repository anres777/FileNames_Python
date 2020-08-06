# LIBRERIAS A UTILIZAR
import os

dirTrabajo = "C:\\Users\\anres\\Downloads\\_JD\\_No H"
# Obtiene una lista con los nombres de todos los elementos (Carpetas y Archivos)
listaNombres = os.listdir(dirTrabajo)

listaCarpetas = []
listaArchivos = []
for x in listaNombres:
	if os.path.isdir(dirTrabajo+"\\"+x):
		listaCarpetas.append(x)
	if os.path.isfile(dirTrabajo+"\\"+x):
		listaArchivos.append(x)
	
# Renombrar, Insertar una frase al inicio o al final del elemento
# - Posicion     : es donde se colocara la nueva frase Inicio o Final
# - TipoElemento : es el tipos de elementos que se renombrara puede ser archivo o carpeta.
posicion = "final"
tipoElemento = "archivo"
fraseInsertar = ".mp4"

listaArchivosNew = []
if tipoElemento=="archivo":
	if posicion == "inicio":
		for x in listaArchivos:
			listaArchivosNew.append(fraseInsertar + x)	
	else:
		for x in listaArchivos:
			listaArchivosNew.append(x + fraseInsertar)
	# Renonbrar:
	for i in range(len(listaArchivos)):
		rutaOld = dirTrabajo +"\\"+ listaArchivos[i]
		rutaNew = dirTrabajo +"\\"+ listaArchivosNew[i]
		os.rename(rutaOld,rutaNew)
else:
	if posicion == "inicio":
		for x in listaCarpetas:
			listaCarpetasNew.append(fraseInsertar + x)	
	else:
		for x in listaCarpetas:
			listaCarpetasNew.append(x + fraseInsertar)
	# Renonbrar:
	for i in range(len(listaCarpetas)):
		rutaOld = dirTrabajo +"\\"+ listaCarpetas[i]
		rutaNew = dirTrabajo +"\\"+ listaCarpetasNew[i]
		os.rename(rutaOld,rutaNew)


