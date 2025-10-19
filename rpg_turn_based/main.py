#main.py
from core.menu import MenuPrincipal # Importa la clase del menú principal

def main():
    print(" Bienvenido al RPG de Computación 2025 ")
    print("===========================================")
    print("Un proyecto creado por estudiantes de Ingeniería en informática")
    print("===========================================\n")

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
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()  
