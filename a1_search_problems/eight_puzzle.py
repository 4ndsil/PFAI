'''
'''
from copy import deepcopy


class EightPuzzle:

    def __init__(self, initial_state, goal_state):
        self.state = initial_state
        self.goal = goal_state
        self.action = ['right', 'down', 'left', 'up']

    def pretty_print(self):
        print('----------------------------')
        print(' Current frontier: ')
        for i in range(len(self.state)):
            curr = []
            for j in range(len(self.state)):
                curr.append(self.state[i][j])
            print(curr)
        print('----------------------------')

    def h_1(self):  # tiles out of place
        h_value = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal[i][j]:
                    h_value += 1
        return h_value

    def h_2(self):  # manhattan distance
        distance = 0
        for i in range(3):
            for j in range(3):
                curr_node = self.state[i][j]
                goal_node = self.get_position_goal(curr_node)
                distance += abs(
                    i - goal_node[0]) + abs(j - goal_node[1])
        return distance

    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    def get_position_goal(self, value):
        for i in range(3):
            for j in range(3):
                if self.goal[i][j] == value:
                    return (i, j)

    def get_position(self, value):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == value:
                    return (i, j)

    def move(self, move):
        if move == 'right':
            dc = deepcopy(self)
            if dc.right():
                return dc
        elif move == 'down':
            dc = deepcopy(self)
            if dc.down():
                return dc
        elif move == 'left':
            dc = deepcopy(self)
            if dc.left():
                return dc
        elif move == 'up':
            dc = deepcopy(self)
            if dc.up():
                return dc

    def right(self):

        e_position = self.get_position('e')
        if self.state[e_position[0]][e_position[1]] != self.state[e_position[0]][2]:
            temp_value = self.state[e_position[0]][e_position[1]+1]
            self.state[e_position[0]][e_position[1]+1
                                      ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True

    def down(self):

        e_position = self.get_position('e')

        if self.state[e_position[0]][e_position[1]] != self.state[2][e_position[1]]:
            temp_value = self.state[e_position[0]+1][e_position[1]]
            self.state[e_position[0]+1][e_position[1]
                                        ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True

    def left(self):

        e_position = self.get_position('e')

        if self.state[e_position[0]][e_position[1]] != self.state[e_position[0]][0]:
            temp_value = self.state[e_position[0]][e_position[1]-1]
            self.state[e_position[0]][e_position[1]-1
                                      ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True

    def up(self):

        e_position = self.get_position('e')

        if self.state[e_position[0]][e_position[1]] != self.state[0][e_position[1]]:
            temp_value = self.state[e_position[0]-1][e_position[1]]
            self.state[e_position[0]-1][e_position[1]
                                        ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True
