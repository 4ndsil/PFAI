'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals
from eight_puzzle import EightPuzzle
from node_and_search import SearchAlgorithm

init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]

init_state_2 = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
goal_state_2 = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]


def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)

    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.bfs(verbose=False, statistics=True)
    print('goal state: ')
    goal_node.state.pretty_print()
    goal_node.pretty_print_solution()
    sa.statistics()

    '''
    print('DFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.dfs(verbose=True, statistics=True)
    print('goal state: ')
    goal_node.state.pretty_print()
    '''

    '''
    print('IDS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.ids(statistics=True, cutoff=11)
    print('goal state: ')
    goal_node.state.pretty_print()
    '''
    '''
    ep = EightPuzzle(init_state_2, goal_state_2)
    sa_2 = SearchAlgorithm(ep)
    
    print('Greedy search')
    print('starting search')
    ep.pretty_print()
    goal_node = sa_2.greedy_search(heuristic=1, verbose=True, statistics=True)
    '''
    '''
    print('A* search')
    print('starting search')
    ep.pretty_print()
    goal_node = sa_2.a_star(heuristic=1, verbose=True, statistics=True)
    '''
    '''
    # uninformed search for eight puzzle
    print('BFS')
    goal_node = sa_2.bfs(statistics=True)
    goal_node.pretty_print_solution()
    print('DFS')
    goal_node = sa_2.dfs(statistics=True)
    goal_node.pretty_print_solution()
    print('IDS')
    goal_node = sa_2.ids(statistics=True)
    goal_node.pretty_print_solution()
    '''


if __name__ == "__main__":
    main()
