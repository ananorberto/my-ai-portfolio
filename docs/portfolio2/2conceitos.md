
## 2. Apresentação dos Conceitos Principais

A abordagem de resolução de problemas por busca se baseia na ideia de que um agente pode adotar um objetivo e trabalhar para satisfazê-lo. Um agente de solução de problemas é um tipo de agente baseado em objetivos.

Os principais conceitos envolvidos são:

*   **Formulação de Objetivo:** O agente adota um ou mais objetivos que deseja alcançar.
*   **Formulação de Problema:** O agente descreve os estados possíveis do "mundo" e as ações que pode realizar para transitar entre esses estados, visando atingir o objetivo. Estados do mundo podem ser considerados como totalidades sem estrutura interna visível (representação atômica), que é a representação considerada na busca básica.
*   **Espaço de Estados (State Space):** É uma representação formal do problema. É definido por uma quádrupla `[N, A, S, GD]`, onde:
    *   `N` é o conjunto de nós ou estados do grafo, correspondendo aos estados no processo de resolução do problema.
    *   `A` é o conjunto de arcos que conectam pares de nós, representando conexões diretas ou ações que levam de um estado a outro.
    *   `S` é o estado inicial.
    *   `GD` é a descrição dos estados objetivo, ou seja, a condição que define que o problema foi resolvido.
    Uma solução para um problema é representada como um caminho no grafo do estado inicial a um estado objetivo.
*   **Busca (Search):** Antes de agir, o agente simula sequências de ações em seu modelo (o espaço de estados) para encontrar um caminho que leve ao objetivo. Isso envolve testar sistematicamente caminhos alternativos.
*   **Execução:** Uma vez encontrado um caminho (solução) pela busca, o agente executa as ações correspondentes no ambiente real.
*   **Agentes de Solução de Problemas:** São agentes baseados em objetivos que utilizam a busca em representações atômicas de estados para encontrar soluções.
*   **Estratégias de Busca:** São os algoritmos usados para explorar o espaço de estados. Elas podem ser:
    *   **Busca Cega (Uninformed Search):** Algoritmos que não utilizam nenhuma informação sobre o quão próximo um estado está do(s) objetivo(s) além da definição do problema.
    *   **Busca Informada (Informed Search):** Algoritmos que utilizam dicas específicas do domínio (heurísticas) sobre a localização dos objetivos para guiar a busca de forma mais eficiente.
*   **Heurísticas:** São funções, denotadas como `h(n)`, que fornecem uma estimativa do custo do caminho mais econômico do estado no nó `n` para um estado objetivo. Elas são informações específicas do domínio que podem melhorar significativamente a eficiência da busca.
*   **Medidas de Performance:** Critérios para avaliar algoritmos de busca:
    *   **Completude (Completeness):** O algoritmo garante encontrar uma solução quando existe uma, ou reportar a falha corretamente.
    *   **Otimização de Custos (Cost Optimization):** O algoritmo garante encontrar a solução com o menor custo.
    *   **Complexidade de Tempo (Time Complexity):** Quanto tempo leva para encontrar a solução.
    *   **Complexidade de Espaço (Space Complexity):** Quanta memória é necessária para a busca.
*   **Filas:** Estruturas de dados usadas para gerenciar a ordem em que os nós são explorados pelos algoritmos de busca: fila FIFO (First-In, First-Out) para busca em largura, pilha LIFO (Last-In, First-Out) para busca em profundidade, e fila de prioridade para busca *best-first*. O uso dessas estruturas permite que os algoritmos explorem estados não testados (lista *open*) e evitem repetir caminhos infrutíferos (lista *closed*).

### 2.1 Discussão PEAS para Problema de Navegação Robótica

Para ilustrar a aplicação do modelo PEAS (Performance, Environment, Actuators, Sensors) na resolução de problemas por busca, analisaremos o caso de um robô de navegação em um ambiente de armazém:

**Performance (Medida de Desempenho):**
- Minimizar o tempo total para encontrar e transportar itens
- Minimizar o consumo de energia
- Evitar colisões com obstáculos e outros robôs
- Completar todas as tarefas de coleta na ordem correta

**Environment (Ambiente):**
- Armazém com corredores, prateleiras e áreas de carga/descarga
- Obstáculos fixos (paredes, prateleiras) e dinâmicos (outros robôs, trabalhadores)
- Superfície plana com possíveis rampas ou elevadores
- Condições de iluminação variáveis

**Actuators (Atuadores):**
- Motores para movimentação (frente, trás, rotação)
- Braço robótico para pegar itens
- Sinalizadores visuais e sonoros
- Sistema de frenagem

**Sensors (Sensores):**
- Câmeras para reconhecimento de objetos e leitura de códigos
- Sensores de proximidade (ultrassônicos, infravermelhos)
- GPS interno ou sistema de localização baseado em marcadores
- Sensores de velocidade e aceleração
- Sensores de carga da bateria

### 2.2 Descrição do Ambiente do Problema

O ambiente de navegação robótica em um armazém possui as seguintes propriedades:

- **Observável parcialmente:** O robô só consegue perceber o que está em seu campo de visão imediato.
- **Determinístico:** As ações do robô têm resultados previsíveis.
- **Sequencial:** Decisões anteriores afetam estados futuros e opções disponíveis.
- **Dinâmico:** O ambiente pode mudar enquanto o robô opera (outros robôs, trabalhadores).
- **Contínuo:** Posição e velocidade variam continuamente, embora possam ser discretizadas para simplificação.
- **Multi-agente:** Múltiplos robôs podem estar operando simultaneamente no mesmo ambiente.

Compreender estas propriedades é fundamental para escolher os algoritmos de busca adequados. Por exemplo, a natureza parcialmente observável do ambiente pode exigir replaneamento frequente, enquanto sua natureza dinâmica pode favorecer algoritmos que possam se adaptar rapidamente a mudanças.


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

