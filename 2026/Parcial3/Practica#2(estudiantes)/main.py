from estudiantes import estudiante
from tkinter import * #Tk,Label,Entry,Button
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(1,1)
        self.main()

    def borrarPantalla (self):
            for widget in self.ventana.winfo_children():
                widget.destroy()
    
            print("\033c")

# view
    def menuAcciones(self):
        self.borrarPantalla()
        tipo="Coche"
        Label(self.ventana, text=f":::Menu de {tipo}:::")
        Button(self.ventana, text="1.-Agregar",command=self.insertar_estudiante_view).pack(pady=10)
        Button(self.ventana, text="2.-Borrar",command=self.borrar_estudiante_view).pack(pady=10)
        Button(self.ventana, text="3.-Modificar",command=self.actualizar_estudiante_view).pack(pady=10)
        Button(self.ventana, text="4.-Mostrar",command=self.mostrar_estudiante_view).pack(pady=10)
        Button(self.ventana, text="5.-Regresar",command=self.main).pack(pady=10)


    def insertar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar los datos del Estudiante...").pack(pady=10)
        Label(self.ventana, text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana, text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

       

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)

        Button(self.ventana, text="::Agregar::",command=self.insertar_estudiante_controller).pack(pady=5)

    def borrar_estudiante_view(self):

        self.borrarPantalla()

        Label(self.ventana, text=".....ELIMINADOR DE ESTUDIANTES.....").pack(pady=10)
        Label(self.ventana, text="Id de el estudiante a eliminar: ").pack(pady=5)
        self.Id=Entry(self.ventana)
        self.Id.focus()
        self.Id.pack(pady=5)
        

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        
        Button(self.ventana, text="::Borrar::",command=self.borrar_estudiante_controller).pack(pady=5)

    def actualizar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Id de el estudiante a actualizar: ").pack(pady=5)
        self.Id=Entry(self.ventana)
        self.Id.focus()
        self.Id.pack(pady=5)

        Label(self.ventana, text="...Ingresar los datos del estudiante a actualizar...").pack(pady=10)
    

        Label(self.ventana, text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.pack(pady=5)
        
        Label(self.ventana, text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)
        
        
        
        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        
        Button(self.ventana, text="::Actualizar::",command=self.actualizar_estudiante_controller).pack(pady=5)

    def mostrar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="....::LISTADO DE ESTUDIANTES::....").pack(pady=10)

        # filas=""
        # filas=self.mostrar_coche_controller(filas)
        # Label(self.ventana,text=f"{filas}").pack(pady=5)

      

        estudiante1 = estudiante.Estudiantes('', 0)
        registros = estudiante1.consultar()
        del estudiante1

        if registros and len(registros) > 0:
            # Encabezado
            encabezado = f"{'ID':<5} | {'Nombre':<10} | {'Nota':<10}"
            Label(self.ventana, text=encabezado, font=("Courier", 9, "bold")).pack(pady=5)

            # Filas
            for fila in registros:
                info = f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} "
                Label(self.ventana, text=info, font=("Courier", 9)).pack(pady=2)
        else:
            Label(self.ventana, text="No se encontró información en la base de datos.").pack(pady=20)

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        

    def menu_coches(self):
        opc = True
        while opc:
            self.borrarPantalla()
            opc = self.menuAcciones('coches')

            match opc:
                case '1':
                    datosCoche = self.pedirDatos("coches")
                    coche1 = cochesbd.Cochesbd(*datosCoche)
                    respuesta = coche1.insertar()
                    self.respuesta_sql(respuesta)
                    del coche1
                case '2':
                    self.borrarPantalla()
                    id = int(input("ingrese el id del coche que desea eliminar....."))
                    coche1 = cochesbd.Cochesbd('','','',0,0,0)
                    respuesta = coche1.eliminar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    del coche1
                    
                case '3':
                    self.borrarPantalla()
                    id =int( input("ingrese el id del coche que desea actualizar......"))
                    datosCoche = self.pedirDatos("coches")
                    coche1 = cochesbd.Cochesbd(*datosCoche)
                    respuesta = coche1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    del coche1
                case '4':
                    coche1 = cochesbd.Cochesbd('','','',0,0,0)
                    registros = coche1.consultar()
                    if len(registros) > 0:
                        numCoches = 1
                        print(f"\n\tcoche # {numCoches}\n\tID:\ttmarca\ttmarca:\tcolor:\t modelo:\tvelocidad:\t potencia:\tasientos:\n")
                        for fila in registros:
                            print(f"\t{fila[0]} \t {fila[1]}\t {fila[2]}\t {fila[3]}\t\t {fila[4]}\t {fila[5]}\t {fila[6]}") 
                    else:
                        print("no se encontro informacion en la base de datos")
                    self.esperaTecla()
                    del coche1
                case '5':
                    opc = False
                case _:
                    self.opcInvalida()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text=";;; MENU PRINCIPAL ;;;",).pack(pady=20)
        Button(self.ventana, text="1.- Estudiantes",command=self.menuAcciones).pack(pady=10)
        Button(self.ventana, text="2.- Salir",command=self.ventana.quit).pack(pady=10)

# controlador
    def respuesta_sql(self,respuesta):
            if respuesta:
                # input("\t\t:::accion exitosa:::")
                messagebox.showinfo(title=":: Exitoso ::", message="...Ajas, tas perro para programar :3...")
            else:
                # input("\t\t:::!camarada al chile no jalo!:::") 
                messagebox.showerror(title=":: Verifique por favor ::", message="...Chale w, no jalo :c...") 

    def insertar_estudiante_controller(self):
        # cochesitos={}
        # cochesitos['marca']=self.marca.get()
        
        datosEstudiante =(self.nombre.get(),self.nota.get())
        estudiante1 = estudiante.Estudiantes(*datosEstudiante)
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1
    def borrar_estudiante_controller(self):
            # cochesitos={}
            # cochesitos['marca']=self.marca.get()
            
        id_estudiante = self.Id.get()
        
        estudiante1 = estudiante.Estudiantes('','','',0,0,0)
        respuesta = estudiante1.eliminar(id_estudiante)
        self.respuesta_sql(respuesta)
        del estudiante1

    def actualizar_estudiante_controller(self):

        id_estudiante = self.Id.get()
        datosEstudiante =(self.nombre.get(),self.nota.get())
        estudiante1 = estudiante.Estudiantes(*datosEstudiante)
        respuesta = estudiante1.actualizar(id_estudiante)
        self.respuesta_sql(respuesta)
        del estudiante1

    def mostrar_estudiante_controller(self):

        estudiante1 = estudiante.Estudiantes('','','',0,0,0)
        registros = estudiante1.consultar()
        if len(registros) > 0:
            numEstudiante = 1
            print(f"\n\testudiante # {numEstudiante}\n\tID:\ttnombre\ttnota:\n")
            for fila in registros:
                print(f"\t{fila[0]} \t {fila[1]}\t {fila[2]}") 
        else:
            print("no se encontro informacion en la base de datos")
            self.esperaTecla()
            del estudiante1

    # def esperaTecla (self):
    #     input("....OPRIMA CUALQUIER TECLA PARA CONTINUAR....")
    # def borrarPantalla (self):
    #     print("\033c")
    # def terminar(self):
    #     input("....gracias por usar el sisitema ")
    # def opcInvalida(self):
    #      input ("...opcion invalida....\npresiona enter para continuar")
    # def menuAcciones(self,tipo):
    #     print(f"\t\t...::::menu de tipo {tipo} :::.... ")
    #     opcion = input("\n\t1.- agregar  \n\t2.- Borrar \n\t3.- modificar \n\t4.- mostrar \n\t5.-regresar \n\t...seleciona una opcion...." ).strip()
    #     return opcion
    # def respuesta_sql(self,respuesta):
    #     if respuesta:
    #         input("\t\t:::accion exitosa:::")
    #     else:
    #         input("\t\t:::!camarada al chile no jalo!:::")
    # def pedirDatos(self,tipo):
    #     self.borrarPantalla()
    #     print(f"\t\t ::: REGISTRAR NUEVO {tipo.upper()} :::")
    #     nombre = input("Ingrese el nombre de estudiante: ").upper().strip()
    #     notas = input("Ingrese la nota: ").upper().strip()
    #     regresar = (nombre,notas)
    #     return regresar
    # def menu_estudiantes(self):
    #     opc = True
    #     while opc:
    #         self.borrarPantalla()
    #         opc = self.menuAcciones('estudiantes')

    #         match opc:
    #             case '1':
    #                 datosEstudiante = self.pedirDatos("Estudiantes")
    #                 # Estudiante1 = estudiante.Estudiantes(*datosEstudiante)
    #                 respuesta = estudiante.Estudiantes(*datosEstudiante).insertar()
    #                 self.respuesta_sql(respuesta)
    #                 # del Estudiante1
    #             case '2':
    #                 self.borrarPantalla()
    #                 id = int(input("ingrese el id del estudiante que desea eliminar....."))
    #                 # Estudiante1 = estudiante.Estudiantes('',0)
                    
    #                 respuesta = estudiante.Estudiantes.eliminar(id)
    #                 self.respuesta_sql(respuesta)
    #                 self.esperaTecla()
    #                 # del Estudiante1
                    
    #             case '3':
    #                 self.borrarPantalla()
    #                 id =int(input("ingrese el id del estudiante que desea eliminar....."))
    #                 datosEstudiante = self.pedirDatos("Estudiantes")
    #                 # Estudiante1 = estudiante.Estudiantes(*datosEstudiante)
                    
    #                 respuesta = estudiante.Estudiantes(*datosEstudiante).actualizar(id)
    #                 self.respuesta_sql(respuesta)
    #                 self.esperaTecla()
    #                 # del Estudiante1
    #             case '4':
    #                 # Estudiante1 = estudiante.Estudiantes('',0)
                    
    #                 registros = estudiante.Estudiantes.consultar()
    #                 if len(registros) > 0:
    #                     numEstudiantes = 1
    #                     print(f"\n\testudiante # {numEstudiantes}\n\tID:\tnombre: \tnota: \n")
    #                     for fila in registros:
    #                         print(f"\t{fila[0]} \t {fila[1]}\t {fila[2]}") 
    #                 else:
    #                     print("no se encontro informacion en la base de datos")
    #                 self.esperaTecla()
    #                 # del Estudiante1
    #             case '5':
    #                 opc = False
    #             case _:
    #                 self.opcInvalida()
    # def main(self):
    #     opcion = True
    #     while opcion:
    #         self.borrarPantalla()
    #         opcion = input("\t\t ::::menu principal:::::\n\t1- Estudiante\n\t2- salir\n\t elige una opcion....").lower().strip()
    #         match opcion:
    #             case '1':
    #                 self.borrarPantalla()
    #                 self.menu_estudiantes()
    #                 self.esperaTecla()
    #             case '2':
    #                 self.borrarPantalla()
    #                 self.terminar()
    #                 opcion = False
    #             case _:
    #                 self.borrarPantalla()
    #                 self.opcInvalida()



if __name__=="__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()
