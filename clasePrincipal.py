import sqlite3
from sqlite3 import Error
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


"""Si tengo que acceder a las listas de sql lite tengo que pasar como parametro y este codigo
cursorObj = conexion.cursor()
datos = Client_data
cursorObj.execute('''INSERT INTO cliente VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',datos)

"""
"""CLASE CONEXION"""
class Conexion:
    def __init__(self):
        pass



    def conexion(self):

        try:
            conexion= sqlite3.connect('basesDeDatosDA.db')
            return conexion
        except Error:
            print(Error)



    def sql_table(self,conexion,str):
        #se utiliza el metodo cursos, permita hacer las sentencias
        try:
            cursorObj = conexion.cursor()
            crearTablaPlan="CREATE TABLE {}".format(str)
            cursorObj.execute(crearTablaPlan)
            conexion.commit()
        except:

            pass





class Ingredientes:
    def __init__(self):
        pass

    def verificacionIngrediente(self,conexion,producto):
        self.producto=producto
        cursorObj = conexion.cursor()

        consultarTabla="SELECT * FROM Ingredientes WHERE name='{}'".format(self.producto)
        cursorObj.execute(consultarTabla)
        filas= cursorObj.fetchall()
        if len(filas)==0:
            self.agregarIngredientes(Conexion().conexion(),producto)

        else:
            print("El producto ya se encuentra en la base de datos")
            print("***********************************************")
            self.menuIngredientes()


    def soloVerificacionIngrediente(self,conexion,producto):
        cursorObj = conexion.cursor()
        try:
            consultarTabla="SELECT * FROM Ingredientes WHERE name='{}'".format(producto)
            cursorObj.execute(consultarTabla)
            filas= cursorObj.fetchall()
            return True
        except:
            return False

    def agregarIngredientes(self,conexion,producto):
        self.producto=producto


        self.cantidad=int(input("cantidad: "))
        self.precio=int(input("precio: "))

        self.precioUni=self.precio//self.cantidad

        cursorObj = conexion.cursor()
        datos = (self.producto, self.cantidad,self.precio,self.precioUni)
        cursorObj.execute('''INSERT INTO Ingredientes VALUES(?,?,?,?)''',datos)
        #guarda en la base de datos
        conexion.commit()
        clearConsole()
        return print("registo exitoso")

    def eliminarIngrediente(self,conexion,producto):
        cursorObj = conexion.cursor()
        cursorObj.execute("DELETE FROM Ingredientes WHERE name='{}'".format(producto))
        conexion.commit()
        print("Tu producto se ha eliminado correctamente")


        pass
    #devuelve una lista con los ingredientes
    def mostrarIngredientesLista(self,conexion,producto):
        cursorObj = conexion.cursor()
        consultarTabla="SELECT * FROM Ingredientes WHERE name='{}' ".format(producto)
        cursorObj.execute(consultarTabla)
        filas= cursorObj.fetchall()
        return filas


    def mostrarIngredientes(self,conexion):
        cursorObj = conexion.cursor()
        consultarTabla="SELECT name FROM Ingredientes "
        cursorObj.execute(consultarTabla)
        filas= cursorObj.fetchall()
        print("*********************************************")
        print("*********Listado de ingredientes*************")
        print("*********************************************")
        for i in range(len(filas)):
            print(filas[i][0])
        print("****************************")
    def menuIngredientes(self):
            a=True
            while a:
                print('''Ingrese la funcion que desea realizar\n1)Agregar ingredientes\n2)Eliminar Ingredientes\n3)Modificar precio de Ingredientes y la cantidad \n4)Conocer los costos\n5)Salir''')
                selector= input()
                clearConsole()
                if(selector=="1"):
                    self.mostrarIngredientes(Conexion().conexion())
                    producto=input("Ingrese el nombre del producto a registrar: ").lower()
                    self.verificacionIngrediente(Conexion().conexion(),producto)

                elif selector=="2":
                    self.mostrarIngredientes(Conexion().conexion())
                    producto=input("Ingrese el nombre del producto a eliminar: ").lower()
                    clearConsole()
                    if self.soloVerificacionIngrediente(Conexion().conexion(),producto)==True:
                        self.eliminarIngrediente(Conexion().conexion(),producto)
                        self.menuIngredientes()
                        clearConsole()
                    else:
                        print("El producto no se encuentra en la base de datos")
                        print("**********************************")
                        self.menuIngredientes()
                elif selector=="3":
                    self.mostrarIngredientes(Conexion().conexion())
                    clearConsole()
                    pass
                elif selector=="5":

                    """if(not(Ingredientes().buscar_ingrediente(producto))):
                        cantidad=int(input("Ingrese la cantidad en gramos:"))
                        valor= int(input("Ingrese el valor:"))

                        a=Ingredientes().insertar_ingredientes(producto,cantidad,valor)
                        print("si se agrego")
                        lista=Ingredientes().consultar_Ingredientes()


                    else:
                        print("El producto ya se encuentra en la lista de ingredientes")"""
class Recetas(Ingredientes):


    def agregarReceta(self):

        self.nombReceta=input("Ingrese el nombre de la receta: ").lower()
        Conexion().sql_table(Conexion().conexion(),"{}( productos text PRIME KEY, cantidad integer, precio integer)".format(self.nombReceta))
        print("Tu receta llamada {} se creado correctamente".format(self.nombReceta))

    def agregarProductosReceta():
        pass
    def menuRecetas(self):
            a=True
            while a:
                print('''Ingrese la funcion que desea realizar\n1)Agregar Receta\n2)Eliminar Eliminar Receta\n3)Modificar valores de la Receta \n4)Conocer los costos\n''')
                selector= input()
                clearConsole()
                if(selector=="1"):
                    self.agregarReceta()
                elif selector=="2":
                    self.mostrarIngredientes(Conexion().conexion())
                    producto=input("Ingrese el nombre del producto a eliminar: ").lower()
                    clearConsole()
                    if self.soloVerificacionIngrediente(Conexion().conexion(),producto)==True:
                        self.eliminarIngrediente(Conexion().conexion(),producto)
                        self.menuIngredientes()
                        clearConsole()
                    else:
                        print("El producto no se encuentra en la base de datos")
                        print("**********************************")
                        self.menuIngredientes()
def rama():
    print("rama de nicolas")
def impresion ():
    print("Hola ke ace")
#funcion para insertar ingredientes
#Ingredientes().verificacionIngrediente(Conexion().conexion(),"huevos")
