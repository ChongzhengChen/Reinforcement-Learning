"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018, University of Alberta.
  Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlo agent using RLGlue.
"""
from rl_glue import RLGlue
from windy_env import WindyEnvironment
from sarsa_agent import SarsaAgent
import numpy as np
import matplotlib.pyplot as plt


max_steps = 8000
steps = 0
episodes = 0

ep_list = []
step_list = []

environment = WindyEnvironment()
agent       = SarsaAgent()
rl          = RLGlue(environment,agent) 
rl.rl_init()
while steps < max_steps:
  rl.rl_episode(max_steps)
  steps = rl.num_steps()
  episodes = rl.num_episodes()
  # print(steps, episodes)

  ep_list.append(episodes)
  step_list.append(steps)


plt.xlabel('Time steps')
plt.ylabel('Episodes')
plt.plot(step_list, ep_list)
plt.show()

    

    

          

        
          

