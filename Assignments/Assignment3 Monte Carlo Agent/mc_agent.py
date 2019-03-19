"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
   Monte Carlo agent using RLGlue - barebones.
"""
from rl_glue import BaseAgent
import numpy as np


class MonteCarloAgent(BaseAgent):
    """
    Monte Carlo agent -- Section 5.3 from RL book (2nd edition)

    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """
    
    def __init__(self):
        """Declare agent variables."""
        self.policy = None
        self.Q = None
        self.num_visits = None
        self.return_reward = None
        self.episode = None
    def agent_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize the variables that need to be reset before each run
        begins
        """
        self.Q = np.zeros((100, 100))
        self.policy = np.zeros(100)
        for s in range(100):
            self.policy[s] = min(s, 100-s)
        self.num_visits = np.zeros((100, 100))
        self.return_reward = np.zeros((100, 100))
    def agent_start(self, state):
        """
        Arguments: state - numpy array
        Returns: action - integer
        Hint: Initialize the variables that you want to reset before starting
        a new episode, pick the first action, don't forget about exploring
        starts
        """
        action = np.random.random_integers(1,min(state[0],100 - state[0]))
        self.episode = []
        return action
    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        Hint: select an action based on pi
        """
        action = int(self.policy[int(state[0])])
        self.num_visits[int(state[0]),int(action)] += 1
        self.episode.append[int(state[0]),int(action)]
        return action
    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        # sa means state and action we seperate it from episode
        for sa in self.episode:
            s = sa[0]
            a = sa[1]
            self.return_reward[s][a] += reward
            
        for s in range(1,100):
            for a in range(1,min(s,100-s)+1):
                if self.num_visits[s][a] != 0:
                    self.Q = self.return_reward[s][a] / self.num_visits[s][a]

        for sa in self.episode:
            s = sa[0]
            for s in range(1,100):
                maximum = np.argmax(self.Q[s])
                self.policy[s] = maximum

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
