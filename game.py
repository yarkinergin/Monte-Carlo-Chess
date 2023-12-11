import fen_setup
import board
import ai
import pieces
import copy
import random
import Agent
from Node import Node

# Start setup is 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

            
# Monte Carlo
agentWhite = Agent.Agent("w")
print("------------------")
agentWhite.playHuman(100)