from rl_glue import BaseEnvironment
import numpy as np

class Environment1D(BaseEnvironment):
    """
    Example 1-Dimensional environment
    """

    def __init__(self):
        """Declare environment variables."""
        self.state = None

    def env_init(self):
        """
        Initialize environment variables.
        """
        #set up the bandit with 10 numbers from gaussian 
        self.bandit = np.random.normal(0,1,10)
        #set the optimal action to the greatest value among the 10 numbers
        self.optimal = np.argmax(self.bandit)
        

    def env_start(self):
        """
        The first method called when the experiment starts, called before the
        agent starts.

        Returns:
            The first state observation from the environment.
        """
        return None

    def env_step(self, action):
        """
        A step taken by the environment.

        Args:
            action: The action taken by the agent

        Returns:
            (float, state, Boolean): a tuple of the reward, state observation,
                and boolean indicating if it's terminal.
        """
        #Define the reward variable and return it
        reward = np.random.normal(self.bandit[action], 1)
        return reward, self.state, False

    def env_message(self):
        return self.optimal
        

