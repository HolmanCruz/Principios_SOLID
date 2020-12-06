print("Bienvenido a Autos 2020, en nuesto consecionario, contamos con las siguientes marcas de autos:")
marcas=["Audi",	"Chevrolet", "Renault", "Ford", "Wolksvagen"]
print(marcas)

seleccionMarca = str(input("Por favor digite el nombre de la marca que desea cotizar:"))

if seleccionMarca == "Audi":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $47.000.000")
elif seleccionMarca == "Chevrolet":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $27.000.000")
elif seleccionMarca == "Renault":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $32.000.000")
elif seleccionMarca == "Ford":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $42.000.000")
elif seleccionMarca == "Wolksvagen":
	print("Ha seleccionado la marca "+seleccionMarca+", Tenemos referencia de esta marca desde tan solo $37.000.000")
else:
	print("No contamos con la marca que nos indica.")

print("fin del programa")