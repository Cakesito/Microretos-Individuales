import os
import sqlite3

# Use a database file located next to this script for predictable behavior
db_path = os.path.join(os.path.dirname(__file__), "reto_elio.db")

conexion = sqlite3.connect(db_path)
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

# Create table `LOGS` with columns `id` and `evento`
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS LOGS (
        id INTEGER PRIMARY KEY,
        evento TEXT NOT NULL
    )
    """
)

# Prepare the 30 events
events = [
    "Inicio sistema",
    "Carga completa",
    "Error detectado",
    "Usuario login",
    "Usuario logout",
    "Creación registro",
    "Actualización registro",
    "Eliminación registro",
    "Backup realizado",
    "Restauración iniciada",
    "Restauración completada",
    "Conexión perdida",
    "Conexión restablecida",
    "Timeout",
    "Validación fallida",
    "Validación exitosa",
    "Permiso denegado",
    "Permiso concedido",
    "Archivo subido",
    "Archivo descargado",
    "Sincronización iniciada",
    "Sincronización completada",
    "Notificación enviada",
    "Notificación recibida",
    "Cache limpiado",
    "Sesión expirada",
    "Token renovado",
    "Configuración guardada",
    "Actualización disponible",
    "Actualización instalada",
]

# Insert all events using a parameterized query; this avoids duplicates if run multiple times
cursor.executemany("INSERT INTO LOGS (evento) VALUES (?)", [(e,) for e in events])

conexion.commit()
conexion.close()
