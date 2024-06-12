import csv
lista=[]
cont=0
acum=0
def CrearCSV():
    with open('bbdd_productos.csv','w',newline='') as bbdd_productos:
            escritor_csv = csv.writer(bbdd_productos)
            escritor_csv.writerow(['ID','NOMBRE','PRECIO'])
            escritor_csv.writerows(lista)
            print("Archivo generado correctamente :D")
            
def CargarCSV():
    with open('bbdd_productos.csv','r',newline='')as bbdd_productos:
            lector_csv=csv.reader(bbdd_productos)
            for x in lector_csv:
                lista.append(x)
            print("Csv Cargado con exito :D")
    
def Agregar():
        id = int(input("Ingrese el id numerico del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto:"))
        listaproductos=[id,nombre,precio]
        lista.append(listaproductos)
    
while True:
    print("")
    print("================Menu================")
    print("")
    print("1.- Agregar Producto")
    print("2.- Listar todos los productos")
    print("3.- Eliminar un producto por ID")
    print("4.- Generar archivo CSV")
    print("5.- Cargar archivo CSV")
    print("6.- Estadisticas")
    print("0.- Salir :c")
    menu=int(input("Ingrese una opcion:"))
    print("")
    if menu == 1:
        print("")
        print("================Agregar Producto================")
        print("")
        Agregar()
    elif menu == 2:
        print("")
        print("================Lista Productos================")
        print("")
        for x in lista:
            print ("Id:", x[0],"Nombre: ",x[1],"Precio:",x[2])
            print("---------------------------------------")
    elif menu == 3:
        print("")
        print("================Eliminar Producto================")
        print("")
        encontrado = False
        id_buscar=int(input("Ingrese el id del producto a buscar: "))
        for x in lista:
            if id_buscar==x[0]:
                print("Producto Eliminado \n") 
                print("Patente : ",x[0], " Marca : ",x[1], " Modelo : ",x[2])
                lista.remove(x)
                print("Producto Eliminado :D")
                encontrado = True
                break
        if encontrado==False:
            print("El producto no existe...")
    elif menu == 4:
        print("")
        print("================Generado CSV================")
        print("")
        CrearCSV()
    elif menu == 5:
        print("")
        print("================Cargar CSV================")
        print("")
        CargarCSV()
    elif menu == 6:
        print("")
        print("================Estadisticas de productos================")
        print("")
        for x in lista:
            cont+=1
            acum=int(acum+x[2])
        print("El precio total de los ",cont,"productos es = ",acum)
        prom = acum/cont
        print("El promedio de los precios es de = ",prom)                
                
    elif menu == 0:
        print("Adios :c")
        break
    else:
        print("Error, intentelo nuevamente")