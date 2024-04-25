import itertools

lista = []
ventas = []

while True:
    print("\x1b[4;3;36m"+"Bienvenido a Wingszu Flowers Heredia"+'\033[0;m')
    print("\x1b[1;33m"+"1. Ingresar Cliente"+'\033[0;m')
    print("\x1b[1;35m"+"2. Compra"+'\033[0;m')
    print("\x1b[1;32m"+"3. Ventas del día"+'\033[0;m')
    print("\x1b[1;31m"+"4. Salir"+'\033[0;m')
    opcion = int(input("\x1b[3;36m"+"Seleccione una opción: "+'\033[0;m'))
    columnas = ['Cedulas', 'Nombres', 'FechasNacimiento', 'Telefonos']
    columnaVentas = ['Flor', 'Cantidad', 'Cedula', 'Nombre', 'Entrega', 'Monto']
    flores = ['Margaritas', 'Tulipanes', 'Rosas', 'Claveles']
    
    if opcion == 4:
        print("Programa cerrado")
        break
    
    elif opcion == 1:
        cedula = input("\x1b[1;33m"+"Ingrese la cedula: "+'\033[0;m')
        nombre = input("\x1b[1;35m"+"Ingrese el nombre completo: "+'\033[0;m')
        fecNacimiento = input("\x1b[1;32m"+"Ingrese la fecha de nacimiento DD/MM/AAAA: "+'\033[0;m')
        telefono = input("\x1b[1;36m"+"Ingrese el numero de telefono: "+'\033[0;m')
        lista += [{'Cedulas': cedula, 'Nombres': nombre, 'FechasNacimiento': fecNacimiento, 'Telefonos': telefono}]
        with open('data.txt', 'w') as txtfile:
                txtfile.write(str(lista))
                txtfile.close()
                print("\x1b[4;3;37m"+"Cliente guardado"+'\033[0;m')

    elif opcion == 2:
        terminado = True
        print("\x1b[1;33m"+"1. Margaritas"+'\033[0;m')
        print("\x1b[1;35m"+"2. Tulipanes"+'\033[0;m')
        print("\x1b[1;32m"+"3. Rosas"+'\033[0;m')
        print("\x1b[1;31m"+"4. Claveles"+'\033[0;m')
        flor = input("\x1b[2;36m"+"Seleccione una flor: "+'\033[0;m')
        cantidad = input("\x1b[1;33m"+"Ingrese la cantidad de flores: "+'\033[0;m')
        cedula2 = input("\x1b[1;35m"+"Ingrese la cedula: "+'\033[0;m')
        nombre2 = input("\x1b[1;32m"+"Ingrese el nombre: "+'\033[0;m')
        entrega = input("\x1b[1;31m"+"¿Requiere entrega?: "+'\033[0;m')
        monto = input("\x1b[2;36m"+"Ingrese el monto: "+'\033[0;m')
        total=0
        #while terminado:
        if entrega == 'Si' or entrega == 'si' or entrega == 'SI':
            entrega = True
            total = int(monto) + 1500
        else:
            entrega = False
            total = int(monto)
            
        ventas += [{'Flor': flor, 'Cantidad': cantidad, 'Cedula': cedula2, 'Nombre': nombre2, 'Entrega': entrega, 'Monto': total}]
        if (list(filter(lambda cedula: cedula['Cedulas'] == cedula2, lista)) != []) == True:
            with open('ventas.txt', 'w') as txtfile2:
                txtfile2.write(str(ventas))
                txtfile2.close()
                print("\x1b[4;3;37m"+"Venta guardada"+'\033[0;m')
            
        else:
            fecNacimiento = input("\x1b[1;33m"+"Ingrese la fecha de nacimiento DD/MM/AAAA: "+'\033[0;m')
            telefono = input("\x1b[1;35m"+"Ingrese el numero de telefono: "+'\033[0;m')
            lista += [{'Cedulas': cedula2, 'Nombres': nombre2, 'FechasNacimiento': fecNacimiento, 'Telefonos': telefono}]
            with open('data.txt', 'w') as txtfile:
                txtfile.write(str(lista))
                txtfile.close()
                print("\x1b[4;3;37m"+"Cliente guardado"+'\033[0;m')
            with open('ventas.txt', 'w') as txtfile2:
                txtfile2.write(str(ventas))
                txtfile2.close()
                print("\x1b[4;3;37m"+"Venta guardada"+'\033[0;m')
        
    elif opcion == 3:
        despliegue = sorted([(dato['Cedula'], dato['Monto']) for dato in ventas], key=lambda dato: dato[0])
        for k, g in itertools.groupby(despliegue,key=lambda dato: dato[0] ):
            suma = sum([x[1] for x in g])
            with open('reporte.txt', 'w') as txtreport:
                txtreport.write('\n' + str(k) + ' ' + str(suma))
                txtreport.close()
        print("\x1b[4;3;37m"+"Reporte generado"+'\033[0;m')
        
    else:
        print("Opción inválida")
