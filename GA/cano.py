import numpy as np

def fitness(ind):
    custo = 0
    penalidade = 0
    vazao = 0

    for i in range(gene):
        custo += Comp[i] * Custo[ind[i]]
        vazao += Q[i]

        d = D[ind[i]]/1000
        q_max = (np.pi * d**2) * (d/4)**(2/3) * np.sqrt(0.005) / 0.013

    #conenferir isso aqui
    if vazao/1000 > 0.75*q_max:
        penalidade = 10000
        
    return custo + penalidade


def selecao(pop):
    pop_i = []
    for i in range(N):
        inds = np.random.choices(pop, k=2)
        melhor = min(inds, key=fitness)
        pop_i.append(melhor)

    return pop_i

def crossover(pop):
    tx_crossover = 0.7
    pop_i = []

    for i in range(N/2):
        inds = np.random.choice(pop, size=2)
        taxa = np.random.normal()

        if taxa <= tx_crossover:
            ...
        else:
            pop_i.append(inds[0], inds[1])

    return pop_i

N = 100
gene = 10
tx_mutacao = 0.1

Comp = [20, 54, 98, 120, 34, 12, 88, 122, 33, 40]
Q = [2.5 * (i+1) for i in range(gene)]

Custo = [65, 98, 150, 210, 340]
D = [150, 200, 250, 300, 400]

populacao = np.random.randint(low=0, high=4, size=(N, gene)) # pop_p


https://docs.google.com/document/d/1-G-5WAKvZt1btJ1s073yOGV5yhgb_819b8Wjjpfr0U8/edit?usp=sharing