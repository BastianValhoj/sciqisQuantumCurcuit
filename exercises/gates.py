import numpy as np


"""Define quantum logic gates (QLG)"""
Z = np.array([[1,0],
              [0,-1]])

X = np.array([[0,1],
              [1,0]])

Y = np.array([[0, -1j],
              [1j, 0]])

H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]])

P = lambda theta: np.array([[1, 0],
                            [0, np.exp(1j*theta)]])
T = P(np.pi/4)

S = P(np.pi/2)




def applyGate(gate, state):
    # actual calculation
    res = gate @ state
    
    # computer precision might deviate from actual -- check and round
    for value in [-1/np.sqrt(2), 0, 1/np.sqrt(2), 1]:
        res[np.isclose(res, value)] = value
    return res
