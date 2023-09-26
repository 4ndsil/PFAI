'''
Define game and start execution of game search

Author: Tony Lindgren
'''
from four_in_a_row import FourInARow
from game_node_and_game_search import GameSearch


def ask_ai(state0):
    gs = GameSearch(state0, depth=5)
    move = gs.minimax_search(alpha=-100000, beta=100000)
    # gs = GameSearch(state0, depth=3, time=20)
    # move = gs.mcts()
    state1 = state0.result(move)
    print('--------')
    print('AI moves')
    print('--------')
    state1.pretty_print()
    stop, value = state1.is_terminal()
    if stop == True:
        if value > 0:
            print('AI won')
        else:
            print('Human won')
        return state1, True
    return state1, False


def ask_player(state0):
    moves = state0.actions()
    legal = False
    while legal == False:
        action_str = input('Available moves: ')
        action = int(action_str)
        if action in moves:
            legal = True
    state1 = state0.result(action)
    print('--------')
    print('Human moves')
    print('--------')
    state1.pretty_print()
    stop, value = state1.is_terminal()
    if stop == True:
        if value > 0:
            print('AI won')
        else:
            print('Human won')
        return state1, True
    return state1, False


def main():
    print('Welcome to play for-in-a-row!')
    answer = None
    while answer != 'y' and answer != 'n':
        answer = input('Would you like to start [y/n]: ')
    if (answer == 'y'):
        state0 = FourInARow('human', 'w')
        stop = False
        while not stop:
            # Ask player
            state1, stop1 = ask_player(state0)
            if stop1:
                break
            else:
                # AI move
                state0, stop2 = ask_ai(state1)
                if stop2:
                    break
    else:
        state0 = FourInARow('ai', 'w')
        stop = False
        while not stop:
            # AI move
            state1, stop1 = ask_ai(state0)
            if stop1:
                break
            else:
                # Ask player
                state0, stop2 = ask_player(state1)
                if stop2:
                    break


if __name__ == "__main__":
    main()
