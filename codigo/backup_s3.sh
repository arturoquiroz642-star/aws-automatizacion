#!/bin/bash
set -e

# ===== CONFIGURACIÓN =====
BUCKET_NAME="mi-bucket-chris"        
SOURCE_DIR="$HOME/respaldo_prueba"
BACKUP_FILE="backup_$(date +%F_%H-%M-%S).tar.gz"
LOG_FILE="backup.log"

# Función para loguear con timestamp
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Validar que el directorio a respaldar existe
if [ ! -d "$SOURCE_DIR" ]; then
    log "ERROR: El directorio $SOURCE_DIR no existe."
    exit 1
fi

# Validar que AWS CLI está autenticado (LabRole)
if ! aws sts get-caller-identity &>/dev/null; then
    log "ERROR: AWS CLI no está autenticado. Verifica el rol IAM de la instancia."
    exit 1
fi

# Validar que el bucket existe
if ! aws s3 ls "s3://$BUCKET_NAME" &>/dev/null; then
    log "ERROR: El bucket s3://$BUCKET_NAME no existe o no tienes permisos."
    exit 1
fi

log "Iniciando respaldo de $SOURCE_DIR"
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" . >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    log "ERROR: Falló la compresión del directorio."
    exit 1
fi
log "Compresión completada: $BACKUP_FILE"

log "Subiendo archivo a s3://$BUCKET_NAME/"
if aws s3 cp "$BACKUP_FILE" "s3://$BUCKET_NAME/" >> "$LOG_FILE" 2>&1; then
    log "Respaldo subido exitosamente."
    # Limpieza opcional: borrar el archivo local después de subirlo
    rm -f "$BACKUP_FILE"
else
    log "ERROR en la subida del respaldo."
    exit 1
fi

log "Proceso finalizado."
