import random 
# CLASE: PERSONAJE 
class Personaje: 
    
    def __init__(self, nombre, nivel, salud_max, fuerza, defensa): 
        self.nombre = nombre
        self.nivel = nivel
        self.salud_max = salud_max
        self.salud = salud_max  # salud actual
        self.fuerza = fuerza
        self.defensa = defensa

    def esta_vivo(self):
        # Devuelve True si el personaje sigue con vida
        return self.salud > 0

    def recibir_daño (self, daño):
        # Resta salud según el daño recibido y la defensa.
        # Devuelve el daño efectivo que se aplicó
        daño_efectivo = max(0, daño - self.defensa)
        self.salud = max(0, self.salud - daño_efectivo)
        return daño_efectivo

    def atacar(self, otro):
        # Realiza un ataque básico. Devuelve el daño infligido
        # Se agrega una pequeña variación aleatoria al daño
        variacion = random.randint(-2, 2)
        poder = self.fuerza + variacion 
        daño = otro.recibir_daño(poder)
        return daño

    def curar (self, cantidad):
        # Restaura salud (sin pasar del máximo)
        self.salud = min(self.salud + cantidad, self.salud_max)

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel}) - Salud: {self.salud}/{self.salud_max}"

 #CLASE HEROE 
 
class Heroe(Personaje): 
     #representa a un personaje controlado por el jugador 
     #incluye experiencia y subida de nivel 
     
     def __init__ (self, nombre, clase, nivel = 1): 
         self.clase = clase.lower()
         self.experiencia = 0 
        #atributos base según la clase del héroe 
         if self.clase =="guerrero":
              salud_max = 120
              fuerza = 15 
              defensa = 8 
         elif self.clase == "mago": 
             salud_max = 80
             fuerza =20
             defensa =4
         elif self.clase == "arquero":
             salud_max = 95
             fuerza = 13
             defensa = 6 
         else: 
             #clase por defecto 
             salud_max =100
             fuerza = 10 
             defensa = 5
         
         super().__init__(nombre, nivel, salud_max, fuerza, defensa)
     def ganar_experiencia(self, cantidad): 
         #suma experiencia. si supere el umbral, sube de nivel 
         #cada nivel requiere nivel_actual * 100 puntos 
         self.experiencia += cantidad 
         experiencia_necesaria = self.nivel * 100 
         
         #subida de nivel 
         if self.experiencia <= experiencia_necesaria: 
            self.experiencia -= experiencia_necesaria 
            self.nivel += 1 
            self.salud_max +- 2 
            self.defensa += 1 
            self.salud = self.salud_max #se cura completamente 
            print(f"{self.nombre} Felicitaciones, subiste de nivel {self.nivel}!")
     
     def usar_item(self, item):
         #aplica el efecto de un item. La estructura de "item" se define en el módulo de ítems
         if item ["tipo"] == "curativo": 
             self.curar(item["efecto"])
             print(f"{self.nombre} uso {item['nombre']} y recupero {item['efecto']} de salud")
         elif item ["tipo"] == "mejora":
             self.fuerza += item ["efecto"]
             print(f"{self.nombre} uso {item['nombre']} y aumento su fuerza en {item['efecto']} puntos")

#CLASE ENEMIGO 
class Enemigo(Personaje):
    #Representa a un enemigo generado aleatoriamente
    #Los atributos dependen del nivel 
    def __init__(self, nombre, nivel): 
      salud_max = 50 + 15 * nivel 
      fuerza = 8 + 3 * nivel 
      defensa = 2 + nivel 
      super().__init__(nombre, nivel, salud_max, fuerza, defensa)

    @staticmethod
    def generar_aleatorio(nivel_min, nivel_max):
        #genera un enemigo aleatorio entre un rango de niveles 
        nombres = ["Globin", "Lobo", "Bandido", "Esqueleto", "Orco", "Arca"]
        nombre = random.choice(nombres)
        nivel = random.randint(nivel_min, nivel_max)
        return Enemigo(nombre, nivel)
 