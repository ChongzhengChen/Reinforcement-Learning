"""Example experiment for CMPUT 366 Fall 2019

This experiment uses the rl_episode() function.

Runs a random agent in a 1D environment. Runs 10 (num_runs) iterations of
100 episodes, and reports the total reward. Each episode is capped at 100 steps.
(max_steps)
"""
import numpy as np
import matplotlib.pyplot as plt

from bandit_env import Environment1D
from bandit_agent import RandomAgent
from rl_glue import RLGlue

def experiment1():
    agent = RandomAgent()
    environment = Environment1D()
    rlg = RLGlue(environment, agent)

    max_steps = 1000  # max number of steps in an episode
    num_runs = 2000  # number of repetitions of the experiment
    optimal_action = np.zeros(max_steps)

    for k in range(num_runs):

        # initialize RL-Glue
        rlg.rl_init() #env_init + agent_init
        rlg.rl_start() 
        for i in range(max_steps): #step
            action = rlg.rl_step()[2] 
            if action == environment.env_message():
                optimal_action[i] += 1
    ratio_optimal_action = optimal_action / num_runs

    return ratio_optimal_action


def main():
    # Create and pass agent and environment objects to RLGlue
    result = experiment1()
    # run the experiment
    plt.plot(result)
    plt.xlabel('steps')
    plt.ylabel('% optimal action')
    plt.legend()
    plt.show()
    


if __name__ == '__main__':
    main()
