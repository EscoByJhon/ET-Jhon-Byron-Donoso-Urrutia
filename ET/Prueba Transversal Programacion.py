import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos():
    return {t: random.randint(300000, 2500000) for t in trabajadores}

def clasificar_sueldos(sueldos):
    menor = {calculo: MM for calculo, MM in sueldos.items() if MM < 800000}
    entre = {calculo: MM for calculo, MM in sueldos.items() if 800000 <= MM <= 2000000}
    mayor = {calculo: MM for calculo, MM in sueldos.items() if MM > 2000000}

    print("\nSueldos menores a 800.000:", menor)
    print("Sueldos entre 800.000 y 2.000.000:", entre)
    print("Sueldos superiores a$2.000.000:", mayor)
    print("total sueldos: ", sum(sueldos.values()))

def ver_estadisticas(sueldos):
    valores = list(sueldos.values())
    print("\nEstadísticas de sueldos:")
    print(f"Sueldo más alto: {max(valores)}")
    print(f"Sueldo más bajo: {min(valores)}")
    print(f"Promedio de sueldos: {sum(valores) / len(valores)}")
    print(f"Media geométrica: {math.exp(sum(math.log(s) for s in valores) / len(valores))}")

def reporte_sueldos(sueldos):
    reporte = [[t, s, s*0.07, s*0.12, s - s*0.07 - s*0.12] for t, s in sueldos.items()]
    print("\nReporte de sueldos:")
    for r in reporte:
        print(f"{r[0]}, Sueldo Base: {r[1]}, Descuento Salud: {r[2]}, Descuento AFP: {r[3]}, Sueldo Líquido: {r[4]}")
    return reporte

def exportar_csv(reporte):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)
    print("\nDatos exportados a reporte_sueldos.csv")

def programa():
    sueldos = {}
    while True:
        print("\n1. Asignar sueldos\n2. Clasificar sueldos\n3. Ver estadísticas\n4. Reporte de sueldos\n5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sueldos = asignar_sueldos()
            print("Sueldos asignados.")
        elif opcion == '2':
            clasificar_sueldos(sueldos) if sueldos else print("Primero debe asignar los sueldos.")
        elif opcion == '3':
            ver_estadisticas(sueldos) if sueldos else print("Primero debe asignar los sueldos.")
        elif opcion == '4':
            if sueldos:
                reporte = reporte_sueldos(sueldos)
                exportar_csv(reporte)
            else:
                print("Primero debe asignar los sueldos.")
        elif opcion == '5':
            print("Finalizando programa")
            print("Desarrollado por Jhon Byron Donoso Urrutia")
            print("Rut 20.329.941-9")
            break
        else:
            print("Opción no válida.")

programa()
