import numpy as np
from rl_glue import BaseAgent


class RandomAgent(BaseAgent): 

    def __init__(self):
        """Declare agent variables."""

        self.action = None
        
    def agent_init(self):
        """Initialize agent variables."""
        
        self.arms = np.zeros(10) + 0 #initialize 10 arms all starts with value 0
        self.alpha = 0.1
        self.epsilon = 0.1

    def agent_start(self, state):
        
        self.action = self._choose_action()
        
        return self.action

    def _choose_action(self):
        """
        Convenience function.

        You are free to define whatever internal convenience functions
        you want, you just need to make sure that the RLGlue interface
        functions are also defined as well.
        """
        if np.random.uniform(0, 1) < self.epsilon:
            self.action = np.random.randint(0,10)
            
        else:
            self.action = np.argmax(self.arms)
        
        return self.action

    def agent_step(self, reward, state):
        """
        A step taken by the agent.
        Args:
            reward (float): the reward received for taking the last action taken
            state (state observation): The agent's current state
        Returns:
            The action the agent is taking.
        """
        #Formula for updating the reward
        self.arms[self.action] = self.arms[self.action]+ self.alpha * (reward - self.arms[self.action])
        # Agent still just chooses an action randomly
        self.action = self._choose_action()

        return self.action

    def agent_end(self, reward):
        """
        Run when the agent terminates.
        Args:
            reward (float): the reward the agent received for entering the
                terminal state.
        """

        # random agent doesn't care about reward
        pass

    def agent_message(self, message):
        # if 'prob0' in message:
        #     self.prob0 = float(message.split()[1])
        pass
