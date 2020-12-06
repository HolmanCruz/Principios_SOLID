class Auto():
	capacidadPasajeros=5
	seguridad="airgab y bloqueo central."
	puertas=4

class ValoresAutos():
	Audi=47000000
	Chevrolet=27000000
	Renault=32000000
	Ford=42000000
	Wolksvagen=32000000

print("Bienvenido a Autos 2020, en nuesto consecionario, contamos con las siguientes marcas de autos:")
marcas=["Audi",	"Chevrolet", "Renault", "Ford", "Wolksvagen"]
print(marcas)

seleccionMarca=str(input("Por favor digite el nombre de la marca que desea cotizar:"))

if seleccionMarca == "Audi":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $", ValoresAutos.Audi)
elif seleccionMarca == "Chevrolet":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $", ValoresAutos.Chevrolet)
elif seleccionMarca == "Renault":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $", ValoresAutos.Renault)
elif seleccionMarca == "Ford":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $", ValoresAutos.Ford)
elif seleccionMarca == "Wolksvagen":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $", ValoresAutos.Wolksvagen)
else:	
	print("No contamos con la marca que nos indica.")

if seleccionMarca in marcas:
	print("Todos nuestro autos cuenta con una capacidad de", Auto.capacidadPasajeros, "pasajeros, además para su seguridad y tranquilidad tienen", Auto.seguridad,)
else:
	print("Gracias por su visita.")

print("fin del programa")
