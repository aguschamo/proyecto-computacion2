from core.battle import Batalla 
from core.character import Heroe, Enemigo 
import time
import random 

#Clase Mazmorra 
#Representa una mazmorra dentro del juego: cada mazmorra tiene: 
#un nombre, una descripcion narrativa, un numero de enemigos, un jefe final

class Mazmorra:    
    def __init__(self, nombre, descripcion, enemigos,jefe): 
        self.nombre = nombre
        self.descripcion = descripcion 
        self.enemigos = enemigos 
        self.jefe = jefe 
    
    def introducir(self): #Muestra la introduccion narrativa de la mazmorra
        print(f"Entrás a la {self.nombre}...")
        time.sleep(1.2)
        print(self.descripcion)
        time.sleep(1.5)
        print("Te preparás para el combate...\n")
        time.sleep(1.2)

#Clase Gestor de Mazmorras 
#Controla el avance entre las diferentes mazmorras
#Cada mazmorra tiene su propio grupo de enemigos y un jefe final 

class GestorDeMazmorras: 
    def __init__(self, heroes):
        self.heroes = heroes
        self.nivel_actual = 1
        self.mazmorras = self.crear_mazmorras()
    
    def crear_mazmorras(self):
#Crea las 3 mazmorras del juego con sus descripciones 
        return [
            Mazmorra(
                "Mazmorra del Bosque Oscuro",
                "Los árboles susurran mientras criaturas acechan entre las sombras. El aire huele a humedad y miedo.", 
                enemigos = 2, 
                jefe = "Lobo Alfa"
            ),
            Mazmorra(
                "Mazmorra del Volcán Carmesí", 
                "El calor es insoportable. El suelo tiembla y la lava ilumina las paredes... tu destino te espera.", 
                enemigos = 3,
                jefe = "Dragón de Fuego"
            )
        ]
    def jugar(self): 
#Ejecuta el recorrido completo de las mazmorras
        print("\n Comienza tu aventura a través de las mazmorras...\n")
        
        for i, mazmorra in enumerate(self.mazmorras, start =1):
            mazmorra.introducir()
#Batallas contra enemigos normales 
            for num in range(mazmorra.enemigos): 
                print(f"Combate {num + 1} en la {mazmorra.nombre}...")
                batalla = Batalla(self.heroes)
                batalla.generar_enemigos(cantidad =1, nivel_min=i, nivel_max=i + 1)
                batalla.iniciar()
                
                if not any(h.esta_vivo() for h in self.heroes): 
                    print("\n ¡El jefe final aparece! ({mazmorra.jefe})")
                    jefe = Enemigo(mazmorra.jefe, nivel=i + 2)
                    batalla_jefe = Batalla(self.heroes)
                    batalla_jefe.enemigos = [jefe]
                    batalla_jefe.iniciar()
                    
                    if not any(h.esta_vivo() for h in self.heroes): 
                        print("\n Todos los héroes cayeron... Fin de la aventura")
                        return False 
                    print(f"\n Has conquistado la {mazmorra.nombre}.\n")
                    time.sleep(1.5)
            print("\n ¡Felicitaciones! Has completado todas las mazmorras y derrotado al jefe final")
            return True 