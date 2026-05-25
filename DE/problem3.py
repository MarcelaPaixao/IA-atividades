import numpy as np

def fitness(individuo):
    individuo = np.array(individuo)
    n = len(individuo)
    somat1 = np.sqrt((1/n) * np.sum(individuo ** 2))
    somat2 = (1/n) * np.sum(np.cos(2 * np.pi * individuo))
    return -20 * np.exp(-0.2 * somat1) - np.exp(somat2) + 20 + np.e

# N deve ser maior ou igual a quatro para garantir o funcionamento do algoritmo!
def DE(low, high, N, D, G, F, Cr):
    pop_p = np.random.uniform(low=low, high=high, size=(N, D))
    
    for g in range(G):

        for i in range(len(pop_p)):
            idx_permitidos = [idx for idx in range(len(pop_p)) if idx != i]
            r1, r2, r3 = np.random.choice(idx_permitidos, size=3, replace=False)
            r2, r3 = np.random.choice(idx_permitidos, size=2, replace=False)

            I_r1 = pop_p[r1]           
            I_r2 = pop_p[r2]
            I_r3 = pop_p[r3]

            I = pop_p[i]
            V = I_r1 + F * (I_r2 - I_r3)
            V = np.clip(V, low, high)

            U = np.array([])
            gene_obrigatorio = np.random.randint(len(I))
            for gene in range(len(I)):
                if np.random.rand() <= Cr or gene == gene_obrigatorio: U = np.append(U, [V[gene]])
                else: U = np.append(U, [I[gene]])
            
            if fitness(U) < fitness(I): pop_p[i] = U
    
        print(fitness(min(pop_p, key=fitness)), g)
    
    melhor = min(pop_p, key=fitness)
    return fitness(melhor)


print(DE(low=-32, high=32, N=100, D=30, G=100, F=0.4, Cr=0.9))