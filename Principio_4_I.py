class IAve():
	actividad="comer"

class IAveVoladora():
	actividad="volar"

class IAveNadadora():
	actividad="nadar"

class IAveHabladora():
	actividad="Hablar"

class IAveSilvadora():
	actividad="Silvar"


class Loro():
	tipo="loro"
	actividades=IAve.actividad, IAveVoladora.actividad, IAveHabladora.actividad

class Canario():
	tipo="canario"
	actividades=IAve.actividad, IAveVoladora.actividad, IAveSilvadora.actividad

class Guacamaya():
	tipo="guacamaya"
	actividades=IAve.actividad, IAveVoladora.actividad,


print("El",Loro.tipo,"puede",Loro.actividades)
print("El",Canario.tipo,"puede",Canario.actividades)
print("La",Guacamaya.tipo,"puede",Guacamaya.actividades)

print("fin del programa")
