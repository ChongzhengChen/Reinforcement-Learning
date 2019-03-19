"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
"""
from rl_glue import BaseAgent
import numpy as np


class SarsaAgent(BaseAgent):
    """
    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """
    
    def __init__(self):
        """Declare agent variables."""
        self.epsilon = 0.1
        self.alpha   = 0.5
        self.gamma   = 1.0
        self.Q       = None
        self.last_state = None
        self.last_action = None
        self.max_action = 8
        self.choose_action = [
            [1,0],   #right
            [-1,0],  #left
            [0,1],   #up
            [0,-1],  #down
            [1,1],   #up+right
            [1,-1],  #down+right
            [-1,1],  #up+left
            [-1,-1], #down+left
            # [0,0]   #origin
        ]
        
    def agent_init(self):
        self.Q = np.zeros((9+1,6+1,self.max_action))
    def agent_start(self, state):
        if np.random.uniform() < self.epsilon:
            action = self.choose_action[np.random.randint(self.max_action)]
        else:
            action = self.choose_action[np.argmax(self.Q[state[0]][state[1]])]
        self.last_action = action
        self.last_state  = state
        return action
    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        """
        if np.random.uniform() < self.epsilon:
            action = self.choose_action[np.random.randint(self.max_action)]
        else:
            action = self.choose_action[np.argmax(self.Q[state[0]][state[1]])]
        #self.index = self.choose_action.index(self.action)
        self.Q[self.last_state[0],self.last_state[1],self.action_index(self.last_action)] += self.alpha* (reward + self.gamma * self.Q[(state[0]),(state[1]),self.action_index(action)]-self.Q[self.last_state[0],self.last_state[1], self.action_index(self.last_action)])
        self.last_action = action
        self.last_state  = state

        return action
    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        return None

    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'ValueFunction':
            return (np.max(self.Q, axis=1)).tostring()
        else:
            return "I dont know how to respond to this message!!"
    def action_index(self,action):
        return self.choose_action.index(action)
        
