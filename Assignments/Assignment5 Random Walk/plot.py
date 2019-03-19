import matplotlib.pyplot as plt
import numpy as np

file1 = open('tabular_output.txt',"r")
file2 = open('tiling_output.txt',"r")

data1 = []
data2 = []

for data in file1:
    data = data.strip()
    data1.append(data)
for data in file2:
    data = data.strip()
    data2.append(data)
plt.show()
plt.plot(data1, label="tabular_agent")
plt.plot(data2, label="tile_agent")
plt.xlim([0, 2000])
plt.legend()
plt.show()