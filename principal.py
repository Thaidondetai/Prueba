import Funciones

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos={}
menores_800000={}
entre_800000_y_2000000={}
mayores_2000000={}
while True:
    try:
        print("1.Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion=int(input("Ingrese opción:"))
        if opcion==1:
            for trabajador in trabajadores:
                if trabajador not in sueldos:
                    sueldos[trabajador]=0
            sueldos=Funciones.asignar_sueldos(trabajadores,sueldos)
     
        elif opcion==2:
            total_sueldos=0
            menores_800000,entre_800000_y_2000000,mayores_2000000=Funciones.clasificar_sueldos(sueldos,menores_800000,entre_800000_y_2000000,mayores_2000000)
            print("\n")
            print("Sueldos menores a $800.000 Total:",len(menores_800000))
            print("\n")
            print("Nombre     Sueldo")
            for trabajador in menores_800000:
                print(trabajador ,menores_800000[trabajador])
            print("\n")
            print("Sueldos entre $800.000 y $2.000.0000 Total:",len(entre_800000_y_2000000))
            print("\n")
            print("Nombre     Sueldo")
            for trabajador in entre_800000_y_2000000:
                print(trabajador ,entre_800000_y_2000000[trabajador])
            print("\n")
            print("Sueldos Superiores a $2.000.0000 Total:",len(mayores_2000000))
            print("\n")
            print("Nombre     Sueldo")
            for trabajador in mayores_2000000:
                print(trabajador ,mayores_2000000[trabajador])
            print("\n")
            for trabajador in sueldos:
                total_sueldos+=sueldos[trabajador]
            print("Total:",(total_sueldos))
            
        elif opcion==3:
            Funciones.estadisticas(sueldos)

        elif opcion==4:
            achivo=Funciones.archivo(sueldos)
            print("Generando Reporte")
        elif opcion==5:
            break
        elif opcion==6:
            print("Solo puedes elegir ente 1 y 5")
    except:
        print("Eso no es un número,vuelve a ingresar")