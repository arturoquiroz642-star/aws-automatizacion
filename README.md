#  Automatización de Respaldo y Gestión de Instancias en AWS

##  Materia: Fundamentos de DevOps

**Alumno:** Christian Arturo Quiroz
**Matrícula:** AL07094421

---

##  Descripción del Proyecto

Este proyecto implementa una solución de automatización en la nube utilizando servicios de AWS, combinando scripts en Bash y Python para gestionar respaldos y administrar instancias EC2.

Se desarrollaron dos componentes principales:

* 🔹 Un script en Bash para generar respaldos comprimidos y almacenarlos en Amazon S3.
* 🔹 Un script en Python utilizando Boto3 para listar, iniciar y detener instancias EC2.

El objetivo es aplicar principios de DevOps como automatización, validación de procesos y uso eficiente de infraestructura en la nube.

---

## Arquitectura Utilizada

* **EC2 (Elastic Compute Cloud):** Ejecución de scripts
* **S3 (Simple Storage Service):** Almacenamiento de respaldos
* **IAM (LabRole):** Gestión segura de permisos sin credenciales explícitas
* **AWS CLI:** Interacción con servicios AWS
* **Boto3:** SDK de Python para AWS

Región utilizada: `us-east-1`

---

##  Configuración del Entorno

1. Lanzamiento de instancia EC2:

   * AMI: Amazon Linux 2023
   * Tipo: t2.micro
   * Rol IAM: LabRole

2. Instalación de dependencias:

```bash
sudo dnf update -y
sudo dnf install python3-pip -y
pip3 install boto3 --user
```

3. Verificación de credenciales:

```bash
aws sts get-caller-identity
```

4. Creación del directorio de prueba:

```bash
mkdir -p ~/respaldo_prueba
echo "Archivo de prueba" > ~/respaldo_prueba/documento1.txt
```

5. Creación del bucket S3:

```bash
aws s3 mb s3://mi-bucket-chris --region us-east-1
```

---

##  Estructura del Proyecto

```
aws-automatizacion/
│
├── README.md
├── codigo/
│   ├── backup_s3.sh
│   └── gestionar_ec2.py
│
└── evidencias/
    ├── backup_log.txt
    ├── python_output.txt
    ├── s3_listing.txt
    └── img/
```

---

## Script Bash: Respaldo a S3

### 🔹 Funcionalidad:

* Verifica existencia del directorio
* Valida autenticación AWS
* Comprime archivos
* Sube respaldo a S3
* Genera log del proceso

###  Ejecución:

```bash
chmod +x backup_s3.sh
./backup_s3.sh
```

### Resultado esperado:

* Archivo `.tar.gz` subido a S3
* Registro en `backup.log`

---

##  Script Python: Gestión de EC2

### 🔹 Funcionalidad:

* Lista instancias EC2
* Inicia o detiene una instancia
* Muestra estado actualizado

###  Ejecución:

```bash
python3 gestionar_ec2.py
```

###  Nota:

Modificar el ID de instancia:

```python
INSTANCIA_ID = "i-xxxxxxxxxx"
```

---

##  Resultados Obtenidos

* ✔ Respaldo exitoso en S3
* ✔ Generación de logs detallados
* ✔ Control de instancias EC2
* ✔ Automatización funcional

Ejemplo de salida:

```
ID: i-1234567890 - Estado: stopped
Iniciando instancia...
ID: i-1234567890 - Estado: running
```

---

##  Evidencias

Las evidencias del funcionamiento se encuentran en la carpeta:

```
/evidencias/
```

Incluyen:

* Logs del script Bash
* Salida del script Python
* Listado del bucket S3
* Capturas de ejecución en EC2

---

##  Retos y Soluciones

Durante el desarrollo se presentaron algunos desafíos:

* ❌ Problemas de autenticación con AWS CLI
  ✔ Solución: Verificación del rol IAM (LabRole)

* ❌ Error al acceder al bucket S3
  ✔ Solución: Validación previa en el script Bash

* ❌ Configuración inicial de dependencias
  ✔ Solución: Instalación manual de boto3 y pip

Estos problemas permitieron fortalecer el entendimiento del entorno AWS y mejorar la robustez de los scripts.

---

## Conclusiones

Este proyecto permitió aplicar conceptos fundamentales de DevOps en un entorno real, integrando automatización, validación de procesos y uso de servicios en la nube.

El uso combinado de Bash y Python facilitó la gestión eficiente de recursos en AWS, demostrando la importancia de la automatización en la administración de infraestructura.

Además, se aplicaron buenas prácticas como:

* Validación de errores
* Uso de logs
* Seguridad mediante roles IAM

---

##  Repositorio

El código fuente y las evidencias se encuentran en este repositorio.

---

## Autor

**Christian Arturo Quiroz**
Estudiante de Ingeniería / DevOps en formación
