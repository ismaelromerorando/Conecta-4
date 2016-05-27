# Conecta-4

Heuristicas

La heuristica de dificultad facil devolvera siempre 0 a no ser que se encuentre un estado final devolviendo infinito o -infinito segun sea el ganador.

La heuristica de dificultad media devolvera un numero al azar entre -100 y 100.

La heuristica de dificultad dificil analizara los posibles movimientos legales uno a uno. Recorrera el tablero a raiz de la posicion del movimiento legal analizado actualmente, contando las fichas propias y los huecos. Sumaran a la heuristica 1 y 0,5 respectivamente. Los movimientos a contemplar seran en columna, filas y diagonales. Una vez calculada la heuristica de la maquina se realizara el mismo proceso con la del jugador. Finalmente se restara al valor de la maquina el correspondiente al jugador obteniendo el valor definitivo de la heuristica.

Run

Se permite seleccionar quien empiez y la dificultad, ademas de no dejar empezar el juego hasta que no se establezcan esos dos parametros.
