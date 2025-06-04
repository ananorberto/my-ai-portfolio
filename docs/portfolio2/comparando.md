## Comparação de Algoritmos e Aplicações Práticas

### Tabela Comparativa de Algoritmos de Busca

**Tabela 1: Comparação de Algoritmos de Busca em Termos de Propriedades e Desempenho**

| Algoritmo | Completude | Otimalidade | Complexidade de Tempo | Complexidade de Espaço | Aplicações Típicas |
|-----------|------------|-------------|----------------------|------------------------|-------------------|
| Busca em Largura (BFS) | Sim | Sim (para custos uniformes) | O(b^d) | O(b^d) | Caminhos mais curtos em grafos não ponderados, quebra-cabeças com poucas ações |
| Busca em Profundidade (DFS) | Não (em espaços infinitos) | Não | O(b^m) | O(bm) | Labirintos, quebra-cabeças, análise de jogos |
| Busca com Aprofundamento Iterativo (IDDFS) | Sim | Sim (para custos uniformes) | O(b^d) | O(bd) | Problemas com profundidade de solução desconhecida |
| Busca de Custo Uniforme | Sim | Sim | O(b^[C*/ε]) | O(b^[C*/ε]) | Caminhos de menor custo em grafos ponderados |
| Busca Gulosa Best-First | Não | Não | O(b^m) | O(b^m) | Problemas onde a heurística é informativa |
| A* | Sim | Sim (com heurística admissível) | O(b^d) | O(b^d) | Planejamento de rotas, navegação robótica |
| Subida de Encosta | Não | Não | O(∞) | O(1) | Otimização local, ajuste de parâmetros |
| Recozimento Simulado | Não | Não (probabilisticamente sim) | O(∞) | O(1) | Problemas com muitos máximos locais |
| Algoritmos Genéticos | Não | Não (probabilisticamente sim) | O(∞) | O(p) | Otimização combinatória, design |

Onde:
- b: fator de ramificação
- d: profundidade da solução mais rasa
- m: profundidade máxima do espaço de estados
- C*: custo da solução ótima
- ε: diferença mínima entre custos de ações
- p: tamanho da população

### Gráfico Comparativo de Desempenho

**Figura 1: Comparação do Número de Nós Expandidos por Diferentes Algoritmos de Busca em Função da Profundidade da Solução**

![Comparação de Algoritmos de Busca](comparison_chart.png)

O gráfico acima ilustra como o número de nós expandidos cresce com a profundidade da solução para diferentes algoritmos. Observe como a busca informada (A*) com uma boa heurística expande significativamente menos nós que os algoritmos de busca cega, demonstrando a importância do conhecimento específico do domínio na eficiência da busca.

### Aplicações Práticas

A resolução de problemas por busca tem inúmeras aplicações práticas em diversos campos:

1. **Navegação e Planejamento de Rotas:**
   - Sistemas GPS utilizam algoritmos como A* para encontrar o caminho mais curto ou mais rápido entre dois pontos.
   - Robôs autônomos empregam técnicas de busca para navegar em ambientes desconhecidos ou dinâmicos.

2. **Jogos e Entretenimento:**
   - Inteligência artificial em jogos de tabuleiro como xadrez e Go utiliza busca adversária (minimax, MCTS).
   - Personagens não-jogáveis (NPCs) em videogames usam algoritmos de busca para encontrar caminhos e tomar decisões.

3. **Otimização de Recursos:**
   - Problemas de escalonamento de tarefas em sistemas de produção.
   - Otimização de rotas para frotas de veículos (problema do caixeiro viajante).
   - Alocação eficiente de recursos em sistemas distribuídos.

4. **Bioinformática:**
   - Alinhamento de sequências de DNA e proteínas.
   - Predição de estruturas de proteínas.
   - Descoberta de medicamentos através de algoritmos genéticos.

5. **Processamento de Linguagem Natural:**
   - Análise sintática de sentenças.
   - Tradução automática.
   - Sistemas de perguntas e respostas.



## Referências Bibliográficas

RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013.

CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. *Introduction to Algorithms*. 3. ed. Cambridge: MIT Press, 2009.

KORF, R. E. Depth-first iterative-deepening: An optimal admissible tree search. *Artificial Intelligence*, v. 27, n. 1, p. 97-109, 1985.

HART, P. E.; NILSSON, N. J.; RAPHAEL, B. A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics*, v. 4, n. 2, p. 100-107, 1968.

KIRKPATRICK, S.; GELATT, C. D.; VECCHI, M. P. Optimization by simulated annealing. *Science*, v. 220, n. 4598, p. 671-680, 1983.

HOLLAND, J. H. *Adaptation in Natural and Artificial Systems*. Ann Arbor: University of Michigan Press, 1975.

KOZA, J. R. *Genetic Programming: On the Programming of Computers by Means of Natural Selection*. Cambridge: MIT Press, 1992.

SILVER, D. et al. Mastering the game of Go with deep neural networks and tree search. *Nature*, v. 529, n. 7587, p. 484-489, 2016.

THRUN, S.; BURGARD, W.; FOX, D. *Probabilistic Robotics*. Cambridge: MIT Press, 2005.

LAVALLE, S. M. *Planning Algorithms*. Cambridge: Cambridge University Press, 2006.


| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 27/05/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

