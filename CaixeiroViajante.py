from igraph import Graph
import math
import random

dados = []

with open('lau15.txt', 'r') as dataArquivo:
    for line in dataArquivo:
        linha = line.strip().split()
        dados.append((linha[0], linha[1], int(linha[2])))

grafo = Graph.TupleList(dados, weights=True, directed=False)

numIndividuosPop = 100
criterioParada = 100 #quatro geracoes sem melhora
numIndividuosElitismo = int(0.10 * numIndividuosPop)
numIndividuosCruzamento = numIndividuosPop - numIndividuosElitismo
numIndividuosMutacao = int(0.20 * numIndividuosCruzamento)

fitnessIndividuos = [0] * numIndividuosPop
individuosPop = []

def defineIndividuosInicial():
    vertices = grafo.vs.indices

    while len(individuosPop) < numIndividuosPop:
        individuo = random.sample(vertices, len(vertices))

        if individuo not in individuosPop:
            individuosPop.append(individuo)

def funcaoObjetivo():
    contador = 0

    for individuo in individuosPop:
        valorTotal = 0
        for i in range(len(individuo)-1):
            u = individuo[i]
            v = individuo[i+1]
            valorTotal += grafo.es[grafo.get_eid(u, v)]["weight"]
        u = individuo[-1]
        v = individuo[0]
        valorTotal += grafo.es[grafo.get_eid(u, v)]["weight"]
        fitnessIndividuos[contador] = valorTotal
        contador+=1

def Elitismo():
    individuosElitismo = []
    indicesfitnessIndividuos = list(range(numIndividuosPop))

    for i in range (numIndividuosElitismo):
        indiceMelhor = min(indicesfitnessIndividuos, key=lambda i: fitnessIndividuos[i])
        melhor = individuosPop[indiceMelhor].copy()
        indicesfitnessIndividuos.remove(indiceMelhor)

        individuosElitismo.append(melhor)

    return individuosElitismo


def SorteioRoletaIndividuos():
    n = len(fitnessIndividuos)

    probabilidades = [0] * n
    indicesUsados = set()

    for rank in range(n, 0, -1):
        indice = min(
            (i for i in range(n) if i not in indicesUsados),
            key=lambda i: fitnessIndividuos[i]
        )
        indicesUsados.add(indice)
        probabilidades[indice] = rank

    soma = sum(probabilidades)
    probabilidades = [p / soma for p in probabilidades]

    pais = []

    for i in range(numIndividuosCruzamento // 2):
        pai1 = random.choices(
            range(numIndividuosPop),
            weights=probabilidades,
            k=1
        )[0]

        pai2 = pai1
        while pai2 == pai1:
            pai2 = random.choices(
                range(numIndividuosPop),
                weights=probabilidades,
                k=1
            )[0]

        #print("PaiA: " +  str(individuosPop[pai1]) + " - PaiB: " + str(individuosPop[pai2]))
        pais.extend([individuosPop[pai1], individuosPop[pai2]])

    #print("|||||||||||||||||||||||||||||||||||")
    return pais

def Cruzamento(paisCruzamento):
    filhos = []
    for i in range(numIndividuosCruzamento//2):
        paiA = paisCruzamento[i*2]
        paiB = paisCruzamento[(i*2) + 1]
        #print("PaiA: " + str(paiA))
        #print("PaiB: " + str(paiB))

        posCorte1 = random.randint(0, len(paiA)-2)
        posCorte2 = random.randint(posCorte1+1, len(paiA)-1)

        corteA = paiA[posCorte1:posCorte2+1]
        corteB = paiB[posCorte1:posCorte2+1]        

        elementosA = [gene for gene in (paiA[posCorte2+1:] + paiA[:posCorte2+1]) if gene not in corteB]
        elementosB = [gene for gene in (paiB[posCorte2+1:] + paiB[:posCorte2+1]) if gene not in corteA]

        filho1 = [-1] * len(paiA)
        filho1[posCorte1:posCorte2+1] = corteB
        pos = (posCorte2+1) % len(filho1)
        for gene in elementosA:            
            filho1[pos] = gene
            pos = (pos + 1) % len(filho1)

        filho2 = [-1] * len(paiB)
        filho2[posCorte1:posCorte2+1] = corteA
        pos = (posCorte2+1) % len(filho2)
        for gene in elementosB:            
            filho2[pos] = gene
            pos = (pos + 1) % len(filho2)

        filhos.extend([filho1, filho2])
        
    #print("||||||||||||||||||||||||||||||||||")
    return filhos

def Mutacao(filhos, numMutacoes):

    indices = random.sample(range(len(filhos)), numMutacoes)
    for cont in indices:
        i = random.randint(0, len(filhos[cont]) - 1)
        j = i

        while j == i:
            j = random.randint(0, len(filhos[cont]) - 1)

        filhos[cont][i], filhos[cont][j] = filhos[cont][j], filhos[cont][i]

    return filhos

def main():

    defineIndividuosInicial()

    melhorFitness = math.inf
    geracoesSemMelhora = 0

    while geracoesSemMelhora < criterioParada:

        funcaoObjetivo()

        fitnessAtual = min(fitnessIndividuos)

        if fitnessAtual < melhorFitness:
            melhorFitness = fitnessAtual
            geracoesSemMelhora = 0
        
        else:
            geracoesSemMelhora += 1

        elite = Elitismo()
        pais = SorteioRoletaIndividuos()
        filhos = Cruzamento(pais)

        if geracoesSemMelhora >= (criterioParada * 0.75):
            numMutacoes = int(numIndividuosMutacao *1.5)
            filhos = Mutacao(filhos, numMutacoes)
        else:
            filhos = Mutacao(filhos, numIndividuosMutacao)

        individuosPop.clear()
        individuosPop.extend(elite)
        
        numFilhos = numIndividuosPop - len(elite)
        individuosPop.extend(filhos[:numFilhos])
    
    funcaoObjetivo()
    indiceMelhor = fitnessIndividuos.index(min(fitnessIndividuos))
    print(f"Melhor solução encontrada:\n {individuosPop[indiceMelhor]}")
    print(f"Custo: {fitnessIndividuos[indiceMelhor]}")

if __name__ == "__main__":
    main()