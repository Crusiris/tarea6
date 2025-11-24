#!/usr/bin/env python3
"""
GESTAP - Gestor de Tareas Personales
Versión 1.0 - 24 de noviembre de 2025

Una aplicación simple de línea de comandos para gestionar tareas personales.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

class GestorTareas:
    def __init__(self, archivo_datos: str = "tareas.json"):
        """Inicializa el gestor de tareas."""
        self.archivo_datos = archivo_datos
        self.tareas = self._cargar_tareas()
        
    def _cargar_tareas(self) -> List[Dict]:
        """Carga las tareas desde el archivo JSON."""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def _guardar_tareas(self) -> None:
        """Guarda las tareas en el archivo JSON."""
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(self.tareas, f, ensure_ascii=False, indent=2)
    
    def agregar_tarea(self, descripcion: str, prioridad: str = "media") -> None:
        """Agrega una nueva tarea."""
        if not descripcion.strip():
            print("❌ Error: La descripción de la tarea no puede estar vacía.")
            return
            
        nueva_tarea = {
            "id": len(self.tareas) + 1,
            "descripcion": descripcion.strip(),
            "prioridad": prioridad.lower(),
            "completada": False,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_completado": None
        }
        
        self.tareas.append(nueva_tarea)
        self._guardar_tareas()
        print(f"✅ Tarea agregada con ID: {nueva_tarea['id']}")
    
    def listar_tareas(self, mostrar_completadas: bool = False) -> None:
        """Lista todas las tareas."""
        if not self.tareas:
            print("📋 No hay tareas registradas.")
            return
        
        print("\n" + "="*60)
        print("📋 GESTAP - Lista de Tareas")
        print("="*60)
        
        tareas_mostrar = self.tareas if mostrar_completadas else [t for t in self.tareas if not t['completada']]
        
        if not tareas_mostrar:
            print("📝 No hay tareas pendientes.")
            return
        
        for tarea in tareas_mostrar:
            estado = "✅" if tarea['completada'] else "⏳"
            prioridad_emoji = {"alta": "🔴", "media": "🟡", "baja": "🟢"}.get(tarea['prioridad'], "🟡")
            
            print(f"{estado} ID: {tarea['id']} | {prioridad_emoji} {tarea['prioridad'].upper()}")
            print(f"   📝 {tarea['descripcion']}")
            print(f"   📅 Creada: {tarea['fecha_creacion']}")
            
            if tarea['completada'] and tarea['fecha_completado']:
                print(f"   ✅ Completada: {tarea['fecha_completado']}")
            
            print("-" * 60)
    
    def completar_tarea(self, tarea_id: int) -> None:
        """Marca una tarea como completada."""
        tarea = self._buscar_tarea(tarea_id)
        if not tarea:
            print(f"❌ Error: No se encontró la tarea con ID {tarea_id}")
            return
        
        if tarea['completada']:
            print(f"ℹ️  La tarea {tarea_id} ya está completada.")
            return
        
        tarea['completada'] = True
        tarea['fecha_completado'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._guardar_tareas()
        print(f"✅ Tarea {tarea_id} marcada como completada.")
    
    def eliminar_tarea(self, tarea_id: int) -> None:
        """Elimina una tarea."""
        tarea = self._buscar_tarea(tarea_id)
        if not tarea:
            print(f"❌ Error: No se encontró la tarea con ID {tarea_id}")
            return
        
        self.tareas = [t for t in self.tareas if t['id'] != tarea_id]
        self._guardar_tareas()
        print(f"🗑️  Tarea {tarea_id} eliminada.")
    
    def _buscar_tarea(self, tarea_id: int) -> Optional[Dict]:
        """Busca una tarea por su ID."""
        return next((tarea for tarea in self.tareas if tarea['id'] == tarea_id), None)
    
    def mostrar_estadisticas(self) -> None:
        """Muestra estadísticas de las tareas."""
        total = len(self.tareas)
        completadas = len([t for t in self.tareas if t['completada']])
        pendientes = total - completadas
        
        print("\n" + "="*40)
        print("📊 ESTADÍSTICAS")
        print("="*40)
        print(f"📋 Total de tareas: {total}")
        print(f"✅ Completadas: {completadas}")
        print(f"⏳ Pendientes: {pendientes}")
        
        if total > 0:
            porcentaje = (completadas / total) * 100
            print(f"📈 Progreso: {porcentaje:.1f}%")


def mostrar_ayuda() -> None:
    """Muestra la ayuda del programa."""
    print("""
🚀 GESTAP - Gestor de Tareas Personales v1.0
================================================

COMANDOS DISPONIBLES:
  add <descripción> [prioridad]  - Agregar nueva tarea
  list                          - Listar tareas pendientes
  listall                       - Listar todas las tareas
  complete <id>                 - Marcar tarea como completada
  delete <id>                   - Eliminar tarea
  stats                         - Mostrar estadísticas
  help                          - Mostrar esta ayuda
  exit                          - Salir del programa

PRIORIDADES:
  alta, media, baja (por defecto: media)

EJEMPLOS:
  add "Comprar leche" alta
  complete 1
  delete 2

Para más información, consulte el manual de usuario.
    """)


def main():
    """Función principal del programa."""
    gestor = GestorTareas()
    
    print("🚀 Bienvenido a GESTAP - Gestor de Tareas Personales")
    print("Escribe 'help' para ver los comandos disponibles o 'exit' para salir.\n")
    
    while True:
        try:
            entrada = input("GESTAP> ").strip()
            
            if not entrada:
                continue
                
            partes = entrada.split()
            comando = partes[0].lower()
            
            if comando == "exit":
                print("👋 ¡Hasta luego!")
                break
            elif comando == "help":
                mostrar_ayuda()
            elif comando == "add":
                if len(partes) < 2:
                    print("❌ Error: Debe proporcionar una descripción para la tarea.")
                    continue
                descripcion = " ".join(partes[1:-1]) if len(partes) > 2 and partes[-1] in ["alta", "media", "baja"] else " ".join(partes[1:])
                prioridad = partes[-1] if len(partes) > 2 and partes[-1] in ["alta", "media", "baja"] else "media"
                gestor.agregar_tarea(descripcion, prioridad)
            elif comando == "list":
                gestor.listar_tareas(False)
            elif comando == "listall":
                gestor.listar_tareas(True)
            elif comando == "complete":
                if len(partes) != 2:
                    print("❌ Error: Debe proporcionar el ID de la tarea.")
                    continue
                try:
                    tarea_id = int(partes[1])
                    gestor.completar_tarea(tarea_id)
                except ValueError:
                    print("❌ Error: El ID debe ser un número.")
            elif comando == "delete":
                if len(partes) != 2:
                    print("❌ Error: Debe proporcionar el ID de la tarea.")
                    continue
                try:
                    tarea_id = int(partes[1])
                    gestor.eliminar_tarea(tarea_id)
                except ValueError:
                    print("❌ Error: El ID debe ser un número.")
            elif comando == "stats":
                gestor.mostrar_estadisticas()
            else:
                print(f"❌ Comando desconocido: '{comando}'. Escriba 'help' para ver los comandos disponibles.")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
