# Algoritmo_Genetico_CaixeiroViajante

Documentação do algoritmo do Caixeiro Viajante
Alunos: Luís Filipe Rabelo Leão de Oliveira, Mateus Dos Santos Coelho
INTRODUÇÃO
Este programa tem como função implementar um algoritmo capaz de solucionar o problema do Caixeiro Viajante. Para isso é necessário percorrer um determinado número de cidades e retornar para a cidade inicial, considerando o menor custo. A linguagem escolhida foi Python, assim como a biblioteca igraph, para o auxílio na construção do grafo. A lógica utilizada foi de um algoritmo genético.
OBJETIVO
O objetivo do programa é receber um arquivo.txt, que contenha linhas, com três colunas cada. A primeira coluna é referente ao vértice de origem, a segunda ao vértice de destino e a terceira coluna representa o custo entre esses vértices. O programa deve retornar a melhor solução encontrada, bem como o custo total, a partir de uma lógica de um algoritmo genético.
EXECUÇÃO
Para a execução, é necessário um arquivo.txt, neste caso “dadosCaixeiroViajante.txt”, utilizado para a leitura do grafo. Para executar o programa, basta digitar o comando python3 CaixeiroViajante.py no terminal.
ENTRADAS E SAÍDAS
O arquivo “dadosCaixeiroViajante.txt” e o “lau15.txt” são utilizados neste caso. O primeiro é composto pelas linhas:
1    2    2
1    3    7
1    4    1
5    5
3    5
2    4    3
5    4
4    6
5    8
5    2
Enquanto o segundo é composto pelos dados padrões de "lau15".

Quando executamos o algoritmo, por se tratar de um algoritmo genético, as saídas podem ser variadas. A melhor solução e o custo total podem variar entre execuções. O exemplo de saída a seguir, não é uma saída padrão.
- Custo = 18.

Saída para Lau15:
- Custo = 291.

CÓDIGO
A lógica utilizada para a resolução do problema do Caixeiro Viajante utilizada foi de um algoritmo genético. Nele consideramos um critério de parada de 4 gerações sem melhoras e o número de indivíduos utilizados é 8, para o primeiro caso. Para o caso de “Lau15”, consideramos um critério de parada de 100 gerações sem melhoras, e o número de indivíduos 100.
Foi utilizado os métodos de Elitismo, Cruzamento e Mutação, para escolher os indivíduos que formarão a população. A quantidade de indivíduos proveniente de cada método é definida previamente.


Essa primeira parte do algoritmo é responsável pela criação do grafo, bem como pela definição dos parâmetros de números de indivíduos da população, o critério de parada e a quantidade de indivíduos vindos de cada método.

A primeira função define a população de indivíduos inicial, que é escolhida por meio de um sorteio.
A segunda função é responsável por calcular o fitness de cada indivíduo de uma determinada população, armazenando esse dado no vetor.
A terceira função é a de Elitismo, ela pega os indivíduos de uma população que possuem a
maior aptidão(fitness) e preenche as vagas direcionadas aos indivíduos de Elitismo com as melhores opções.

Essa função é responsável por selecionar os pais que participarão do cruzamento. Essa seleção é feita por meio de uma roleta viciada, onde é criado um rank entre os indivíduos. Seguindo esse rank, é calculada a probabilidade, que influencia diretamente no sorteio, dando mais chances para os que possuem um menor peso, e, consequentemente, uma maior probabilidade.

A função de Cruzamento gera os filhos, por meio do cruzamento entre os pais que foram anteriormente selecionados. É feito um corte nos elementos dos pais, que serão perpetuados para os filhos, e depois, o restante dos genes é completado.

A função de mutação faz a alteração nos genes de alguns dos filhos gerados. Essa mutação troca dois genes de lugar, gerando um novo indivíduo. Essa função é importante para garantir uma maior diversidade genética da população.

Por último temos a main. Ela organiza a ordem de chamada das funções, bem como atualiza o número de gerações sem melhoria. No nosso caso, conforme sugerido pelo slide, adotamos um critério que modifica o número de mutações dos filhos. Caso o número de gerações sem melhoria seja maior que 0.75 * critério de parada, nós optamos por aumentar a quantidade de indivíduos que sofrem a mutação. Isso é interessante, pois há casos em que uma maior mutação pode levar a outros indivíduos que ainda não haviam sido explorados e que podem ter um fitness melhor.
Após encontrar a possível melhor solução, ela é impressa, juntamente com o seu custo.

