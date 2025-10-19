import random 
from core.character import Heroe, Enemigo 
from core.item import GestorDeItems
from core.save_manager import SaveManager 

#CLASE BATALLA 

class Batalla: 
    #Clase que gestiona el combate por turnos entre un grupo de héroes y enemigos 
    def __init__(self, heroes): 
        self.heroes = heroes 
        self.enemigos = []
        self.gestor_items = GestorDeItems()
        self.save_manager = SaveManager()
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
    
    # TURNOS DE BATALLA
    def turno_heroes(self):
        # Turno de los héroes: el jugador elige acciones para cada héroe vivo
        for heroe in self.heroes:
            if not heroe.esta_vivo():
                continue

            print(f"\nTurno de {heroe.nombre} ({heroe.clase.capitalize()})")
            print("1. Atacar")
            print("2. Usar ítem")
            print("3. Pasar turno")
            print("4. Abandonar batalla")
            opcion = input("Elige una opción:")

            if opcion == "1":
                # Mostrar enemigos vivos
                enemigos_vivos = [e for e in self.enemigos if e.esta_vivo()]
                if not enemigos_vivos:
                    print("No hay enemigos vivos para atacar")
                    continue

                # Si hay un solo enemigo, ataca directamente
                if len(enemigos_vivos) == 1:
                    enemigo_objetivo = enemigos_vivos[0]
                    print(f"{heroe.nombre} ataca directamente a {enemigo_objetivo.nombre}!")
                else:
                    # Si hay más de uno, mostrar menú de selección
                    for i, enemigo in enumerate(enemigos_vivos, start=1):
                        print(f"{i}. {enemigo.nombre} ({enemigo.salud}/{enemigo.salud_max})")

                    eleccion = input("Elige enemigo a atacar:")
                    try:
                        enemigo_objetivo = enemigos_vivos[int(eleccion) - 1]
                    except (ValueError, IndexError):
                        print("Opción inválida, turno perdido")
                        continue

                daño = heroe.atacar(enemigo_objetivo)
                print(f"{heroe.nombre} atacó a {enemigo_objetivo.nombre} y hizo {daño} de daño")

                if not enemigo_objetivo.esta_vivo():
                    print(f"{enemigo_objetivo.nombre} fue derrotado!")

                # DROP DE ÍTEM
                drop = self.gestor_items.drop_aleatorio()
                if drop and random.random() < 0.5:  # 50% de probabilidad de que el héroe recoja el ítem
                    print(f"¡El enemigo dejó caer un ítem: {drop.nombre}!")
                    heroe.inventario.append({
                        "nombre": drop.nombre,
                        "tipo": drop.tipo,
                        "efecto": drop.efecto
                    })
                    print(f"¡{heroe.nombre} recogió el ítem: {drop.nombre} y lo ha guardado en su inventario!")

            elif opcion == "2":
                if not heroe.inventario:
                    print(f"{heroe.nombre} no tiene ítems para usar.")
                    continue

                print("Ítems disponibles:")
                for i, item in enumerate(heroe.inventario, start=1):
                    print(f"{i}. {item['nombre']} ({item['tipo']}) → {item['efecto']}")

                eleccion_item = input("Elige el ítem a usar: ")
                try:
                    item_seleccionado = heroe.inventario[int(eleccion_item) - 1]
                except (ValueError, IndexError):
                    print("Opción inválida, turno perdido")
                    continue

                heroe.usar_item(item_seleccionado)
                # Opcional: remover el ítem del inventario si es de un solo uso
                heroe.inventario.pop(int(eleccion_item) - 1)

            elif opcion == "3":
                print(f"{heroe.nombre} decide esperar este turno.")

            elif opcion == "4":
                confirmar = input("¿Seguro que queres abandonar la batalla? (s/n): ")
                if confirmar.lower() == "s":
                    guardar = input("¿Deseas guardar tu progreso antes de salir? (s/n): ")
                    if guardar.lower() == "s":
                        self.save_manager.guardar_partida(self.heroes, self.enemigos, self.turno)
                        print("Partida guardada exitosamente.")
                    print("Abandonando la batalla...\n Volviendo al menú principal.")
                    self.enemigos = []  # Vaciar la lista de enemigos para terminar la batalla
                    return "salir"

            else:
                print("Opción inválida, turno perdido.")


    def turno_enemigos(self):
        #Turno de los enemigos: atacan a héroes aleatorios
        print("\n--- Turno de los Enemigos ---")
        heroes_vivos = [h for h in self.heroes if h.esta_vivo()]

        for enemigo in self.enemigos:
            if enemigo.esta_vivo() and heroes_vivos:
                objetivo = random.choice(heroes_vivos)
                daño = enemigo.atacar(objetivo)
                print(f"{enemigo.nombre} atacó a {objetivo.nombre} y hizo {daño} de daño")
                if not objetivo.esta_vivo():
                    print(f"{objetivo.nombre} fue derrotado!")
        
    def iniciar(self):
        """Ejecuta el flujo completo de la batalla hasta que un grupo pierda"""
        print("\n ¡Comienza la batalla!")
        while self.todos_vivos (self.heroes) and self.todos_vivos(self.enemigos):
            print(f"\n--- Turno {self.turno} ---")
            self.mostrar_estado()
            resultado = self.turno_heroes()
            if resultado == "salir":
                # Se solicitó abandonar la batalla y ya se guardó si el jugador lo pidió
                return "salir"
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