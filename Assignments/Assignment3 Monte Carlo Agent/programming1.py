
import numpy as np
import matplotlib.pyplot as plt
#probility of Headup
pHead = 0.55
delta = 0
theta = 0.00000001
stateValue = np.zeros(101)
#set the optimal policy 
Policy = np.zeros(101)
Reward = np.zeros(101)
#the winning state which means the reward is 1
Reward[100] = 1.0
sweep = 0
forever = True

##Value iteration algorithm from textbook

while forever:
    delta = 0.0
    for state in range(1, 100):
        v = stateValue[state]
        result = []
        #money that can be used to make a bet(0 --  whatever you have left)
        for action in range(1, min(state, 100 - state) + 1):
            win = state + action
            lose =  state - action
            #append the balance to the result list
            result.append(pHead * (Reward[win] + stateValue[win]) + (1 - pHead) * (Reward[lose] + stateValue[lose]))
        stateValue[state] = np.max(result)
        Policy[state] = np.argmax(result)+1
        delta = max(delta, abs(v - stateValue[state]))
    #plot the first three sweep in figure 1
    sweep += 1
    if sweep == 1 or sweep == 2 or sweep == 3:
        plt.plot(stateValue)
    if delta < theta:
        stateValue[100] = None
        forever = False
print("Sweep Total:",str(sweep)) 
       






plt.figure(1)
plt.suptitle('Gambler problem+pHead'+str(pHead))
plt.xlabel('State (Capital)')
plt.ylabel('Value')
plt.plot(stateValue)
plt.figure(2)
plt.suptitle('Gambler problem+pHead'+str(pHead))
plt.xlabel('State (Capital)')
plt.ylabel('Policy')
plt.plot(Policy)
plt.show()