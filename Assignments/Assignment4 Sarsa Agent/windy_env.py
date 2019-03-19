"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018,
  University of Alberta.
  Windy's problem environment using RLGlue.
"""
from rl_glue import BaseEnvironment
import numpy as np


class WindyEnvironment(BaseEnvironment):
    """
    Note: inherit from BaseEnvironment to be sure that your Agent class implements
    the entire BaseEnvironment interface
    """
    def __init__(self):
        """Declare environment variables."""
        
        self.initial = [0,3]
        self.current_state = [0,0]
        self.goal = [7,3]
        self.length_x = 9
        self.length_y = 6
        self.wind = [0,0,0,1,1,1,2,2,1,0]
        self.reward = 0.0
        
    def env_init(self):
        pass
    def env_start(self):
        
        self.current_state = self.initial
        return self.current_state
    
    def env_step(self, action):
        self.update_state = [0,0]
        self.update_state[0] = self.current_state[0] + action[0]
        self.update_state[1] =  self.current_state[1] + action[1] + self.wind[self.current_state[0]]
        if self.update_state[0] > self.length_x:
            self.update_state[0] = self.length_x
        if self.update_state[1] > self.length_y:
            self.update_state[1] =  self.length_y
        if self.update_state[0] < 0:
            self.update_state[0] = 0
        if self.update_state[1] < 0:
            self.update_state[1] = 0
        
        self.current_state = self.update_state

        self.is_terminal = False
        if self.current_state[0] == self.goal[0] and self.current_state[1] == self.goal[1]:
            self.reward = 1.0
            self.is_terminal = True
        else:
            self.reward = -1.0

        return self.reward, self.current_state, self.is_terminal
    
    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass
