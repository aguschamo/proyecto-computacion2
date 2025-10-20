from core.character import Heroe
from core.dungeon import GestorDeMazmorras
from core.save_manager import SaveManager
import time
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

class MenuPrincipal:
    """
    Muestra el menú principal y gestiona la navegación entre opciones.
    """
    def __init__(self):
        self.save_manager = SaveManager()
    
    def mostrar_menu(self):
        while True:
            limpiar_pantalla()
            print("Un viaje de calma, magia y espíritu \n")
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Nueva Partida")
            print("2. Cargar Partida")
            print("3. Salir")
            opcion = input("\n Elige una opción: ")

            if opcion == "1":
                self.nueva_partida()
            elif opcion == "2":
                self.cargar_partida()
            elif opcion == "3":
                print("Gracias por explorar el Bosque eterno...")
                print("Que los espiritus del viento te acompañen en tu viaje \n")
                time.sleep(1.2)
                break
            else:
                print("\n Opción inválida, por favor intenta de nuevo.")
                time.sleep(1.2)

    def nueva_partida(self):
        """Crea una nueva partida"""
        print("\n Comienza tu viaje...\n")
        time.sleep(1.5) #simula tiempo de carga
        print("El viento murmura entre las hojas...")
        print("Los espiritus del bosque despiertan para guiarte en tu aventura.\n")
        time.sleep(2)

        heroe1 = Heroe("Elaria", "Guardiana del Bosque")
        heroe2 = Heroe("Kael", "Alquimista del Aire")
        heroe3 = Heroe("Lyra", "Viajero del Sueño")
        heroes = [heroe1, heroe2, heroe3]

        gestor = GestorDeMazmorras(heroes)
        resultado = gestor.jugar()
        # Si el jugador eligió abandonar la partida desde una batalla, volver al menú
        if resultado == "salir":
            print("Has decidido descansar entre los árboles del bosque...\n Volviendo al menú principal.")
            time.sleep(1.5)
            return

        # Al terminar la aventura normalmente, permitir guardar
        opcion = input("\n¿Deseas guardar la partida? (s/n): ")
        if opcion.lower() == "s": 
            self.save_manager.guardar_partida(gestor.heroes, [], 0)  # enemigos y turno iniciales
            print("Partida guardada exitosamente.")
            time.sleep(1.5)
        
    def cargar_partida(self):
        """Carga una partida guardada, si existe"""
        limpiar_pantalla()
        print("Buscando tus recuerdos perdidos...\n")
        time.sleep(1.5)

        heroes, enemigos, turno = self.save_manager.cargar_partida()
        if heroes is None:
            print("\n No se encontró ninguna partida guardada.")
            time.sleep(2)
            return
        

        print("\n Tus guardianes despiertan de su descanso...\n")
        time.sleep(1.5)

        gestor = GestorDeMazmorras(heroes)
        resultado = gestor.jugar()

        if resultado == "salir":
            print("Has decidido volver al claro del bosque...\n Volviendo al menú principal.")
            time.sleep(1.5)
            return