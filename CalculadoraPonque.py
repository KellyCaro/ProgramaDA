from ClaseIngredientes import Ingredientes
from ClasePonqueDeNaranja import IngredientesPN
from ClasePonqueChocolate import IngredientesPC
from ClasePonqueMantequilla import IngredientesPDM

from ClaseFondant import Fondant

from ClaseRellenoVainilla import RellenoVainilla
from ClaseRellenoVainilla2 import RellenoVainilla2
from ClaseRellenoArequipe import RellenoArequipe
from ClaseRellenoChocolate import RellenoChocolate
from ClaseRellenoFrutal import RellenoFrutal
from ClaseRellenoCafe import RellenoCafe
from ClaseRellenoCafe2 import RellenoCafe2
from ClaseRedVelvet import PonqueRedVelvet
from Brownie import IngredientesBRO

class calculadora:
    

    def __init__(self):
        print("")

    #Costo Brownie
    def costoBRO(self):
        suma=0
        ponque=IngredientesBRO()
        listaPonque=ponque.consultar_Ingredientes()
        for i in listaPonque:
            suma+=i[2]
        return(suma)

    #costo relleno vainilla por 1 lamina   
    def costoRV(self):
        rellenoVainilla=  RellenoVainilla()
        suma=0
        lista= rellenoVainilla.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)
    #costo relleno vainilla por 2 lamina   
    def costoRV2(self):
        rellenoVainilla2=  RellenoVainilla2()
        suma=0
        lista= rellenoVainilla2.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)
    #costo relleno Arequipe por 1 lamina
    def costoRA(self):
        rellenoArequipe= RellenoArequipe()
        suma=0
        fondant = Fondant()
        lista= rellenoArequipe.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)
    #costo relleno Cafe por 1 lamina
    def costoRCA(self):
        rellenoCafe= RellenoCafe()
        suma=0
        lista= rellenoCafe.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)
    #costo relleno Cafe por 2 lamina
    def costoRCA(self):
        rellenoCafe2= RellenoCafe2()
        suma=0
        lista= rellenoCafe2.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)

    #costo relleno Chocolate por 2 lamina
    def costoRCH(self):
        relleno= RellenoChocolate()
        suma=0
        lista= relleno.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)    
    #costo Frutal por 2 lamina
    def costoRF(self):
        relleno= RellenoFrutal()
        suma=0
        lista= relleno.consultar_Ingredientes()
        for i in lista:
            suma+=i[2]
        return(suma)
    
    #costo fondant por 3kilos
    def costoFon(self):
        sumaFon=0
        fondant = Fondant()
        listaFon= fondant.consultar_Ingredientes()
        for i in listaFon:
            sumaFon+=i[2]
        return(sumaFon)
    
    #costo ponque de mantequilla
    
    def costoPMantequilla(self):
        sumaMan=0
        mantequilla= IngredientesPDM()
        listaMan= mantequilla.consultar_Ingredientes()
        for i in listaMan:
            sumaMan+=i[2]
        return(sumaMan)
    #costo ponque de naranja
    
    def costoPNaranja(self):
        sumaNa=0
        naranja=IngredientesPN()
        listaNara = naranja.consultar_Ingredientes()
        for i in listaNara:
            sumaNa+=i[2]
        return(sumaNa)
    #costo ponque de chocolate
    def costoPChocolate(self):
        chocolate=IngredientesPC()
        listaChoco= chocolate.consultar_Ingredientes()
        sumaChoco=0
        for i in listaChoco:
            sumaChoco+=i[2]

        return(sumaChoco)
    #costo ponque Red velvet
    def costoPRED(self):
        suma=0
        ponque=PonqueRedVelvet()
        listaPonque=ponque.consultar_Ingredientes()
        for i in listaPonque:
            suma+=i[2]

        return(suma)
    
#costo_fondant_por_cupcake
CFPC=(calculadora().costoFon()/3000)*40
#costo_MassCream_por_cupcake
CMCPC=((12000*125/1000)/6)
#costo relleno por cupcake
CRPC= 10*calculadora().costoRV2()/300
print("CRPC",CRPC)

#costo_fondant_por_Torta 10 porciones
CFPPF=(calculadora().costoFon()/3000)*270
#costo_fondant_por_Torta 10 porciones medio
CFPPM=(calculadora().costoFon()/3000)*400
#costo_fondant_por_Torta 10 porciones Alto
CFPPD=(calculadora().costoFon()/3000)*600
'''print("Fondant: ",sumaFon)
print("Masa naranja: ",sumaNa,"Masa de  naraja con fondat",sumaNa+ (sumaFon/3000*200))

massCream= 12000/900  *150
ponquePor6= sumaNa/15*6
print("ponque * 6 unidades", ponquePor6)
print("Ganancia de la caja de cupcakes por 6:", 27000-(20*sumaFon/3000*6 + ponquePor6 + massCream +1800))

print("Relleno de arequipe: ",sumaAre)
print("Suma arequipe+con vainilla, con torta de 10 a 15 porciones ponque de naranja mas fondant: ",int(sumaNa+ (sumaFon/3000*200)+sumaAre+sumaVai))'''


print("costo ponque de naranja: {}".format(calculadora().costoPNaranja()+calculadora().costoRF()))
print("costo ponque de Chocolate: {}".format(calculadora().costoPChocolate()))
print("costo ponque de Mantequilla: {}".format(calculadora().costoPMantequilla()))
print("costo ponque de Fondant por 3 kilos: {}".format(calculadora().costoFon()))
print("costo ponque de Relleno de arequipe por lamina: {}".format(calculadora().costoRA()))
print("costo ponque de Red velvet y ganache de vainilla: {}".format(calculadora().costoPRED()))
print((calculadora().costoFon()*270/3000)+calculadora().costoPRED()+calculadora().costoRV2())

print("Precio de los cupcakes")
print("Masa de naranja = 15 salen precio por unidad cupcakes: {} ".format((calculadora().costoPNaranja()/15)))
print((calculadora().costoPNaranja()/15)+CFPC+CMCPC+CRPC)
print("Masa de Negra = 22 cupcakes: {}".format(format((calculadora().costoPChocolate()/22))))
print((calculadora().costoPChocolate()/22)+CFPC+CMCPC+CRPC)
print("********************************************************")


print("Costo del ponque de 10 porciones diseño Facil:",calculadora().costoPChocolate()+calculadora().costoRCA()+CFPPF+3000)
print("Costo del ponque de 10 porciones diseño Medio:",calculadora().costoPChocolate()+calculadora().costoRCA()+CFPPM+3000)
print("Costo del ponque de 10 porciones diseño Dificil:",calculadora().costoPChocolate()+calculadora().costoRCA()+CFPPD+3000)

print("********************************************************")

print("Costo del ponque de 30 porciones diseño Facil:",(calculadora().costoPChocolate()*2)+(calculadora().costoRCA()*2)+(CFPPF*1.4)+4000)
print("Costo del ponque de 30 porciones diseño Medio:",(calculadora().costoPChocolate()*2)+(calculadora().costoRCA()*2)+(CFPPM*1.6)+4000)
print("Costo del ponque de 30 porciones diseño Dificil:",(calculadora().costoPChocolate()*2)+(calculadora().costoRCA()*2)+(CFPPM*1.8)+4000)

print("***************************************************************************************************")
print("Costo del ponque de 30 porciones diseño Facil:",(calculadora().costoPChocolate()*3)+(calculadora().costoRCA()*3)+(CFPPF*2.5)+5000)
print("Costo del ponque de 30 porciones diseño Medio:",(calculadora().costoPChocolate()*3)+(calculadora().costoRCA()*3)+(CFPPM*2.7)+5000)
print("Costo del ponque de 30 porciones diseño Dificil:",(calculadora().costoPChocolate()*3)+(calculadora().costoRCA()*3)+(CFPPM*2.9)+5000)



