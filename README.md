# GESTAP - Gestor de Tareas Personales

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Educational-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0-orange.svg)](CHANGELOG.md)

## 🎯 Descripción

**GESTAP** es una aplicación simple de línea de comandos para la gestión de tareas personales. Desarrollada en Python, ofrece una interfaz intuitiva y funcionalidades esenciales para organizar tu productividad diaria.

## ✨ Características

- 📝 **Gestión Completa**: Agregar, listar, completar y eliminar tareas
- 🎨 **Interfaz Visual**: Emojis y colores para mejor experiencia
- 🔄 **Persistencia**: Guarda automáticamente en formato JSON
- 📊 **Estadísticas**: Seguimiento de progreso y productividad
- ⚡ **Prioridades**: Organiza tareas por niveles de importancia
- 💾 **Ligero**: Sin dependencias externas, solo Python estándar

## 🚀 Inicio Rápido

### Instalación

```bash
# Clonar o descargar
git clone <repository-url>
cd gestap

# Ejecutar directamente
python gestap.py
```

### Uso Básico

```bash
# Iniciar GESTAP
python gestap.py

# Comandos esenciales
GESTAP> add "Mi primera tarea"
GESTAP> list
GESTAP> complete 1
GESTAP> stats
```

## 📖 Documentación

- 📘 **[Manual de Usuario Completo](MANUAL_USUARIO_GESTAP.md)** - Guía detallada con ejemplos
- 🛠️ **[Guía de Instalación](MANUAL_USUARIO_GESTAP.md#instalación)** - Instrucciones paso a paso
- ❓ **[FAQ](MANUAL_USUARIO_GESTAP.md#preguntas-frecuentes-faq)** - Preguntas frecuentes

## 💻 Requisitos

- **Python**: 3.6 o superior
- **SO**: Windows, macOS, Linux
- **Memoria**: 64 MB RAM
- **Disco**: 10 MB de espacio

## 📋 Comandos Disponibles

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `add` | Agregar tarea | `add "Comprar leche" alta` |
| `list` | Listar pendientes | `list` |
| `listall` | Listar todas | `listall` |
| `complete` | Completar tarea | `complete 1` |
| `delete` | Eliminar tarea | `delete 2` |
| `stats` | Ver estadísticas | `stats` |
| `help` | Mostrar ayuda | `help` |
| `exit` | Salir | `exit` |

## 🎨 Capturas de Pantalla

### Lista de Tareas
```
============================================================
📋 GESTAP - Lista de Tareas
============================================================
⏳ ID: 1 | 🔴 ALTA
   📝 Estudiar para examen final
   📅 Creada: 2025-11-24 10:30:15
------------------------------------------------------------
⏳ ID: 2 | 🟡 MEDIA  
   📝 Comprar víveres para la semana
   📅 Creada: 2025-11-24 11:15:30
------------------------------------------------------------
```

### Estadísticas
```
========================================
📊 ESTADÍSTICAS
========================================
📋 Total de tareas: 8
✅ Completadas: 5
⏳ Pendientes: 3
📈 Progreso: 62.5%
```

## 📁 Estructura del Proyecto

```
gestap/
│
├── gestap.py                 # Aplicación principal
├── MANUAL_USUARIO_GESTAP.md  # Manual de usuario completo
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias (opcional)
├── CHANGELOG.md             # Historial de cambios
└── tareas.json              # Archivo de datos (se crea automáticamente)
```

## 🔧 Solución de Problemas

### Error Común: Python no encontrado
```bash
# Verificar instalación
python --version
# o intentar
python3 --version

# Si no está instalado, descargar de:
# https://www.python.org/downloads/
```

### Permisos en Linux/macOS
```bash
chmod +x gestap.py
python3 gestap.py
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea tu rama de característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Roadmap

- [ ] Integración con calendarios
- [ ] Notificaciones de recordatorio
- [ ] Categorías personalizadas
- [ ] Interfaz web opcional
- [ ] Sincronización en la nube

## 📜 Licencia

Este proyecto está licenciado bajo términos educativos - ver el archivo [LICENSE](LICENSE) para detalles.

## 👤 Autor

**GESTAP Team**
- 📧 Email: soporte@gestap.app
- 🌐 Website: [gestap.app](https://gestap.app)

## 🙏 Agradecimientos

- Comunidad Python por las librerías estándar
- Usuarios beta por el feedback invaluable
- Contribuidores del proyecto

---

## 📊 Estado del Proyecto

- ✅ **Estable**: Versión 1.0 lista para producción
- 🧪 **Testeado**: Funciona en Windows, macOS y Linux
- 📚 **Documentado**: Manual completo disponible
- 🚀 **Activo**: En desarrollo continuo

---

*⭐ Si te gusta GESTAP, ¡no olvides darle una estrella al proyecto!*

**GESTAP** - *"Organiza tu día, alcanza tus metas"*
