# Actividad: Automatización en AWS con Boto3 y Bash

## Descripción
- **Script Python** (`gestionar_ec2.py`): Lista instancias EC2, inicia o detiene una instancia específica.
- **Script Bash** (`backup_s3.sh`): Comprime un directorio local y sube el respaldo a un bucket S3, generando un log.

## Requisitos cumplidos
- Sin credenciales en texto plano (uso de `LabRole`).
- Manejo de excepciones en Python y validaciones en Bash.
- Generación de logs con timestamp.

## Evidencias de ejecución

### 1. Gestión de instancias EC2
**Salida del script Python:**



## Instrucciones de ejecución
1. Asegurar que la instancia EC2 tenga el rol `LabRole`.
2. Ejecutar `python3 gestionar_ec2.py`.
3. Ejecutar `./backup_s3.sh`.

## Conclusión
Se automatizó exitosamente la gestión de instancias EC2 y el respaldo a S3 usando scripts en Python y Bash.
