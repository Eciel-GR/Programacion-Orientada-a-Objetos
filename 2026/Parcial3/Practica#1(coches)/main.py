from coches import  coches,cochesbd
from tkinter import * #Tk,Label,Entry,Button
from tkinter import messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(1,1)

        self.main()
#....Vistas Views del sistema
   
    def borrarPantalla (self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        print("\033c")

    # def terminar(self):
    #     input("....gracias por usar el sistema ")
    
    # def opcInvalida(self):
    #      input ("...opcion invalida....\npresiona enter para continuar")


    def menuAcciones(self):
        self.borrarPantalla()
        tipo="Coche"
        Label(self.ventana, text=f":::Menu de {tipo}:::")
        Button(self.ventana, text="1.-Agregar",command=self.insertar_coches_view).pack(pady=10)
        Button(self.ventana, text="2.-Borrar",command=self.borrar_coches_view).pack(pady=10)
        Button(self.ventana, text="3.-Modificar",command=self.actualizar_coches_view).pack(pady=10)
        Button(self.ventana, text="4.-Mostrar",command=self.mostrar_coches_view).pack(pady=10)
        Button(self.ventana, text="5.-Regresar",command=self.main).pack(pady=10)
   
    

    def insertar_coches_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar los datos del Coche...").pack(pady=10)
        Label(self.ventana, text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana, text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="# de Asientos: ").pack(pady=5)
        self.num_asientos=Entry(self.ventana)
        self.num_asientos.pack(pady=5)

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)

        Button(self.ventana, text="::Agregar::",command=self.insertar_coche_controller).pack(pady=5)

    def borrar_coches_view(self):

        self.borrarPantalla()

        Label(self.ventana, text=".....ELIMINADOR DE COCHES.....").pack(pady=10)
        Label(self.ventana, text="Id de el coche a eliminar: ").pack(pady=5)
        self.Id=Entry(self.ventana)
        self.Id.focus()
        self.Id.pack(pady=5)
        

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        
        Button(self.ventana, text="::Borrar::",command=self.borrar_coche_controller).pack(pady=5)

    def actualizar_coches_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Id de el coche a actualizar: ").pack(pady=5)
        self.Id=Entry(self.ventana)
        self.Id.focus()
        self.Id.pack(pady=5)

        Label(self.ventana, text="...Ingresar los datos del Coche a actualizar...").pack(pady=10)
        self.marca=Entry(self.ventana)
        Label(self.ventana, text="Marca: ").pack(pady=5)
        self.marca.focus()
        self.marca.pack(pady=5)
        
        Label(self.ventana, text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana, text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana, text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana, text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana, text="# de Asientos: ").pack(pady=5)
        self.num_asientos=Entry(self.ventana)
        self.num_asientos.pack(pady=5)
        
        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        
        Button(self.ventana, text="::Actualizar::",command=self.actualizar_coche_controller).pack(pady=5)

    def mostrar_coches_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="....::LISTADO DE COCHES::....").pack(pady=10)

        # filas=""
        # filas=self.mostrar_coche_controller(filas)
        # Label(self.ventana,text=f"{filas}").pack(pady=5)

      

        coche1 = cochesbd.Cochesbd('', '', '', 0, 0, 0)
        registros = coche1.consultar()
        del coche1

        if registros and len(registros) > 0:
            # Encabezado
            encabezado = f"{'ID':<5} | {'Marca':<10} | {'Color':<10} | {'Modelo':<10} | {'Velocidad':<6} | {'Potencia':<6} | {'Asientos':<6}"
            Label(self.ventana, text=encabezado, font=("Courier", 9, "bold")).pack(pady=5)

            # Filas
            for fila in registros:
                info = f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]:<10} | {fila[4]:<10} | {fila[5]:<10} | {fila[6]:<10}"
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
        Button(self.ventana, text="1.- Coches",command=self.menuAcciones).pack(pady=10)
        Button(self.ventana, text="2.- Salir",command=self.ventana.quit).pack(pady=10)

 #....Controlador del sistema...  

    def respuesta_sql(self,respuesta):
            if respuesta:
                # input("\t\t:::accion exitosa:::")
                messagebox.showinfo(title=":: Exitoso ::", message="...Ajas, tas perro para programar :3...")
            else:
                # input("\t\t:::!camarada al chile no jalo!:::") 
                messagebox.showerror(title=":: Verifique por favor ::", message="...Chale w, no jalo :c...") 

    def insertar_coche_controller(self):
        # cochesitos={}
        # cochesitos['marca']=self.marca.get()
        
        datosCoche =(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.num_asientos.get())
        coche1 = cochesbd.Cochesbd(*datosCoche)
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def borrar_coche_controller(self):
            # cochesitos={}
            # cochesitos['marca']=self.marca.get()
            
        id_coche = self.Id.get()
        
        coche1 = cochesbd.Cochesbd('','','',0,0,0)
        respuesta = coche1.eliminar(id_coche)
        self.respuesta_sql(respuesta)
        del coche1

    def actualizar_coche_controller(self):

        id_coche = self.Id.get()
        datosCoche =(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.num_asientos.get())
        coche1 = cochesbd.Cochesbd(*datosCoche)
        respuesta = coche1.actualizar(id_coche)
        self.respuesta_sql(respuesta)
        del coche1

    def mostrar_coche_controller(self):

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

if __name__ == "__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()
