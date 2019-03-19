"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
"""
from rl_glue import BaseAgent
import numpy as np
import matplotlib.pyplot as plt
from tile3 import *
class Agent(BaseAgent):
    """
    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """
    
    def __init__(self):
        """Declare agent variables."""
        self.prev_state = None
        self.prev_tile = None
        self.weights = None 
        self.q = None
        self.prev_action = None

        self.z = np.zeros(1)
        self.num_of_tiling = 8 
        self.size_of_tiling = [8,8] 
        self.alpha = 0.1/self.num_of_tiling

        self.iht = IHT(2048)
        self.lamda = 0.9
        self.epsilon = 0.0
        self.gamma = 1.0
    def agent_init(self):
        """
        Hint: Initialize the variables that need to be reset before each run begins
        Returns: nothing
        """
        self.q = np.zeros([self.size_of_tiling[0], self.size_of_tiling[1], 3])
        self.weights = np.random.uniform(-0.001, 0.0, 2048)                         #memory size for the tile coder: 2048

    def agent_start(self, state):
        """          
        Hint: Initialize the variavbles that you want to reset before starting a new episode
        Arguments: state: numpy array
        Returns: action: integer
        """
        #take action A using epsilon_greedy policy
        self.pos = self.size_of_tiling[0] * (state[0]) / (1.7) 
        self.velocity = self.size_of_tiling[1] * (state[1]) / (0.07*2)
        self.tile = [self.pos, self.velocity]
        self.action = self.choose_action(self.tile)
        #update state,action 
        self.prev_tile = self.tile
        self.prev_state = state
        self.prev_action = self.action
        self.z = np.zeros(len(self.weights))

        return self.action

        
          
        

    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        """
        #take action A 
        self.tile = [self.pos, self.velocity]
        self.action = self.choose_action(self.tile)
        TD_error = reward
        #first loop
        for i in self.F(self.prev_tile, self.prev_action):
            TD_error -= self.weights[i]
            self.z[i] += 1.0

        self.pos = self.size_of_tiling[0] * (state[0]) / (1.7) 
        self.velocity = self.size_of_tiling[1] * (state[1]) / (0.07*2)
        self.tile = [self.pos, self.velocity]
        self.action = self.choose_action(self.tile)
        self.visited = self.z
        if reward == 1:
            self.weights += self.alpha * TD_error * self.z
        #second loop
        for i in self.F(self.tile, self.action):
            self.visited[i] = 1.0
            TD_error += self.gamma * self.weights[i]

        self.weights += self.alpha * TD_error * self.z
        self.z = self.gamma * self.lamda * self.z

        self.prev_state = state
        self.prev_action = self.action
        self.prev_tile = self.tile

        return self.action        

    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        pass
    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'ValueFunction':
            return [self.weights,self.iht]
        else:
            return "I dont know how to respond to this message!!"

    def F(self,state, action):
        #info about the tile
        return tiles(self.iht, self.num_of_tiling,state,[action])

    def choose_action(self,state):

        #epislon greedy policy on choosing actions
        #it would be exploring all the time since the random number would never be less than 0 (epislon)
        if np.random.uniform() < self.epsilon: 
            self.action = np.random.randint(0,3) # 0 for decelerate 1 for coast 2 for accelerate
        else:
            list = []
            for self.action in range(0,3):
                tile_info = self.F(state, self.action)
                list.append(np.sum(self.weights[tile_info]))
            list = np.array(list)
            arg_max = np.random.choice(np.where(list == list.max())[0])
            self.action = arg_max
        return self.action

    
            

