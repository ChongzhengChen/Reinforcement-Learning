"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018,
  University of Alberta.
  Gambler's problem environment using RLGlue.
"""
from rl_glue import BaseEnvironment
import numpy as np


class GamblerEnvironment(BaseEnvironment):
    """
    Slightly modified Gambler environment -- Example 4.3 from
    RL book (2nd edition)

    Note: inherit from BaseEnvironment to be sure that your Agent class implements
    the entire BaseEnvironment interface
    """
    num_of_states = 99
    def __init__(self):
        """Declare environment variables."""
        
        self.num_of_states = 99
    def env_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize environment variables necessary for run.
        """
        self.phead = 0.55
        self.current_state = None
        terminal_state = False
    def env_start(self):
        """
        Arguments: Nothing
        Returns: state - numpy array
        Hint: Sample the starting state necessary for exploring starts and return.
        """
        self.current_state = np.zeros(1) + np.random.randint(self.num_of_states) + 1  
        return self.current_state
    def env_step(self, action):
        """
        Arguments: action - integer
        Returns: reward - float, state - numpy array - terminal - boolean
        Hint: Take a step in the environment based on dynamics; also checking for action validity in
        state may help handle any rogue agents.
        """
        terminal_state = False
        if action > min(self.current_state[0],(100-self.current_state[0])+1):
            exit() 
        random_prob = np.random.normal(0,1)
        if random_prob > self.phead:
            self.current_state == self.current_state + action
        else:
            self.current_state == self.current_state - action
         
        reward = 0.0
        if self.current_state[0] == 100:
            terminal_state = True
            self.current_state =  None
            reward = 1.0
        elif self.current_state[0] == 0:
            terminal_state = True
            self.current_state = None
        return reward,terminal_state,self.current_state
    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass
