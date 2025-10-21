from core.battle import Batalla 
from core.character import Heroe, Enemigo 
import time
import random 

"""Clase Mazmorra 
Representa un santuario o lugar del mundo natural, con su atmósfera,
enemigos espirituales y un guardián ancestral al final."""

class Mazmorra:    
    def __init__(self, nombre, descripcion, enemigos,jefe): 
        self.nombre = nombre
        self.descripcion = descripcion 
        self.enemigos = enemigos 
        self.jefe = jefe 
    
    def introducir(self): #Narrativa de introducción a la mazmorra
        print(f"\n Entrás en {self.nombre}...")
        time.sleep(5)
        print(f" {self.descripcion}")
        time.sleep(5)
        print("Sentís una energía ancestral vibrar en el aire...\n")
        time.sleep(5)

#Clase Gestor de Mazmorras 
#Controla el avance entre las diferentes mazmorras
#Cada mazmorra tiene su propio grupo de enemigos y un jefe final 

class GestorDeMazmorras: 
    def __init__(self, heroes):
        self.heroes = heroes
        self.nivel_actual = 1
        self.mazmorras = self.crear_mazmorras()
    
    def crear_mazmorras(self):
#Crea las mazmorras del mundo Ghibli  
        return [
            Mazmorra(
                "Bosque de los Susurros",
                "Los árboles se mueven suavemente como si respiraran. Pequeños espíritus de musgo te observan desde las raíces.", 
                enemigos = 2, 
                jefe = "Espíritu del Roble Ancestral"
            ),
            Mazmorra(
                "Ruinas del Vientos Antiguo", 
                "Entre columnas cubiertas de enredaderas, el aire canta melodías antiguas. Algo poderoso duerme bajo las piedras.", 
                enemigos = 3,
                jefe = "Guardían del Eco"
            ), 
            Mazmorra(
                "Santuario de la luna",
                "Un lago plateado refleja el cielo estrellado. Los espíritus flotan sobre el agua, susurrando plegarias olvidadas", 
                enemigos = 3, 
                jefe = "Sombra del Reflejo Lunar"
            )
        ]
    def jugar(self): 
#Ejecuta el recorrido narrativo y de combate de las mazmorras"
        print("\n Comienza su travesía por los Santuarios del Bosque Eterno...\n")
        time.sleep(5)
        
        for i, mazmorra in enumerate(self.mazmorras, start =1):
            mazmorra.introducir()
            # --- Combates Normales ---
            for num in range(mazmorra.enemigos): 
                print(f"Encuentro {num + 1} en {mazmorra.nombre}...")
                time.sleep(5)
                batalla = Batalla(self.heroes)
                batalla.generar_enemigos(cantidad=1, nivel_min=i, nivel_max=i + 1)
                resultado = batalla.iniciar()
                
                if resultado == "salir":
                    # El jugador decidió abandonar y volver al menú
                    return "salir"
                
                if not any(h.esta_vivo() for h in self.heroes): 
                    print("\n Todos los espíritus protectores han caído...")
                    print("El bosque guarda silencio una vez más")
                    return False
                
                # --- Jefe Final --- 
                print(f"\n Se aproxima una presencia poderosa")
                time.sleep(5)
                jefe = Enemigo(mazmorra.jefe, nivel=i + 2)
                batalla_jefe = Batalla(self.heroes)
                batalla_jefe.enemigos = [jefe]
                resultado_jefe = batalla_jefe.iniciar()
                
                if resultado_jefe == "salir":
                    print("\n Has abandonado tu destino... por ahora.")
                    return "salir"
                    
                if not any(h.esta_vivo() for h in self.heroes): 
                    print("\n Todos los héroes han caído bajo la luna.")
                    time.slepp(5)
                    
                print(f"\n Has purificado {mazmorra.nombre}. Los espíritus descansan en paz\n")
                time.sleep(5)
            print("\n ¡Has completado todos los santuarios del Bosque Eterno!")
            print("El equilibrio ha sido restaurado.\n")
            return True 