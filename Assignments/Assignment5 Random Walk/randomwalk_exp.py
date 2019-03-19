"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018, University of Alberta.
  Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlo agent using RLGlue.
"""
from rl_glue import RLGlue
from randomwalk_env import RandomWalkEnvironment
from agent1 import Agent1
from agent2 import Agent2
import numpy as np
import matplotlib.pyplot as plt



def tabular(real_value):
    environment = RandomWalkEnvironment()
    agent       = Agent1()
    rl          = RLGlue(environment,agent) 
    error = np.zeros(5000)
    for run in range(30):
        rl.rl_init()
        for episode in range(2000):
            rl.rl_episode(10000)
            estimate = rl.RL_agent_message("ValueFunction")
            error[episode] += np.sqrt(np.mean(np.power(real_value-estimate,2)))

        rl.RL_cleanup()
    file1 = open("tabular_output.txt","w")
    for i in range(2000):
        file1.write(format(error[i]/10))
    file1.close()
def tiling(real_value):
    environment = RandomWalkEnvironment()
    agent       = Agent2()
    rl          = RLGlue(environment,agent) 
    error = np.zeros(5000)
    for run in range(30):
        rl.rl_init()
        for episode in range(2000):
            rl.rl_episode(10000)
            estimate = rl.RL_agent_message("ValueFunction")
            error[episode] += np.sqrt(np.mean(np.power(real_value-estimate,2)))

        rl.RL_cleanup()
    file2 = open("tiling_output.txt","w")
    for i in range(2000):
        file2.write(format(error[i]/10))
    file2.close()
def compute_value_function():
    """
    Computes the value function for the 1000 state random walk as described in Sutton and Barto (2017).
    :return: The value function for states 1 to 1000. Index 0 is not used in this array (i.e. should remain 0).
    """
    state_prob = 0.5 / 100.0
    gamma = 1
    theta = 0.000001

    V = np.zeros(1001)

    delta = np.infty
    i = 0
    while delta > theta:
        i += 1
        delta = 0.0
        for s in range(1, 1001):
            v = V[s]
            value_sum = 0.0
            for transition in range(1, 101):
                right = s + transition
                right_reward = 0
                if right > 1000:
                    right_reward = 1
                    right = 0

                left = s - transition
                left_reward = 0
                if left < 1:
                    left_reward = -1
                    left = 0

                value_sum += state_prob * ((right_reward + gamma * V[right]) + (left_reward + gamma * V[left]))

            V[s] = value_sum
            delta = max(delta, np.abs(v - V[s]))

        print('true value:', i)

    return V
def main():
    np.random.seed(50)
    v_bar = compute_value_function()[1:]
    tabular(v_bar)
    tiling(v_bar)
main()




    

          

        
          

