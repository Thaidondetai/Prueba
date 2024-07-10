import random,csv,statistics
def asignar_sueldos(trabajadores,sueldos):
    for trabajador in trabajadores:
        sueldo=random.randint(300000,2500000)
        sueldos[trabajador]=sueldo
    return sueldos

def clasificar_sueldos(sueldos,menores_800000,entre_800000_y_2000000,mayores_2000000):
    for trabajador,pago in sueldos.items():
        if pago<800000:
            menores_800000[trabajador]=pago
        elif pago<2000000:
            entre_800000_y_2000000[trabajador]=pago
        elif pago>=2000000:
            mayores_2000000[trabajador]=pago
    return menores_800000,entre_800000_y_2000000,mayores_2000000

def estadisticas(sueldos):

    sueldo=list(sueldos.values())
    minimo=min(sueldo)
    maximo=max(sueldo)
    prom=sum(sueldo)/len(sueldo)
    media_geometrica=statistics.geometric_mean(sueldo)

    print("Sueldo más alto:",maximo)
    print("Sueldo más bajo :",minimo)
    print("Promedios Sueldos:",prom)
    print("Media geometrica:",media_geometrica)

def archivo(sueldos):
    with open("Reporte.csv","w",newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo liquido"])
        for trabajador,sueldo in sueldos.items():
            descuento_salud=(sueldo*7)/100 #Disminuye de 100% a 93%
            descuento_AfP=(sueldo*12)/100 #Disminuye de 100% a 88%
            sueldoliquido=(sueldo-descuento_salud-descuento_AfP)
            escritor.writerow([trabajador,sueldo,descuento_salud,descuento_AfP,sueldoliquido])
            
                    
                    


    