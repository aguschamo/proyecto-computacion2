# main.py
from core.menu import MenuPrincipal

def main():
    """
    Punto de entrada principal del juego.
    Muestra el menú inicial y permite al jugador
    comenzar una nueva partida, cargar una existente o salir.
    """
    print("🎮 Bienvenido al RPG de Computación 2025 🎮")
    print("===========================================")
    print("Un proyecto creado por estudiantes de Ingeniería 👩‍💻")
    print("===========================================\n")

    menu = MenuPrincipal()
    menu.mostrar_menu()

if __name__ == "__main__":
    main()

