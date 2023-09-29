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

    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.successors = []
        self.parent = parent
        self.wins = 0
        self.move = move
        self.actions_left = state.actions()
        self.playouts = 0

    def ucb1(self, c):  # c is preferably math.sqrt(2)
        return (self.wins/self.playouts) + (c * math.sqrt(math.log(self.parent.playouts)/self.playouts))


class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''

    def __init__(self, game, depth=3, time_limit=None):
        self.state = game
        self.depth = depth
        self.time = time_limit

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

    def select(self, node):    # stopping condition is if the current node has actions left,
        if node.actions_left:
            return node
        max_ucb1 = 0
        max_node = None
        for succ in node.successors:
            curr_ucb1 = succ.ucb1(math.sqrt(2))
            if curr_ucb1 > max_ucb1:
                max_ucb1 = curr_ucb1
                max_node = succ
        return self.select(max_node)

    def expand(self, node):  # remember to check if terminal node is reached
        if not node.actions_left:
            return node
        move = node.actions_left.pop()
        new_state = node.state.result(move)
        child = GameNode(new_state, node, move)
        node.successors.append(child)
        return child

    def simulate(self, node):  # remember to check if terminal node is reached
        curr_node = node
        while True:
            terminal, value = curr_node.state.is_terminal()
            if terminal:
                return value
            rand_move = random.choice(curr_node.actions_left)
            new_state = curr_node.state.result(rand_move)
            curr_node = GameNode(new_state, curr_node, rand_move)

    def back_propagate(self, result, node):
        curr_node = node
        while curr_node.parent:
            curr_node.playouts += 1
            if result == 100:
                curr_node.wins += 1
            curr_node = curr_node.parent
        curr_node.playouts += 1
        if result == 100:
            curr_node.wins += 1

    def actions(self, node):
        if not node.successors:
            return None
        best_value = 0
        best_move = None
        for move in node.state.actions():
            for succ in node.successors:
                if succ.move == move:
                    curr_value = (succ.wins/succ.playouts)
                    if curr_value > best_value:
                        best_value = curr_value
                        best_move = move
        return best_move

    def minimax_search(self, alpha=None, beta=None, time_limit=None):
        start = process_time()
        stop = None
        if time_limit != None:
            stop = start + time_limit
        _, move = self.max_value(
            self.state, self.depth, alpha, beta, start, stop)
        return move

    def max_value(self, state, depth, alpha=None, beta=None, start=None, stop=None):
        move = None
        terminal, value = state.is_terminal()
        if terminal:
            return state.eval(), None
        if stop != None and start >= stop:
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
