import games
import heuristica


#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial
player = 'X'

heu= raw_input("Elija la dificultad f(facil), m(medio o d(dificil): ") #Seleccion de quien comienza, funcionamiento identico a la eleccion de dificultad.
while heu != 'F' and heu!= 'M' and heu != 'D' and heu != 'f' and heu != 'm' and heu != 'd':
    print "Comando de dificultad erroneo por favor vuelva a introducirlo"
    heu = raw_input("Elija la dificultad: ")


player = raw_input("Elija el jugador que desea comenzar X (maquina) O (humano): ") #Seleccion de quien comienza, funcionamiento identico a la eleccion de dificultad.
while player != 'X' and player!= 'O' and player != 'x' and player != 'o':
    print "Comando de jugador erroneo por favor vuelva a introducirlo"
    player = raw_input("Elija el jugador que empezara primero: ")


if player == 'x' or player == 'X': #En el caso que se elija que comience la maquina (X)
 	state.to_move = 'X' #Se indica que el primero en mover va a ser la maquina
if player == 'o' or player == 'O': #En el caso que quiera empezar el humano (O)
    state.to_move = 'O'  # Se indica que el primero en mover sera el humano

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        #move = games.alphabeta_search(state, game,4,None,0)

        if heu == 'f' or heu == 'F':
            move = games.alphabeta_search(state, game, 4, cutoff_test=None, eval_fn=heuristica.facil)
        if heu == 'm' or heu == 'M':
            move = games.alphabeta_search(state, game, 4, cutoff_test=None, eval_fn=heuristica.medio)
        if heu == 'd' or heu == 'D':
            move = games.alphabeta_search(state, game, 4, cutoff_test=None, eval_fn=heuristica.dificil)
        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
