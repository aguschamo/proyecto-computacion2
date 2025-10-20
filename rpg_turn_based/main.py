#main.py
from core.menu import MenuPrincipal # Importa la clase del menú principal
import time
import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    limpiar_pantalla()  
    print("Bienvenido al RPG de Computación 2025 ")
    print("Un proyecto creado por estudiantes de Ingeniería en informática")
    time.sleep(2)
    print("Inspirado en la serenidad y la magia de los mundos de Studio Ghibli.\n ")
    time.sleep(2)

    menu = MenuPrincipal()
    while True:
        opcion = menu.mostrar_menu()  # Asumimos que mostrar_menu devuelve la opción elegida

        if opcion == "nueva_partida":
            resultado = menu.iniciar_historia()  # función que arranca la historia/batalla
            if resultado == "salir":
                continue  # vuelve al menú principal sin reiniciar la historia
        elif opcion == "cargar_partida":
            menu.cargar_partida()
        elif opcion == "salir":
            print("\n Gracias por explorar el bosque...")
            print("Que los espíritus de la naturaleza te acompañen en tu viaje.\n")
            time.sleep(1.2)
            break

if __name__ == "__main__":
    main()  
