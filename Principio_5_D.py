class Menu():
	comida=["hamburgesa", "pizza", "perro caliente", "salchipapa"]
	bebida=["Limonada", "gaseosa", "té", "cerveza"]
	acompanamiento=["tocineta", "papas", "patacones"]


class DomicilioA():
	cliente="Mauricio"
	pedido=Menu.comida[2],Menu.bebida[0]
	adicional=Menu.acompanamiento[1]

class DomicilioB():
	cliente="Juliana"
	pedido=Menu.comida[1],Menu.bebida[2]
	adicional=Menu.acompanamiento[0]

class DomicilioC():
	cliente="David"
	pedido=Menu.comida[0],Menu.bebida[3]
	adicional=Menu.acompanamiento[2]

class DomicilioD():
	cliente="Angela"
	pedido=Menu.comida[3],Menu.bebida[3]
	adicional=Menu.acompanamiento[2]

class DomicilioE():
	cliente="Sofia"
	pedido=Menu.comida[2],Menu.bebida[2]
	adicional=Menu.acompanamiento[0]

print("Listado de domicilios de Food Speed Center")

print(DomicilioA.cliente,"solicito un domicilio de combo de:",DomicilioA.pedido,"acompañada de",DomicilioA.adicional)
print(DomicilioB.cliente,"solicito un domicilio de combo de:",DomicilioB.pedido,"acompañada de",DomicilioB.adicional)
print(DomicilioC.cliente,"solicito un domicilio de combo de:",DomicilioC.pedido,"acompañada de",DomicilioC.adicional)
print(DomicilioD.cliente,"solicito un domicilio de combo de:",DomicilioD.pedido,"acompañada de",DomicilioD.adicional)
print(DomicilioE.cliente,"solicito un domicilio de combo de:",DomicilioE.pedido,"acompañada de",DomicilioE.adicional)

print("fin del programa")




