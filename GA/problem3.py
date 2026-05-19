import numpy as np

def fitness(individuo):
    n = 30
    somat1 = 1/n * np.sum(individuo ** 2)
    somat2 = 1/n * np.sum(np.cos(2 * np.pi * individuo))
    result = -20 ** np.exp(-0.2 * np.sqrt(somat1)) - np.exp(somat2) + 20 + np.e

    penalidade = 0
    if min(result) < -32 or max(result) > 32: penalidade = 10000
    
    return result + penalidade