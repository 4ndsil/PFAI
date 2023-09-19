'''
Missionaries and Cannibal problem

Author: Tony Lindgren
'''
from copy import deepcopy


class MissionariesAndCannibals:

    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.goal = goal
        self.action = ['mm', 'mc', 'cc', 'm', 'c']

    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    def move(self, move):
        if move == 'mm':
            dc = deepcopy(self)
            if dc.mm():
                return dc
        elif move == 'mc':
            dc = deepcopy(self)
            if dc.mc():
                return dc
        elif move == 'cc':
            dc = deepcopy(self)
            if dc.cc():
                return dc
        elif move == 'm':
            dc = deepcopy(self)
            if dc.m():
                return dc
        elif move == 'c':
            dc = deepcopy(self)
            if dc.c():
                return dc

    def mm(self):
        left_bank = self.state[0]
        boat = self.state[1]
        right_bank = self.state[2]
        if boat == 'r':
            if (right_bank[0] - 2 == 0 or right_bank[0] - 2 >= right_bank[1]) and right_bank[0] >= 2 and left_bank[0] + 2 >= left_bank[1]:
                right_bank[0] = right_bank[0] - 2
                boat = 'l'
                left_bank[0] = left_bank[0] + 2
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True
        else:
            if (left_bank[0] - 2 == 0 or left_bank[0] - 2 >= left_bank[1]) and left_bank[0] >= 2 and right_bank[0] + 2 >= right_bank[1]:
                left_bank[0] = left_bank[0] - 2
                boat = 'r'
                right_bank[0] = right_bank[0] + 2
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True

    def cc(self):
        left_bank = self.state[0]
        boat = self.state[1]
        right_bank = self.state[2]
        if boat == 'r':
            if (left_bank[0] == 0 or left_bank[0] >= left_bank[1] + 2) and right_bank[1] >= 2:
                right_bank[1] = right_bank[1] - 2
                boat = 'l'
                left_bank[1] = left_bank[1] + 2
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True
        else:
            if (right_bank[0] == 0 or right_bank[0] >= right_bank[1] + 2) and left_bank[1] >= 2:
                left_bank[1] = left_bank[1] - 2
                boat = 'r'
                right_bank[1] = right_bank[1] + 2
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True

    def m(self):
        left_bank = self.state[0]
        boat = self.state[1]
        right_bank = self.state[2]
        if boat == 'r':
            if (right_bank[0] - 1 == 0 or right_bank[0] - 1 >= right_bank[1]) and right_bank[0] >= 1 and left_bank[0] + 1 >= left_bank[1]:
                right_bank[0] = right_bank[0] - 1
                boat = 'l'
                left_bank[0] = left_bank[0] + 1
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True
        else:
            if (left_bank[0] - 1 == 0 or left_bank[0] - 1 >= left_bank[1]) and left_bank[0] >= 1 and right_bank[0] + 1 >= right_bank[1]:
                left_bank[0] = left_bank[0] - 1
                boat = 'r'
                right_bank[0] = right_bank[0] + 1
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True

    def c(self):
        left_bank = self.state[0]
        boat = self.state[1]
        right_bank = self.state[2]
        if boat == 'r':
            if (left_bank[0] == 0 or left_bank[0] >= left_bank[1] + 1) and right_bank[1] >= 1:
                right_bank[1] = right_bank[1] - 1
                boat = 'l'
                left_bank[1] = left_bank[1] + 1
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True
        else:
            if (right_bank[0] == 0 or right_bank[0] >= right_bank[1] + 1) and left_bank[1] >= 1:
                left_bank[1] = left_bank[1] - 1
                boat = 'r'
                right_bank[1] = right_bank[1] + 1
                # update our state
                self.state = [left_bank, boat, right_bank]
                return True

    def mc(self):
        left_bank = self.state[0]
        boat = self.state[1]
        right_bank = self.state[2]
        if boat == 'r':
            if (right_bank[0] - 1 == 0 or right_bank[0] - 1 >= right_bank[1] - 1) and right_bank[0] >= 1 and right_bank[1] >= 1 and left_bank[0] + 1 >= left_bank[1] + 1:
                right_bank[0] = right_bank[1] - 1
                right_bank[1] = right_bank[1] - 1
                boat = 'l'
                left_bank[0] = left_bank[0] + 1
                left_bank[1] = left_bank[1] + 1
                self.state = [left_bank, boat, right_bank]
                return True
        else:
            if (left_bank[0] - 1 == 0 or left_bank[0] - 1 >= left_bank[1] - 1) and left_bank[0] >= 1 and left_bank[1] >= 1 and right_bank[0] + 1 >= right_bank[1] + 1:
                right_bank[0] = right_bank[1] + 1
                right_bank[1] = right_bank[1] + 1
                boat = 'r'
                left_bank[0] = left_bank[0] - 1
                left_bank[1] = left_bank[1] - 1
                self.state = [left_bank, boat, right_bank]
                return True

    def pretty_print(self):
        print('----------------------------')
        print(' #miss on left bank: ', self.state[0][0])
        print(' #cann on left bank: ', self.state[0][1])
        print('            boat is: ', self.state[1])
        print('#miss on right bank: ', self.state[2][0])
        print('#cann on right bank: ', self.state[2][1])
        print('----------------------------')
