from core.character import Heroe, Enemigo 

#creo los heroes 
guerrero= Heroe ("agustina", "guerrero")
mago = Heroe ("luna", "mago")

#crear enemigo 
enemigo = Enemigo.generar_aleatoria(1,2)

print(guerrero)
print(mago)
print(enemigo)

#simulacion de ataque 
daño = guerrero.atacar(enemigo)
print(f"{guerrero.nombre} ataco a {enemigo.nombre} e hizo {daño} de daño")
print(enemigo)

#ganar experiencia 
guerrero.ganar_experiencia(120) 
