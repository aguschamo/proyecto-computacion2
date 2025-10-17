import json
import os
from core.character import Heroe, Enemigo

#Clase SaveManager que gestiona la carga y guardado de partidas

class SaveManager:
    """Maneja el guardado y carga de partidas usando archivos JSON.
    Guarda los datos esenciales: heroe, enemigos y turno actual"""
    def __init__(self, ruta_archivo= 'data/savegame.json'): 
        self.ruta_archivo = ruta_archivo
    
    # Guarda una partida en un archivo JSON
    def guardar_partida(self, heroes, enemigos, turno):
        """Guarda el estado actual de la partida en un archivo JSON"""
        datos_guardar = {
            "heroes": [self._serializar_personaje(h) for h in heroes], #convierte objetos Heroe a diccionarios
            "enemigos": [self._serializar_personaje(e) for e in enemigos], #convierte objetos Enemigo a diccionarios
            "turno": turno 
        }
        os.makedirs(os.path.dirname(self.ruta_archivo), exist_ok=True) #asegura que la carpeta exista
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo: #abre el archivo para escribir
            json.dump(datos_guardar, archivo, indent=4, ensure_ascii=False) #guarda los datos en formato JSON
        print(f"Partida guardada exitosamente en '{self.ruta_archivo}'.")

#Carga una partida desde un archivo JSON
    def cargar_partida(self):
        """Carga el estado de la partida desde un archivo JSON"""
        if not os.path.exists(self.ruta_archivo): #verifica si el archivo existe
            print(f"No se encontró ningún archivo de guardado en '{self.ruta_archivo}', comenzando una nueva partida.")
            return None, None, 1  # Retorna valores por defecto si no existe el archivo
        
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo: #abre el archivo para leer
            datos = json.load(archivo) #carga los datos desde el archivo JSON
            
        heroes = [self._dict_a_heroe(h_data) for h_data in datos["heroes"]] #convierte diccionarios a objetos Heroe
        enemigos = [self._dict_a_enemigo(e_data) for e_data in datos["enemigos"]] #convierte diccionarios a objetos Enemigo
        turno = datos.get("turno", 1) # Valor por defecto 1 si no existe

        print(f"Partida cargada exitosamente desde '{self.ruta_archivo}'.")
        return heroes, enemigos, turno
     
#funciones auxiliares 

    def _personaje_a_dict(self, personaje):
        """Convierte un objeto Personaje (Heroe o Enemigo) a un diccionario para guardado"""
        base= { 
            "tipo": personaje.__class__.__name__, #Guarda el tipo de clase
            "nombre": personaje.nombre,
            "nivel": personaje.nivel,
            "salud": personaje.salud,
            "salud_max": personaje.salud_max,
            "fuerza": personaje.fuerza,
            "defensa": personaje.defensa
        }

        if isinstance(personaje, Heroe):
          base["clase"] = personaje.clase 
          base["experiencia"] = personaje.experiencia
        return base

    def _dict_a_heroe(self,datos):
        """Convierte un diccionario a un objeto Heroe"""
        heroe = Heroe(datos["nombre"], datos["clase"], datos["nivel"])
        heroe.salud = datos["salud"]
        heroe.salud_max = datos["salud_max"]
        heroe.fuerza = datos["fuerza"]
        heroe.defensa = datos["defensa"]
        heroe.experiencia = datos.get("experiencia", 0) #Por si no existe en el diccionario
        return heroe

    def _dict_a_enemigo(self, datos):
        """Convierte un diccionario a un objeto Enemigo"""
        enemigo = Enemigo(datos["nombre"], datos["nivel"])
        enemigo.salud = datos["salud"]
        enemigo.salud_max = datos["salud_max"]
        enemigo.fuerza = datos["fuerza"]
        enemigo.defensa = datos["defensa"]
        return enemigo