from core.character import Heroe
from core.dungeon import GestorDeMazmorras
from core.save_manager import SaveManager
import time

class MenuPrincipal:
    """
    Muestra el menú principal y gestiona la navegación entre opciones.
    """
    def __init__(self):
        self.save_manager = SaveManager()
    
    def mostrar_menu(self):
        while True:
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
                print("¡Gracias por jugar! Hasta la próxima aventura.")
                time
                # Break the loop to exit
                break
            else:
                print("\n Opción inválida, por favor intenta de nuevo.")

    def nueva_partida(self):
        """Crea una nueva partida"""
        print("\n Creando nueva partida...\n")
        time.sleep(1) #simula tiempo de carga

        heroe1 = Heroe("Agustina", "Guerrero")
        heroe2 = Heroe("Coti", "Mago")
        heroe3 = Heroe("Tadeo", "Arquero")
        heroes = [heroe1, heroe2, heroe3]

        gestor = GestorDeMazmorras(heroes)
        resultado = gestor.jugar()
        # Si el jugador eligió abandonar la partida desde una batalla, volver al menú
        if resultado == "salir":
            print("Volviendo al menú principal.")
            return

        # Al terminar la aventura normalmente, permitir guardar
        opcion = input("\n¿Deseas guardar la partida? (s/n): ")
        if opcion.lower() == "s": 
            self.save_manager.guardar_partida(gestor.heroes, [], 0)  # enemigos y turno iniciales
            print("Partida guardada exitosamente.")
        
    def cargar_partida(self):
        """Carga una partida guardada, si existe"""
        heroes, enemigos, turno = self.save_manager.cargar_partida()
        if heroes is None:
            print("\n No se encontró ninguna partida guardada.")
            return
        
        print("\n Cargando tu aventura...\n")
        time.sleep(1)
        gestor = GestorDeMazmorras(heroes)
        resultado = gestor.jugar()
        if resultado == "salir":
            print("Volviendo al menú principal.")
            return