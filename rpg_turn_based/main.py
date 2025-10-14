# main.py
from core.character import Heroe
from core.battle import Batalla

def main():
    print("🎮 Bienvenido al RPG de Computación 2025 🎮")
    print("Preparando a tus héroes...\n")

    # Crear grupo de héroes
    heroe1 = Heroe("Agustina", "Guerrero")
    heroe2 = Heroe("Luna", "Mago")
    heroe3 = Heroe("Tadeo", "Arquero")
    heroes = [heroe1, heroe2, heroe3]

    # Iniciar batalla
    batalla = Batalla(heroes)
    batalla.generar_enemigos(cantidad=2, nivel_min=1, nivel_max=2)
    batalla.iniciar()

if __name__ == "__main__":
    main()
