import json
import random
import os

# CLASE ITEM
class Item:
    """Representa un item del juego. Puede ser curativo o de mejora (Afecta fuerza o defensa)."""

    def __init__(self, nombre, tipo, efecto, descripcion):
        self.nombre = nombre
        self.tipo = tipo 
        self.efecto = efecto  
        self.descripcion = descripcion 

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.descripcion}: {self.efecto}"
    

# CLASE GESTOR DE ITEMS
class GestorDeItems:
    """Administra la carga de ítems desde un archivo JSON y la selección aleatoria de drops."""

    def __init__(self, ruta_archivo="data/items.json"):
        self.ruta_archivo = ruta_archivo
        self.items = self.cargar_items()  

    def cargar_items(self):
        """Carga los ítems desde un archivo JSON."""
        if not os.path.exists(self.ruta_archivo):
            print(f"El archivo {self.ruta_archivo} no existe.")
            return []

        items = []
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for item_data in datos:
                item = Item(
                    nombre=item_data['nombre'],
                    tipo=item_data['tipo'],
                    efecto=item_data['efecto'],
                    descripcion=item_data['descripcion']
                )
                items.append(item)

        return items

    def obtener_item_aleatorio(self, nombre):
        """Devuelve un item según su nombre."""
        for item in self.items:
            if item.nombre.lower() == nombre.lower():
                return item
        return None  

    def drop_aleatorio(self):
        """Devuelve un item aleatorio (simula que un enemigo dejó caer algo).
        Probabilidad: 50% de que dropee un item, 50% de que no."""
        prob = random.random()
        if prob < 0.5:
            return None
        return random.choice(self.items)
