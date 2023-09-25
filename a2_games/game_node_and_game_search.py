'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren
'''
from time import process_time
import random
import math


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''

    def __init__(self, state, node=None):
        self.state = state
        self.successors = []
        self.parent
        self.wins = 0
        self.move
        self.actions_left = state.actions()
        self.playouts

    def ucb1(self, c):  # c is preferably math.sqrt(2)
        return (self.wins/self.playouts) + (c * math.sqrt(math.log(self.parent)/self.playouts))


class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''

    def __init__(self, game, depth=3):
        self.state = game
        self.depth = depth

    def mcts(self):
        start_time = process_time()
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()
        elapsed_time = 0
        while elapsed_time < self.time:
            leaf = self.select(tree)
            child = self.expand(leaf)
            result = self.simulate(child)
            self.back_propagate(result, child)
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move

    def select(self, node):
        if node.actions_left:
            return node
        max_ucb1 = 0
        for succ in node.successors:
            curr_ucb1 = succ.ucb1()
            if curr_ucb1 > max_ucb1:
                max_ucb1 = curr_ucb1
                break
        return self.select(self, succ)

    def expand(self, node):
        if not node.action_left:
            return node

    def minimax_search(self, alpha=None, beta=None, time_limit=None):
        start = process_time()
        stop = start + time_limit
        _, move = self.max_value(
            self.state, self.depth, alpha, beta, start, stop)
        return move

    def max_value(self, state, depth, alpha=None, beta=None, start=None, stop=None):
        move = None
        terminal, value = state.is_terminal()
        if terminal:
            return state.eval(), None
        if start != None and start >= stop:
            print('stop')
            return state.eval(), None
        if depth == 0:
            return state.eval(), None
        v = -100000
        actions = state.actions()
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1, alpha, beta)
            if v2 > v:
                v = v2
                move = action
            if beta != None and alpha != None:
                alpha = max(alpha, v)
                if v >= beta:
                    return v, move
        return v, move

    def min_value(self, state, depth, alpha=None, beta=None, start=None, stop=None):
        move = None
        terminal, value = state.is_terminal()
        if terminal:
            return state.eval(), None
        if start != None and start >= stop:
            return state.eval(), None
        if depth == 0:
            return state.eval(), None
        v = 100000
        actions = state.actions()
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1, alpha, beta)
            if v2 < v:
                v = v2
                move = action
            if beta != None and alpha != None:
                beta = min(beta, v)
                if v <= alpha:
                    return v, move
        return v, move
