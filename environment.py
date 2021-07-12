# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typing.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import numpy as np
import pygame as pg


# import sound
# %matplotlib inline

class GridWorld:
    ## Initialise starting data
    def __init__(self):
        # Set information about the gridworld
        self.height = 1
        self.width = 5
        self.grid = np.zeros((self.height, self.width))

        # Set random start location for the agent
        # self.current_location = (0,  np.random.randint(0,5))
        self.current_location = (0, 0)

        # Set locations for the bomb and the gold
        self.bomb_location = (0, 0)
        self.gold_location = (0, 4)
        self.terminal_states = [self.bomb_location, self.gold_location]

        # Set grid rewards for special cells
        self.grid[self.bomb_location[0], self.bomb_location[1]] = -10
        self.grid[self.gold_location[0], self.gold_location[1]] = 10
        self.grid[0, 1] = -8
        self.grid[0, 2] = -5
        self.grid[0, 3] = 0

        # Set available actions
        self.actions = ['Click', 'Encourage', 'None']

    ## Put methods here:
    def get_available_actions(self):
        """Returns possible actions"""
        return self.actions

    def agent_on_map(self):
        """Prints out current location of the agent on the grid (used for debugging)"""
        grid = np.zeros((self.height, self.width))
        grid[self.current_location[0], self.current_location[1]] = 1
        return grid

    def get_reward(self, new_location):
        """Returns the reward for an input position"""
        return self.grid[new_location[0], new_location[1]]

    def make_step(self, action):
        """Moves the agent in the specified direction. If agent is at a border, agent stays still
        but takes negative reward. Function returns the reward for the move."""

        reward = self.get_reward(self.current_location)
        return reward

    def check_state(self):
        """Check if the agent is in a terminal state (gold or bomb), if so return 'TERMINAL'"""
        if self.current_location in self.terminal_states:
            return 'TERMINAL'




