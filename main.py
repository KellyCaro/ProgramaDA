
from clasePrincipal import *
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# el Menu esta amarrado a los imgredientes, a la actualización de datos y a la calculadora de costos
#para crear una nueva receta debo crear una nueva base de datos
#agregar un archivo con la clase de la receta
#cambiar los nombres para que coincidan con los de la base de datos
#revisar primero que los datos de la actualización de archivos este correcta
# ya que sin eso no va a funcionar la calculadora de costos y va a botar error
#revisar
conect=Conexion()
miConexion=Conexion().conexion()
misRecetas= Recetas()
misIngredientes=Ingredientes()

tablaIngredientes=Conexion().sql_table(miConexion,"Ingredientes( name text PRIME KEY, cantidadXGramosUni integer, precioTotal integer, PrecioUnitario integer)")




def Menu():



    porciones= int(input("escribe la cantidad de porciones que deseas para tu pastel\n1)10-15\n2)20-25\n3)30-35\n"))
    relleno=input('''Selecciona que tipo de relleno deseas
		  1)Relleno de Vainilla
		  2)Relleno  de Arequipe
		  3)Relleno de chocolate
		  4)Relleno de Cafe
		  5)Relleno frutal\n''')
    adicion=input("Selecciona la adición que deseas agregar\n1)Ninguno")
    if relleno == "1":
        costo=(tipoDePonque*porciones)+(calculadora().costoRV2()*porciones)
        print("El costo de tu pastel  es de {}, incluye, el relleno ponque y cantidad de porciones".format(tipoDePonque,costo))
    elif relleno == "2":
        costo=(tipoDePonque*porciones)+(calculadora().costoRA()*porciones)+(calculadora().costoRV()*porciones)
        print("El costo de tu pastel  es de {}, incluye, el relleno ponque y cantidad de porciones".format(costo))

    elif relleno == "3":
        costo=(tipoDePonque*porciones)+(calculadora().costoRCH()*porciones)
        print("El costo de tu pastel  es de {}, incluye, el relleno ponque y cantidad de porciones".format(costo))
    elif relleno == "4":
        costo=(tipoDePonque*porciones)+(calculadora().costoRCA()*porciones)
        print("El costo de tu pastel  es de {}, incluye, el relleno ponque y cantidad de porciones".format(costo))
    elif relleno == "5":
        costo=(tipoDePonque*porciones)+(calculadora().costoRF()*porciones)
        print("El costo de tu pastel  es de {}, incluye, el relleno ponque y cantidad de porciones".format(costo))




    else:
	    print("Seleccione una opcion correcta")





def principalMain():
    selector=input('''Selecciona
		  1)Ingredientes
		  2)Recetas
		  3)Costo de recetas\n''')

    if selector == "1":
        misIngredientes.menuIngredientes()

        Ingredientes()
    elif selector== "2":
        misRecetas.menuRecetas()
    else:
        print("por favor digite una opción válida")
        print("*********************")
        principalMain()
        clearConsole()
principalMain()
