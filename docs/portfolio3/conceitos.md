#### **Aprofundando em CSPs: Conceitos e Aplicação**

##### **Definição Formal**

Um Problema de Satisfação de Restrições (CSP) é formalmente definido por três componentes:

*   **Variáveis (X):** Um conjunto de variáveis {X₁, X₂, ..., Xn}.
*   **Domínios (D):** Um conjunto de domínios {D₁, D₂, ..., Dn}, onde cada Di é o conjunto finito de valores possíveis para a variável Xi.
*   **Restrições (C):** Um conjunto de restrições {C₁, C₂, ..., Ck}. Cada restrição Cj especifica uma combinação permitida de valores para um subconjunto de variáveis.

Uma **solução** para um CSP é uma atribuição completa e consistente de valores para todas as variáveis, ou seja, uma atribuição onde cada variável Xi recebe um valor de seu domínio Di, e todas as restrições Cj são satisfeitas (RUSSELL; NORVIG, 2010).

##### **Exemplo Prático: Coloração de Mapas**

Consideremos o problema clássico de colorir um mapa de forma que regiões adjacentes não tenham a mesma cor, usando um número limitado de cores (por exemplo, Vermelho, Verde, Azul).

*   **Variáveis (X):** Cada região do mapa (ex: Região A, Região B, ...).
*   **Domínios (D):** O conjunto de cores disponíveis para cada região (ex: {Vermelho, Verde, Azul}).
*   **Restrições (C):** Para cada par de regiões adjacentes (ex: Região A e Região B), a restrição é que suas cores atribuídas devem ser diferentes (Cor(A) ≠ Cor(B)).

O **grafo de restrições** neste caso teria as regiões como nós e uma aresta entre duas regiões se elas forem adjacentes.

##### **Modelagem PEAS (Performance, Environment, Actuators, Sensors)**

Podemos modelar um agente que resolve o problema de coloração de mapas usando o framework PEAS (RUSSELL; NORVIG, 2010):

*   **P (Performance Measure - Medida de Desempenho):** Completa a coloração do mapa satisfazendo todas as restrições (regiões adjacentes com cores diferentes). Idealmente, minimiza o número de cores usadas ou o tempo de resolução.
*   **E (Environment - Ambiente):** O mapa a ser colorido, definido por suas regiões e adjacências. O ambiente é estático (o mapa não muda), discreto (número finito de regiões e cores) e conhecido (a estrutura do mapa é dada).
*   **A (Actuators - Atuadores):** A capacidade de atribuir uma cor a uma região específica.
*   **S (Sensors - Sensores):** A capacidade de perceber o estado atual da coloração, incluindo quais regiões são adjacentes e quais cores já foram atribuídas a elas e a seus vizinhos.

##### **3.4 Técnicas de Resolução e Propagação de Restrições**

A resolução de CSPs frequentemente envolve algoritmos de busca, como o **Backtracking Search** (RUSSELL; NORVIG, 2010). No entanto, a eficiência desses algoritmos é drasticamente melhorada pela **propagação de restrições**. Essa técnica usa as restrições para reduzir o número de valores legais para uma variável, o que pode, por sua vez, reduzir os valores legais para outras variáveis.

*   **Forward Checking:** Quando uma variável X recebe um valor, o Forward Checking verifica cada variável Y não atribuída que está conectada a X por uma restrição e remove de Dy qualquer valor inconsistente com o valor atribuído a X.
*   **Consistência de Arco (AC-3):** Este algoritmo busca tornar o grafo de restrições arco-consistente. Um arco (Xi, Xj) é consistente se, para cada valor x no domínio Di, existe algum valor y no domínio Dj que satisfaz a restrição binária entre Xi e Xj. O AC-3 remove iterativamente valores dos domínios que não podem satisfazer a consistência de arco, potencialmente simplificando muito o problema antes ou durante a busca.

A propagação de restrições ajuda a detectar falhas mais cedo no processo de busca, podando subárvores inteiras que não levariam a uma solução.

#### **Algoritmo Exemplo: Backtracking Search para CSPs**

O algoritmo de Backtracking é uma abordagem fundamental para resolver CSPs. Ele funciona atribuindo valores às variáveis uma a uma e, ao encontrar uma atribuição que viola uma restrição, ele 

 retrocede (backtracks).

**Pseudocódigo do Algoritmo de Backtracking para CSPs:**

```
função BACKTRACKING-SEARCH(csp)
    retorna BACKTRACK({}, csp)

função BACKTRACK(atribuição, csp)
    se atribuição está completa então retorna atribuição

    var ← SELECIONAR-VARIÁVEL-NÃO-ATRIBUÍDA(csp)

    para cada valor em ORDENAR-VALORES-DOMÍNIO(var, atribuição, csp) fazer
        se valor é consistente com atribuição de acordo com as restrições de csp então
            adicionar {var = valor} à atribuição
            inferências ← INFERÊNCIA(csp, var, valor) // Ex: Forward Checking, AC-3
            se inferências ≠ falha então
                adicionar inferências à atribuição
                resultado ← BACKTRACK(atribuição, csp)
                se resultado ≠ falha então
                    retorna resultado
            remover {var = valor} e inferências da atribuição

    retorna falha
```

**Explicação do Pseudocódigo:**

1.  **`BACKTRACKING-SEARCH(csp)`:** Inicia a busca com uma atribuição vazia.
2.  **`BACKTRACK(atribuição, csp)`:**
    *   **Verificação de Conclusão:** Se todas as variáveis receberam valores consistentes, a solução foi encontrada e é retornada.
    *   **Seleção de Variável:** Escolhe uma variável ainda não atribuída (heurísticas como *Minimum Remaining Values - MRV* podem ser usadas aqui).
    *   **Iteração de Valores:** Para cada valor possível no domínio da variável selecionada (heurísticas como *Least Constraining Value - LCV* podem ordenar os valores):
        *   **Verificação de Consistência:** Verifica se atribuir o valor atual à variável viola alguma restrição com as variáveis já atribuídas.
        *   **Atribuição e Inferência:** Se consistente, o valor é temporariamente atribuído. Técnicas de inferência (propagação de restrições como Forward Checking ou AC-3) são aplicadas para deduzir consequências dessa atribuição e reduzir domínios de outras variáveis.
        *   **Chamada Recursiva:** Se a inferência não detectou inconsistências, a função `BACKTRACK` é chamada recursivamente para a próxima variável.
        *   **Backtracking:** Se a chamada recursiva falhar (não encontrar solução a partir dali) ou se o valor inicial não for consistente ou a inferência falhar, a atribuição temporária e as inferências são removidas, e o algoritmo tenta o próximo valor. Se nenhum valor funcionar para a variável atual, a função retorna falha, indicando a necessidade de retroceder na chamada anterior.

Este algoritmo, combinado com heurísticas eficientes de seleção de variáveis/valores e técnicas de propagação de restrições, forma a base para resolver muitos CSPs complexos de forma eficaz.




---

### **Bibliografia**

LUGER, George F. **Artificial Intelligence: Structures and Strategies for Complex Problem Solving**. 6th ed. Boston: Addison-Wesley, 2008.

RUSSELL, Stuart J.; NORVIG, Peter. **Artificial Intelligence: A Modern Approach**. 3rd ed. Upper Saddle River, NJ: Prentice Hall, 2010.

SUTTON, Richard S.; BARTO, Andrew G. **Reinforcement Learning: An Introduction**. 2nd ed. Cambridge, MA: MIT Press, 2018.

---

| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 03/06/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

