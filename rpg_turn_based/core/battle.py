import random 
from core.character import Heroe, Enemigo 
from core.item import GestorDeItems 

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
        print("Héroes:")
        for i, h in enumerate(self.heroes, start = 1):
            estado = f"{i}. {h.nombre} ({h.clase.capitalize()}) - Salud {h.salud}/{h.salud_max}"
            print(estado)
        
        print("\nEnemigos:")
        for i, e in enumerate(self.enemigos, start=1): 
            estado = f"{i}. {e.nombre} - Salud {e.salud}/{e.salud_max}"
            print(estado)
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
                print(f"{enemigo_objetivo.nombre} fue derrotado!")

            #Drop de item
            drop = self.gestor_items.drop_aleatorio()
            if drop:
                print(f"¡El enemigo dejó caer un ítem: {drop.nombre}!")
                heroe.usar_item({
                    "nombre": drop.nombre,
                    "tipo": drop.tipo,
                    "efecto": drop.efecto
                }
                )
            
            elif opcion == "2":
                print("Ítems disponibles(por ahora simulación simple):")
                pocion = self.gestor_items.obtener_item_por_nombre("Pocion pequeña")
                if pocion:
                    heroe.usar_item({
                        "nombre": pocion.nombre,
                        "tipo": pocion.tipo,
                        "efecto": pocion.efecto
                    })
                else:
                    print("No tienes ítems disponibles.")
            elif opcion == "3":
                print(f"{heroe.nombre} decide esperar este turno")
            else:
                print("Opción inválida, turno perdido")

    def turno_enemigos(self):
        #Turno de los enemigos: atacan a héroes aleatorios
       print("\n--- Turno de los Enemigos ---")
       heroes_vivos = [h for h in self.heroes if h.esta_vivo()]

       for enemigo in self.enemigos:
           if enemigo.esta_vivo() and heroes_vivos:
               objetivo = random.choice(heroes_vivos)
               daño = enemigo.atacar(objetivo)
               print(f"{enemigo.nombre} ataco a {objetivo.nombre} e hizo {daño} de daño")
               if not objetivo.esta_vivo():
                   print(f"{objetivo.nombre} fue derrotado!")
        
    def iniciar(self):
        """Ejecuta el flujo completo de la batalla hasta que un grupo pierda"""
        print("\n ¡Comienza la batalla!")
        while self.todos_vivos (self.heroes) and self.todos_vivos(self.enemigos):
            print(f"\n--- Turno {self.turno} ---")
            self.mostrar_estado()
            self.turno_heroes()
            if self.todos_vivos(self.enemigos):
                self.turno_enemigos()
            self.turno += 1

        print ("\n--- Batalla Terminada ---")
        if self.todos_vivos(self.heroes):
            print("¡Los héroes han ganado la batalla!")
            for h in self.heroes:
                if h.esta_vivo():
                    h.ganar_experiencia(50)  # Cada héroe vivo gana 50 de experiencia
                    print(f"{h.nombre} ganó 50 puntos de experiencia.")
        else:
            print("¡Los enemigos han ganado la batalla!")