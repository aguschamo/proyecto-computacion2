# core/item.py
import json
import random
import os


# CLASE ITEM
class Item:
    """
    Representa un ítem del juego. 
    Puede ser curativo o de mejora (afecta fuerza o defensa).
    """

    def __init__(self, nombre, tipo, efecto, descripcion):
        self.nombre = nombre
        self.tipo = tipo          # "curativo" o "mejora"
        self.efecto = efecto      # número que indica el efecto (ej: +20 HP o +3 fuerza)
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) → {self.descripcion}"

# CLASE GESTOR DE ITEMS
class GestorDeItems:
    """
    Administra la carga de ítems desde un archivo JSON
    y la selección aleatoria de drops.
    """

    def __init__(self, ruta_archivo=None):
        """
        Si no se pasa una ruta específica, busca automáticamente
        el archivo 'data/items.json' dentro del proyecto,
        sin importar desde dónde se ejecute el programa.
        """
        if ruta_archivo is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            ruta_archivo = os.path.join(base_dir, "data", "items.json")

        self.ruta_archivo = ruta_archivo
        self.items = []
        self.cargar_items()

    def cargar_items(self):
        """Carga los ítems desde un archivo JSON."""
        if not os.path.exists(self.ruta_archivo):
            print(f"Archivo de ítems no encontrado: {self.ruta_archivo}")
            return

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item_data in datos:
                    item = Item(
                        nombre=item_data["nombre"],
                        tipo=item_data["tipo"],
                        efecto=item_data["efecto"],
                        descripcion=item_data["descripcion"]
                    )
                    self.items.append(item)
        except Exception as e:
            print(f"Error al leer los ítems: {e}")

    def drop_aleatorio(self):
        """Devuelve un ítem aleatorio como drop, o None si no hay ítems."""
        if not self.items:
            print("No hay ítems disponibles para drop.")
            return None
        return random.choice(self.items)