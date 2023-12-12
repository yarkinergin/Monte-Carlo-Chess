import Agent
from Node import Node
            
# Monte Carlo
agentWhite = Agent.Agent("w")
print("------------------")

total = 0
num = 0
for x in range(5):
    total += agentWhite.playHuman(100)
    num += 1
    print(str(total) + " / " + str(num))