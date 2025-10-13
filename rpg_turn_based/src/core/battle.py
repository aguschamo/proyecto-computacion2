import random 
from core.character import Heroe, Enemigo 
from core.item import GestordeItems 

#CLASE BATALLA 

class Batalla: 
    #Clase que gestiona el combate por turnos entre un grupo de héroes y enemigos 
    def __init__(self, heroes):
        self.heroes = heroes 
        self.enemigos = []
        self.gestor_items = GestorDeItems()
        self.turno = 1 
    
    def generar_enemigos(self, cantidad, nivel_min, nivel_max): 
        #genera una lista de enemigos aleatorios
        self.enemigos = [Enemigo.generar_aleatorio(nivel_min, nivel_max) for _ in range(cantidad)]
    
    def mostrar_estado(self): 
        #muestra el estado actual de todos los personajes
        print("\n--- ESTADO DE BATALLA ---")
        print("🧙‍♂️ Héroes:")
        for i, h in enumerate(self.heroes, start = 1):
            estado = f"{i}. {h.nombre} ({h.clase.capitalize()}) - Salud {h.salud}/{h.salud_max}"
            print(estado)
        
        print("\n👹 Enemigos:")
        for i, e in enumerate(self.enemigos, start=1): 
            estado = f"{i}. {e.nombre} -Salud {e.salud}/{e.salud_max}"
            print (estado)
        print("--------------")
    def todos_vivos(self, lista):
         #Devuelve True si al menos uno en la lista está vivo
        return any(p.esta_vivo() for p in lista)
    
    def turno_heroes(self): 
        #Turno de los héroes: el juegador elige acciones para cada héroe vivo
        for heroe in self.heroes:
            if not heroe.esta_vivo():
                continue
            
            print(f"\nTurno de {heroe.nombre} ({heroe.clase.capitalize()})") 
            print("1. Atacar")
            print("2. Usar ítem")
            print("3. Pasar turno")
            opcion = input ("Elige una opción:")
            
            if opcion == "1": 
                #Mostar enemigos vivos 
                enemigos_vivos = [e for e in self.enemigos if e.esta_vivo()]
                if not enemigos_vivos:
                    print("No hay enemigos vivos para atacar")
                    continue 
            for i, enemigo in enumerate(enemigos_vivos, start = 1): 
                print(f"{i}. {enemigo.nombre} ({enemigo.salud}/{enemigo.salud_max})")
                
            eleccion = input ("Elige enemigo a atacar:")
            try: 
                enemigo_objetivo = enemigos_vivos [int(eleccion) - 1]
            except (ValueError, IndexError): 
                print("Opcion inválida, turno perdido")
                continue 
            daño = heroe.atacar(enemigo_objetivo)
            print(f"{heroe.nombre} ataco a {enemigo_objetivo.nombre} e hizo {daño} de daño")
            if not enemigo_objetivo.esta_vivo():
                print(f"💀 {enemigo_objetivo.nombre} fue derrotao!")     