"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
"""
from rl_glue import BaseAgent
import numpy as np
from importlib import import_module

class Agent2(BaseAgent):
    """
    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """
    
    def __init__(self):
        """Declare agent variables."""
        self.current_state = None
        self.weight = None
        self.last_state = None
        self.alpha = 0.01/50
        self.gamma = 1.0
        #meaning of x
        self.x = None
        self.tiling = 50
        self.tile = import_module("tiles3")
        self.iht = self.tile.IHT(3000)

    def agent_init(self):
        self.current_state = None
        self.last_state = None
        self.weight = np.zeros(1001)

    def agent_start(self, state):
        self.current_state = np.zeros(1)
        self.last_state = self.current_state
        self.action = np.random.binomial(1, 0.5)
          
        return self.action

    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        """
        state1 = np.zeros(1200)
        state2 = np.zeros(1200)
        self.current_state[0] = float(state[0]/200.0)
        self.current_x = self.tile.tiles(self.iht,50,self.current_state)
        self.last_x = self.tile.tiles(self.iht,50,self.last_state)
        for i in self.current_x:
            state1[i] = 1
        for j in self.last_x:
            state2[j] = 1
        self.weight = self.weight + self.alpha*(reward + self.gamma*np.dot(self.weight,state1)-np.dot(self.weight,state2))*state2
        self.last_state = self.current_state
        return self.action

    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        state2 = np.zeros(1200)
        self.last_x =  self.tile.tiles(self.iht,50,self.last_state)
        for i in self.last_x:
            state2[i] = 1
        self.weight = self.weight + self.alpha*(reward-np.dot(self.weight,state2))*state2
        


    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'ValueFunction':
            output = np.zeros(1001)
            for i in range(1001):
                self.x = self.tile.tiles(self.iht,50,[float(i/200.0)])
                state = np.zeros(1200)
                for i in self.x:
                    state[i] = 1
                    output[i] = np.dot(self.weight,state)
                return output
        else:
            return "I dont know how to respond to this message!!"
        

