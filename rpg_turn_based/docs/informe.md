informe = """
## Informe del proyecto: RPG por turnos

**Fecha:** 25/10/2025

Acá les cuento cómo está armado nuestro proyecto, qué cambios hicimos, cómo funciona el juego y qué podríamos mejorar o agregar más adelante.  

---

### Resumen

Hicimos un RPG por turnos inspirado en el estilo de Studio Ghibli. El juego tiene un menú principal, mazmorras con enemigos, combates por turnos, ítems que los héroes pueden usar y un sistema de guardado para no perder la partida.  

En esta versión corregimos varias cosas importantes: ahora el menú funciona mejor, se guarda la partida sin problemas, los héroes suben de nivel correctamente, los ítems se aplican como deberían, y las mazmorras ya no tienen errores raros que cortaban el juego.  

---

### Cómo está organizado el proyecto

- `main.py` → Es el archivo que arranca el juego y abre el menú.  
- `core/` → Acá está toda la lógica del juego:
  - `character.py` → Define los héroes y los enemigos.  
  - `battle.py` → Controla los combates por turnos.  
  - `dungeon.py` → Maneja las mazmorras y los encuentros con enemigos.  
  - `item.py` → Maneja los ítems y cómo se consiguen.  
  - `menu.py` → El menú que ves por consola.  
  - `save_manager.py` → Guarda y carga las partidas.  
- `data/` → Archivos de ejemplo como los ítems o partidas guardadas.  
- `docs/` → Documentación y el diagrama del juego.  

---

### Qué hace cada parte

- **Héroes y enemigos:** Cada personaje tiene nombre, nivel, salud, fuerza y defensa. Los héroes además tienen clase, experiencia e inventario.  
- **Ítems:** Pueden curar o mejorar fuerza/defensa. Se pueden conseguir aleatoriamente al vencer enemigos.  
- **Combates:** Se turnan los héroes y los enemigos; los héroes pueden atacar, usar ítems, pasar o rendirse.  
- **Mazmorras:** Se recorren enfrentando enemigos normales y al final aparece un jefe.  
- **Menú:** Desde ahí se empieza una partida nueva o se carga una guardada.  
- **Guardado:** Ahora se guarda todo lo importante, incluyendo los ítems que tienen los héroes.  

---

### Cambios importantes que hicimos

- El menú ahora es más simple y estable.  
- Las partidas se guardan bien y se cargan sin perder los ítems del inventario.  
- Los héroes suben de nivel correctamente aunque ganen mucha experiencia de golpe.  
- Los ítems aplican los efectos de curación o mejora correctamente.  
- Las mazmorras ahora muestran a los jefes en el momento correcto y ya no hay errores que cortaban la partida.  
- En los combates, mostrar y usar los ítems funciona aunque estén guardados como listas de objetos o diccionarios.  

---

### Qué probamos

- Abrir el juego, crear héroes y entrar en mazmorras.  
- Usar ítems, atacar enemigos y derrotar jefes.  
- Guardar y cargar partidas varias veces.  
- Revisamos que no aparezcan errores de código.  

---

### Cosas que todavía podrían mejorar

- A veces el inventario mezcla objetos y diccionarios, podría unificarse para que sea más simple.  
- Si estás en medio de una batalla y cargas la partida, el juego no recuerda exactamente en qué turno estabas.  
- Falta que algunos inputs sean validados para evitar errores por parte del jugador.  

---

### Próximos pasos

- Usar siempre objetos para los ítems y que se guarden bien.  
- Mejorar el guardado para que se pueda retomar una batalla exactamente donde la dejaste.  
- Agregar pruebas automáticas para asegurarnos de que todo funcione correctamente.  
- Separar la parte del menú de la lógica del juego para que sea más fácil de mantener.  

