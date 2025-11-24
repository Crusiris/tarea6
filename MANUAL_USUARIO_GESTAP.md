# MANUAL DE USUARIO - GESTAP
## Gestor de Tareas Personales

**Versión:** 1.0  
**Fecha:** 24 de noviembre de 2025  
**Autor:** Sistema GESTAP  

---

## 📋 TABLA DE CONTENIDOS

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Inicio Rápido](#inicio-rápido)
5. [Guía Detallada de Comandos](#guía-detallada-de-comandos)
6. [Ejemplos de Uso](#ejemplos-de-uso)
7. [Gestión de Archivos](#gestión-de-archivos)
8. [Solución de Problemas](#solución-de-problemas)
9. [Preguntas Frecuentes (FAQ)](#preguntas-frecuentes-faq)
10. [Soporte y Contacto](#soporte-y-contacto)

---

## 🎯 INTRODUCCIÓN

**GESTAP** (Gestor de Tareas Personales) es una aplicación de línea de comandos diseñada para ayudarte a organizar y gestionar tus tareas diarias de manera eficiente. Con una interfaz simple e intuitiva, GESTAP te permite:

- ✅ Agregar tareas con diferentes niveles de prioridad
- 📋 Visualizar tus tareas pendientes y completadas
- ⚡ Marcar tareas como completadas
- 🗑️ Eliminar tareas innecesarias
- 📊 Consultar estadísticas de progreso

### Características Principales

| Característica | Descripción |
|----------------|-------------|
| **Simplicidad** | Interfaz de línea de comandos fácil de usar |
| **Persistencia** | Las tareas se guardan automáticamente |
| **Prioridades** | Organiza tareas por niveles de importancia |
| **Estadísticas** | Visualiza tu progreso y productividad |
| **Portabilidad** | Funciona en cualquier sistema con Python |

---

## 💻 REQUISITOS DEL SISTEMA

### Requisitos Mínimos
- **Sistema Operativo:** Windows 10/11, macOS 10.14+, Linux Ubuntu 18.04+
- **Python:** Versión 3.6 o superior
- **Memoria RAM:** 64 MB disponible
- **Espacio en disco:** 10 MB

### Requisitos Recomendados
- **Python:** Versión 3.8 o superior
- **Terminal/Consola** con soporte para emojis UTF-8

### Verificación de Python

Para verificar tu versión de Python, ejecuta:

```bash
python --version
# o
python3 --version
```

---

## 🚀 INSTALACIÓN

### Instalación Simple

1. **Descargar el archivo**
   ```bash
   # Descarga o copia el archivo gestap.py a tu directorio preferido
   ```

2. **Hacer ejecutable** (Linux/macOS)
   ```bash
   chmod +x gestap.py
   ```

3. **Ejecutar**
   ```bash
   python gestap.py
   # o en Linux/macOS
   python3 gestap.py
   ```

### Instalación Avanzada (Opcional)

Para usar GESTAP desde cualquier directorio:

**En Linux/macOS:**
```bash
# Copiar a directorio del sistema
sudo cp gestap.py /usr/local/bin/gestap
sudo chmod +x /usr/local/bin/gestap

# Usar directamente
gestap
```

**En Windows:**
```cmd
# Agregar el directorio de GESTAP a la variable PATH del sistema
```

---

## ⚡ INICIO RÁPIDO

### Primera Ejecución

1. Abre tu terminal o línea de comandos
2. Navega al directorio donde tienes `gestap.py`
3. Ejecuta: `python gestap.py`
4. Verás el mensaje de bienvenida:

```
🚀 Bienvenido a GESTAP - Gestor de Tareas Personales
Escribe 'help' para ver los comandos disponibles o 'exit' para salir.

GESTAP>
```

### Primeros Pasos

```bash
# 1. Ver ayuda
GESTAP> help

# 2. Agregar tu primera tarea
GESTAP> add "Comprar leche"

# 3. Ver tus tareas
GESTAP> list

# 4. Completar una tarea
GESTAP> complete 1

# 5. Ver estadísticas
GESTAP> stats
```

---

## 📖 GUÍA DETALLADA DE COMANDOS

### Comando: `add`
**Propósito:** Agregar una nueva tarea

**Sintaxis:**
```
add <descripción> [prioridad]
```

**Parámetros:**
- `descripción`: Texto descriptivo de la tarea (obligatorio)
- `prioridad`: Nivel de importancia: `alta`, `media`, `baja` (opcional, por defecto: media)

**Ejemplos:**
```bash
GESTAP> add "Llamar al dentista"
GESTAP> add "Estudiar para examen" alta
GESTAP> add "Lavar el auto" baja
```

### Comando: `list`
**Propósito:** Mostrar tareas pendientes

**Sintaxis:**
```
list
```

**Salida esperada:**
```
============================================================
📋 GESTAP - Lista de Tareas
============================================================
⏳ ID: 1 | 🔴 ALTA
   📝 Estudiar para examen
   📅 Creada: 2025-11-24 10:30:15
------------------------------------------------------------
```

### Comando: `listall`
**Propósito:** Mostrar todas las tareas (pendientes y completadas)

**Sintaxis:**
```
listall
```

### Comando: `complete`
**Propósito:** Marcar una tarea como completada

**Sintaxis:**
```
complete <id>
```

**Parámetros:**
- `id`: Número identificador de la tarea

**Ejemplo:**
```bash
GESTAP> complete 1
✅ Tarea 1 marcada como completada.
```

### Comando: `delete`
**Propósito:** Eliminar una tarea permanentemente

**Sintaxis:**
```
delete <id>
```

**⚠️ Advertencia:** Esta acción no se puede deshacer

**Ejemplo:**
```bash
GESTAP> delete 2
🗑️  Tarea 2 eliminada.
```

### Comando: `stats`
**Propósito:** Mostrar estadísticas de productividad

**Sintaxis:**
```
stats
```

**Salida esperada:**
```
========================================
📊 ESTADÍSTICAS
========================================
📋 Total de tareas: 5
✅ Completadas: 3
⏳ Pendientes: 2
📈 Progreso: 60.0%
```

### Comando: `help`
**Propósito:** Mostrar ayuda y lista de comandos

### Comando: `exit`
**Propósito:** Salir de la aplicación

---

## 💡 EJEMPLOS DE USO

### Escenario 1: Planificación Diaria

```bash
GESTAP> add "Revisar emails" alta
✅ Tarea agregada con ID: 1

GESTAP> add "Reunión con equipo a las 2pm" alta
✅ Tarea agregada con ID: 2

GESTAP> add "Comprar víveres" media
✅ Tarea agregada con ID: 3

GESTAP> list
# Ver todas las tareas del día
```

### Escenario 2: Seguimiento de Proyecto

```bash
GESTAP> add "Investigar tecnologías" alta
GESTAP> add "Escribir propuesta" alta  
GESTAP> add "Revisar presupuesto" media
GESTAP> add "Enviar presentación" baja

# Después de completar investigación
GESTAP> complete 1

GESTAP> stats
# Ver progreso del proyecto
```

### Escenario 3: Gestión de Tareas Domésticas

```bash
GESTAP> add "Limpiar casa" media
GESTAP> add "Lavar ropa" baja
GESTAP> add "Pagar recibo de luz" alta
GESTAP> add "Reparar grifo" media

# Completar tareas urgentes primero
GESTAP> complete 3
GESTAP> listall
```

---

## 📁 GESTIÓN DE ARCHIVOS

### Archivo de Datos

GESTAP almacena todas las tareas en un archivo llamado `tareas.json` en el mismo directorio donde se ejecuta la aplicación.

**Ubicación:**
- Mismo directorio que `gestap.py`
- Nombre: `tareas.json`

**Formato del archivo:**
```json
[
  {
    "id": 1,
    "descripcion": "Comprar leche",
    "prioridad": "media",
    "completada": false,
    "fecha_creacion": "2025-11-24 10:30:15",
    "fecha_completado": null
  }
]
```

### Respaldo de Datos

**Recomendación:** Realiza copias de seguridad periódicas de `tareas.json`

```bash
# Linux/macOS
cp tareas.json tareas_backup_$(date +%Y%m%d).json

# Windows
copy tareas.json tareas_backup_%date%.json
```

### Migración de Datos

Para mover tus tareas a otra computadora:
1. Copia el archivo `tareas.json`
2. Colócalo en el directorio donde ejecutarás GESTAP
3. Ejecuta GESTAP normalmente

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Problemas Comunes

#### Error: "python no reconocido como comando"
**Síntomas:** El sistema no encuentra Python  
**Solución:**
```bash
# Verificar instalación
python3 --version
# o intentar
python3 gestap.py
```

#### Error: "No module named 'json'"
**Síntomas:** Error al ejecutar la aplicación  
**Solución:** Actualizar Python a versión 3.6+

#### Error: "Permission denied"
**Síntomas:** No se puede ejecutar en Linux/macOS  
**Solución:**
```bash
chmod +x gestap.py
```

#### Archivo de tareas corrupto
**Síntomas:** Error al cargar tareas existentes  
**Solución:**
1. Renombrar `tareas.json` a `tareas_corrupto.json`
2. Reiniciar GESTAP (creará nuevo archivo)
3. Recuperar datos manualmente si es necesario

### Problemas de Codificación

Si ves caracteres extraños en lugar de emojis:
- **Windows:** Usar Windows Terminal en lugar de CMD
- **Linux/macOS:** Verificar que el terminal soporte UTF-8

### Depuración

Para activar modo de depuración, ejecuta:
```bash
python -u gestap.py
```

---

## ❓ PREGUNTAS FRECUENTES (FAQ)

### ¿Puedo usar GESTAP en múltiples computadoras?
Sí, solo necesitas copiar el archivo `tareas.json` entre dispositivos.

### ¿Hay límite en el número de tareas?
No hay límite técnico, pero se recomienda no exceder 1000 tareas para mantener buen rendimiento.

### ¿Puedo cambiar la prioridad de una tarea existente?
Actualmente no, pero puedes eliminar la tarea y recrearla con la nueva prioridad.

### ¿GESTAP guarda automáticamente?
Sí, todos los cambios se guardan automáticamente en `tareas.json`.

### ¿Puedo exportar mis tareas?
El archivo `tareas.json` puede abrirse con cualquier editor de texto o importarse a otras aplicaciones.

### ¿Funciona GESTAP sin conexión a internet?
Sí, GESTAP es completamente offline y no requiere internet.

### ¿Puedo personalizar los comandos?
La versión actual no permite personalización, pero puedes modificar el código fuente.

---

## 📞 SOPORTE Y CONTACTO

### Recursos de Ayuda

- **Comando de ayuda integrado:** `help` dentro de la aplicación
- **Manual de usuario:** Este documento
- **Archivo de código fuente:** `gestap.py` (contiene comentarios detallados)

### Reportar Problemas

Si encuentras errores o tienes sugerencias:

1. **Verifica** que tienes la versión más reciente
2. **Documenta** el error con pasos para reproducirlo  
3. **Incluye** tu sistema operativo y versión de Python
4. **Adjunta** el archivo `tareas.json` si es relevante

### Información de Versión

Para verificar tu versión de GESTAP:
- La versión se muestra al iniciar la aplicación
- También está documentada en este manual

---

## 📝 HISTORIAL DE VERSIONES

| Versión | Fecha | Cambios |
|---------|--------|---------|
| 1.0 | 24/11/2025 | Versión inicial con funcionalidades básicas |

---

## 📄 LICENCIA Y TÉRMINOS DE USO

GESTAP es un software educativo. Puedes usarlo, modificarlo y distribuirlo libremente para fines educativos y personales.

---

**© 2025 GESTAP - Gestor de Tareas Personales**  
*"Organiza tu día, alcanza tus metas"*

---

> 💡 **Tip:** Mantén este manual a mano durante tus primeros días usando GESTAP. ¡La práctica hace al maestro!
