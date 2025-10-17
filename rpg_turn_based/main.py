# main.py
from core.character import Heroe
from core.battle import Batalla
from core.save_manager import SaveManager

def main():
    print("🎮 Bienvenido al RPG de Computación 2025 🎮")

    save_manager = SaveManager()
    heroes, enemigos, turno_guardado = save_manager.cargar_partida()

    if heroes is None:  # No hay partida guardada
        print("\nCreando nueva partida...\n")
        heroe1 = Heroe("Agustina", "Guerrero")
        heroe2 = Heroe("Coti", "Mago")
        heroe3 = Heroe("Tadeo", "Arquero")
        heroes = [heroe1, heroe2, heroe3]

        batalla = Batalla(heroes)
        batalla.generar_enemigos(cantidad=2, nivel_min=1, nivel_max=2)
    else:
        print("\nContinuando partida anterior...\n")
        batalla = Batalla(heroes)
        batalla.enemigos = enemigos
        batalla.turno = turno_guardado

    # --- Bucle principal de batalla ---
    batalla.iniciar()

    # Al final de la batalla, ofrecer guardar
    opcion = input("\n¿Deseas guardar la partida? (s/n): ")
    if opcion.lower() == "s":
        save_manager.guardar_partida(batalla.heroes, batalla.enemigos, batalla.turno)

if __name__ == "__main__":
    main()

