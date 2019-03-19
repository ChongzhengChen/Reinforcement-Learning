"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
"""
from rl_glue import BaseAgent
import numpy as np
from importlib import import_module


class Agent1(BaseAgent):
    """
    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """
    
    def __init__(self):
        """Declare agent variables."""
        self.current_state = None
        self.weight = None
        self.last_state = None
        self.alpha = 0.5
        self.gamma = 1.0
        self.x = None

    def agent_init(self):
        self.weight = np.zeros(1000)
        self.x = np.identity(1000)
        self.last_state = 0

    def agent_start(self, state):
        self.action = np.random.binomial(1,0.5)
        self.last_state = state[0]
        return self.action

    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        """
        self.current_state = state[0]
        #update weight
        self.weight = self.weight + self.alpha*(reward + self.gamma*self.weight[self.current_state -1]-self.weight[self.last_state - 1])*self.x[self.last_state-1]
        self.action = np.random.binomial(1,0.5)
        self.last_state = self.current_state
        return self.action


    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        self.weight = self.weight + self.alpha*(reward + self.gamma*self.weight[self.current_state -1]-self.weight[self.last_state - 1])*self.x[self.last_state-1]
        return None


    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'ValueFunction':
            return self.weight
        else:
            return "I dont know how to respond to this message!!"

