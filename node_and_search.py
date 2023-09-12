'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
import time
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Node:
    '''
    This class defines nodes in search trees. It keeps track of: 
    state, cost, parent, action, and depth 
    '''

    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def goal_state(self):
        return self.state.check_goal()

    def successor(self):
        successors = queue.Queue()
        for action in self.state.action:
            child = self.state.move(action)
            if child != None:
                childNode = Node(child, self.cost + 1, self, action)
                successors.put(childNode)
        return successors

    def pretty_print_solution(self, verbose=False):
        if self.parent:
            self.parent.pretty_print_solution(verbose)
            if verbose:
                self.state.pretty_print()
            print("action:", self.action)
        else:
            if verbose:
                self.state.pretty_print()
            print("action:", self.action)


class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''

    def __init__(self, problem):
        self.start = Node(problem)
        self.goal_depth = 0
        self.search_cost = 0
        self.solution_cost = 0
        self.cpu_time = 0

    def bfs(self, verbose=False, statistics=False):
        start_time = time.process_time()
        frontier = queue.Queue()
        visited_states = [self.start.state.state]
        frontier.put(self.start)
        self.search_cost += 1
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node.goal_state():
                stop = True
                curr_node.pretty_print_solution(verbose)
                if statistics:
                    self.goal_depth = curr_node.depth
                    self.solution_cost = curr_node.cost  # fråga på handledning
                    self.cpu_time = time.process_time() - start_time
                    self.statistics()
                return curr_node
            successors = curr_node.successor()
            while not successors.empty():
                succ = successors.get()
                # if succ.state.state not in visited_states:
                self.search_cost += 1
                succ.visited = True
                frontier.put(succ)

    def dfs(self, depth_limit=None, verbose=False, statistics=False):
        self.search_cost = 0
        start_time = time.process_time()
        frontier = []
        frontier.append(self.start)
        visited_states = [self.start.state.state]
        self.search_cost += 1
        stop = False
        while not stop:
            if len(frontier) == 0:
                return None
            curr_node = frontier.pop()
            if curr_node.goal_state():
                stop = True
                curr_node.pretty_print_solution(verbose)
                if statistics:
                    self.goal_depth = curr_node.depth
                    self.solution_cost = curr_node.depth  # fråga på handledning
                    self.cpu_time = time.process_time() - start_time
                    self.statistics()
                return curr_node
            successors = curr_node.successor()
            while not successors.empty():
                succ = successors.get()
                if (depth_limit == None or depth_limit >= curr_node.depth) and succ.state.state not in visited_states:
                    self.search_cost += 1
                    frontier.append(succ)
                    visited_states.append(succ.state.state)

    def ids(self, statistics=False, cutoff=None):
        start_time = time.process_time()
        depth_limit = 0
        while depth_limit >= 0:
            dfs_output = self.dfs(depth_limit, False, False)
            if dfs_output != None or depth_limit == cutoff:
                end_time = time.process_time()
                if statistics:
                    self.goal_depth = dfs_output.depth
                    self.solution_cost = dfs_output.depth  # fråga på handledning
                    self.cpu_time = end_time - start_time
                    self.statistics()
                return dfs_output
            depth_limit += 1

    def greedy_search(self, heuristic=0, verbose=False, statistics=False):
        self.search_cost = 0
        start_time = time.process_time()
        frontier = queue.PriorityQueue()
        h = self.start.state.h_1() if heuristic == 0 else self.start.state.h_2()
        frontier.put(PrioritizedItem(h, self.start))
        visited_states = [self.start.state.state]
        self.search_cost += 1
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node.item.goal_state():
                stop = True
                curr_node.item.pretty_print_solution(verbose)
                if statistics:
                    self.goal_depth = curr_node.item.depth
                    self.solution_cost = curr_node.item.depth  # fråga på handledning
                    self.cpu_time = time.process_time() - start_time
                    self.statistics()
                return curr_node.item
            successors = curr_node.item.successor()
            while not successors.empty():
                succ = successors.get()
                if succ.state.state not in visited_states:
                    self.search_cost += 1
                    visited_states.append(succ.state.state)
                    h = succ.state.h_1() if heuristic == 0 else succ.state.h_2()
                    frontier.put(PrioritizedItem(h, succ))

    def a_star(self, heuristic=0, verbose=False, statistics=False):
        self.search_cost = 0
        self.start.depth = 0
        start_time = time.process_time()
        frontier = queue.PriorityQueue()
        h = self.start.state.h_1() if heuristic == 0 else self.start.state.h_2()
        start_cost = self.start.cost + h
        frontier.put(PrioritizedItem(start_cost, self.start))
        visited_states = [self.start.state.state]
        self.search_cost += 1
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node.item.goal_state():
                stop = True
                curr_node.item.pretty_print_solution(verbose)
                if statistics:
                    self.goal_depth = curr_node.item.depth
                    self.solution_cost = curr_node.item.depth  # fråga på handledning
                    self.cpu_time = time.process_time() - start_time
                    self.statistics()
                return curr_node.item
            successors = curr_node.item.successor()
            while not successors.empty():
                succ = successors.get()
                if succ.state.state not in visited_states:
                    self.search_cost += 1
                    visited_states.append(succ.state.state)
                    h = succ.state.h_1() if heuristic == 0 else succ.state.h_2()
                    estimated_cost = succ.cost + h
                    print(succ.cost)
                    frontier.put(PrioritizedItem(estimated_cost, succ))

    def statistics(self):
        branching = self.search_cost ** (1 / self.goal_depth)
        print("depth: ", self.goal_depth)
        print("search cost: ", self.search_cost)
        print("solution cost: ", self.solution_cost)
        print("cpu time: ", self.cpu_time)
        print("effective branching factor: ", branching)
