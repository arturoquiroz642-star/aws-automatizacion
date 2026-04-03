#!/usr/bin/env python3
import boto3
import time

def listar_instancias(ec2_client):
    print("--- Listado de Instancias EC2 ---")
    try:
        response = ec2_client.describe_instances()
        instancias = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instancia_id = instance['InstanceId']
                estado = instance['State']['Name']
                print(f"ID: {instancia_id} - Estado: {estado}")
                instancias.append((instancia_id, estado))
        return instancias
    except Exception as e:
        print(f"Error al listar instancias: {e}")
        return []

def gestionar_instancia(ec2_client, instancia_id, accion):
    if accion == "iniciar":
        print(f"Iniciando instancia {instancia_id}...")
        try:
            ec2_client.start_instances(InstanceIds=[instancia_id])
            print(f"Instancia {instancia_id} iniciada.")
        except Exception as e:
            print(f"Error al iniciar: {e}")
    elif accion == "detener":
        print(f"Deteniendo instancia {instancia_id}...")
        try:
            ec2_client.stop_instances(InstanceIds=[instancia_id])
            print(f"Instancia {instancia_id} detenida.")
        except Exception as e:
            print(f"Error al detener: {e}")
    else:
        print("Acción no válida. Usa 'iniciar' o 'detener'.")

if __name__ == "__main__":
    # Cambia la región si tu laboratorio usa us-west-2
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Listar instancias
    instancias = listar_instancias(ec2)
    
    if not instancias:
        print("No se encontraron instancias EC2 en esta región.")
        exit(1)
    
    # Elegir la primera instancia de la lista como ejemplo
    id_ejemplo, estado_actual = instancias[0]
    print(f"\n--- Gestionando instancia {id_ejemplo} (estado actual: {estado_actual}) ---")
    
    # Decidir la acción según el estado actual
    if estado_actual == "stopped":
        gestionar_instancia(ec2, id_ejemplo, "iniciar")
    elif estado_actual == "running":
        gestionar_instancia(ec2, id_ejemplo, "detener")
    else:
        print(f"La instancia está en estado '{estado_actual}' no se puede iniciar/detener.")
    
    # Esperar unos segundos para que AWS procese el cambio
    time.sleep(5)
    
    # Volver a listar para ver el nuevo estado
    print("\n--- Listado actualizado después de la gestión ---")
    listar_instancias(ec2)
