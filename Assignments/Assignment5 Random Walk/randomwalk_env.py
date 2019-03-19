"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018,
  University of Alberta.
  RandomWalk's problem environment using RLGlue.
"""
from rl_glue import BaseEnvironment
import numpy as np


class RandomWalkEnvironment(BaseEnvironment):
    """
    Note: inherit from BaseEnvironment to be sure that your Agent class implements
    the entire BaseEnvironment interface
    """
    def __init__(self):
        """Declare environment variables."""
        self.current_state = None
        self.right_boundry = 1000
        self.left_boundry  = 0
        self.start_pos     = 500
        
    def env_init(self):
        self.current_state = np.zeros(1)
    def env_start(self):
        
        self.current_state[0] = self.start_pos
        return self.current_state
    
    def env_step(self, action):
        self.step_size = np.random.randint(1,101)
        #choose direction on the x_axis
        if action == 1:
            move = 1
        else:
            move = -1
        final_move = move * self.step_size
        self.current_state[0] += final_move
        if self.current_state[0] <= self.left_boundry:
            self.is_terminal = True
            self.reward = -1
        elif self.current_state[0] >= self.right_boundry:
            self.is_terminal = True
            self.reward = 1
        else:
            self.is_terminal = False
            self.reward = 0
        return self.reward, self.current_state, self.is_terminal
    
    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass
