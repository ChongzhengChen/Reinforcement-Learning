#!/usr/bin/env python

import numpy as np
from rl_glue import RLGlue
from env_hw6 import Environment
from agent_hw6 import Agent

def part3():
    # Specify hyper-parameters

    agent = Agent()
    environment = Environment()
    rlglue = RLGlue(environment, agent)

    num_episodes = 200
    num_runs = 1
    max_eps_steps = 100000

    steps = np.zeros([num_runs, num_episodes])

    for r in range(num_runs):
        print("run number : ", r)
        rlglue.rl_init()
        for e in range(num_episodes):
            rlglue.rl_episode(max_eps_steps)
            steps[r, e] = rlglue.num_ep_steps()
            # print(steps[r, e])
    np.save('steps', steps)
    fout = open('value','w')
    steps = 50
    num_of_actions = 3
    for i in range(steps):
        for j in range(steps):
            q = []
            for a in range(num_of_actions):
                pos = -1.2 + (1*1.7/steps)
                vel =  -0.07 + (j*0.14/steps)
                tile = (pos,vel)
                inds = Agent.F(tile,self.action)
                q.append(np.sum(self.weights[inds]))
            height = max(q)
            fout.write(repr(-height) + '')
        fout.write('\n')
    fout.close()
    np.save('heights',height)
    np.save('steps', steps)

if __name__ == "__main__":
    part3()
    print("Done")
