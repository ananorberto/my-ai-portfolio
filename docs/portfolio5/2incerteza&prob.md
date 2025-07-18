# 2. Incerteza e Probabilidade

Na Inteligência Artificial (IA), um dos maiores desafios é construir agentes que operem de forma eficaz em ambientes que são, por natureza, imprevisíveis e complexos. A realidade é que o mundo raramente é tão organizado e determinístico quanto gostaríamos. É aqui que entra a **incerteza**, um elemento fundamental que os agentes de IA precisam aprender a quantificar e gerenciar.

### Por que a IA precisa lidar com incerteza?

Como vimos nas aulas e como Russell e Norvig (2010, p. 54) destacam, **"agentes podem precisar lidar com incerteza, seja devido a observabilidade parcial, não determinismo ou uma combinação dos dois"**. Imagine um robô explorando um ambiente desconhecido: seus sensores podem falhar ou fornecer dados imprecisos (observabilidade parcial), e suas ações podem não ter resultados garantidos (não determinismo). Por exemplo, um sistema de navegação autônoma em um carro não pode ter certeza absoluta de que um pedestre parado continuará parado ou que um semáforo verde permanecerá verde tempo suficiente.

Essa incerteza não é apenas um "problema técnico"; é uma característica intrínseca do mundo real. Ela surge da nossa "preguiça" em especificar cada detalhe do universo e da nossa "ignorância" sobre todas as condições que afetam um resultado (RUSSELL; NORVIG, 2010, p. 72). Além disso, **"sistemas de raciocínio e planejamento devem ser capazes de lidar com a incerteza"**, pois as informações sensoriais raramente são perfeitamente confiáveis (RUSSELL; NORVIG, 2010). A busca por uma racionalidade perfeita, que exigiria modelar cada minúcia do mundo e calcular todas as consequências, é muitas vezes computacionalmente inviável.

### A transição dos agentes lógicos para agentes que tomam decisões com base em graus de crença

Tradicionalmente, muitos agentes de IA, especialmente os agentes lógicos, operam com base em verdades absolutas: uma proposição é verdadeira, falsa ou desconhecida. Eles mantêm um "estado de crença" que representa o conjunto de todos os estados possíveis do mundo em que o agente poderia estar e, a partir daí, geram planos de contingência para cada eventualidade. Contudo, essa abordagem, embora rigorosa, possui desvantagens significativas. Ela pode levar ao que chamamos de "problema da qualificação", onde é impossível listar todas as exceções ou condições que podem impedir uma regra de ser aplicada com certeza. Além disso, em ambientes complexos, manter um conjunto completo de todos os estados possíveis pode ser inviável.

É nesse ponto que a **probabilidade** se apresenta como uma alternativa mais flexível e realista. Enquanto um agente lógico pode ter uma opinião binária (verdadeiro/falso/desconhecido) sobre uma sentença, **"um agente probabilístico pode ter um grau numérico de crença entre 0 (para sentenças que são certamente falsas) e 1 (certamente verdadeiras)"** (RUSSELL; NORVIG, 2010, p. 56). Essa capacidade de expressar "graus de crença" permite que o agente tome decisões mais nuances e racionais, mesmo diante de informações incompletas ou ruidosas. Como ilustrado pelo exemplo do Mundo do Wumpus, um agente probabilístico pode calcular as chances de um buraco em diferentes quadrados, permitindo-lhe evitar áreas de alta probabilidade de risco, algo que um agente puramente lógico não conseguiria discernir (RUSSELL; NORVIG, 2010, p. 71).

### Conceitos fundamentais para quantificar incertezas

A ferramenta central para lidar com graus de crença é a **teoria da probabilidade** (RUSSELL; NORVIG, 2010, p. 56). Segundo Laplace, **"A teoria da probabilidade não é nada mais do que o senso comum reduzido a cálculo"** (LAPLACE, 1819, citado em RUSSELL; NORVIG, 2010, p. 95). Ela nos fornece uma linguagem formal para quantificar a incerteza, expressando a incapacidade de um agente de chegar a uma decisão definitiva sobre a verdade de uma sentença e sumarizando suas crenças em relação às evidências (RUSSELL; NORVIG, 2010, p. 72).

Alguns conceitos fundamentais para entender essa quantificação são:

*   **Variáveis Aleatórias, Espaço Amostral e Eventos:**
    *   Uma **variável aleatória** é uma função que associa um resultado numérico a cada possível desfecho de um evento (LUGER, p. 380). Por exemplo, "Chuva" é uma variável aleatória que pode assumir os valores 'Verdadeiro' ou 'Falso'.
    *   Um **espaço amostral** é o conjunto de todos os resultados possíveis de um experimento ou situação. Por exemplo, ao lançar um dado, o espaço amostral é {1, 2, 3, 4, 5, 6} (LUGER, p. 375).
    *   Um **evento** é um subconjunto do espaço amostral. A probabilidade de um evento é a soma das probabilidades dos "mundos" (ou seja, atribuições de valores a todas as variáveis aleatórias) em que esse evento ocorre (RUSSELL; NORVIG, 2010, p. 59).

*   **Princípio da Utilidade Máxima Esperada (MEU - Maximum Expected Utility):**
    *   A decisão racional para um agente não se baseia apenas no que ele acredita ser verdadeiro, mas também no que ele **deseja** que aconteça. Essa "vontade" é capturada pela **utilidade**, uma medida numérica da desejabilidade dos resultados (RUSSELL; NORVIG, 2010, p. 57).
    *   O princípio do MEU afirma que um agente racional deve escolher a ação que maximiza sua **utilidade esperada** (RUSSELL; NORVIG, 2010, p. 57). A utilidade esperada é a média dos resultados possíveis de uma ação, ponderada pela probabilidade de cada resultado ocorrer.
    *   Como Russell e Norvig (2010, p. 115) sumarizam, **"a teoria da probabilidade descreve o que um agente deve acreditar com base na evidência, a teoria da utilidade descreve o que um agente quer, e a teoria da decisão une as duas para descrever o que um agente deve fazer"**. Esse princípio forma a base para a tomada de decisões em ambientes incertos, e seu uso foi amplamente promovido por trabalhos como o de Judea Pearl (1988).

### Exemplos simples: O Paradoxo de Monty Hall

Para ilustrar como a intuição pode falhar e como o raciocínio probabilístico é essencial, podemos considerar o **Paradoxo de Monty Hall**. Este problema, que inclusive foi abordado nos slides da Aula 16, demonstra claramente a importância de atualizar as crenças probabilísticas diante de novas evidências.

No problema, um participante escolhe uma porta (digamos, Porta 1) entre três, sabendo que atrás de uma delas há um carro e atrás das outras duas, bodes. O apresentador, que sabe onde o carro está, abre uma das outras duas portas (digamos, Porta 3), revelando um bode. Ele então pergunta ao participante se ele gostaria de trocar sua escolha inicial (Porta 1) pela porta restante (Porta 2).

Intuitivamente, muitas pessoas pensam que, com duas portas restantes, a probabilidade de o carro estar atrás de cada uma delas se torna 50%. No entanto, a análise probabilística revela que **trocar de porta dobra as chances de ganhar o carro**.

*   No início, cada porta tem 1/3 de chance de ter o carro.
*   Quando o participante escolhe a Porta 1, ela tem 1/3 de chance de ter o carro.
*   As Portas 2 e 3, juntas, têm 2/3 de chance de ter o carro.
*   Quando Monty Hall abre a Porta 3 e revela um bode, ele concentra os 2/3 de probabilidade restantes na Porta 2 (se o carro não estiver na Porta 1). Isso ocorre porque Monty *sempre* abrirá uma porta com um bode. Se o carro estivesse na Porta 2, ele teria que abrir a Porta 3. Se estivesse na Porta 3, ele teria que abrir a Porta 2. Se estivesse na Porta 1 (sua escolha inicial), ele poderia abrir aleatoriamente a Porta 2 ou 3, mas de qualquer forma, a porta que ele *não* abriu (Porta 2, em nosso exemplo) retém a maior probabilidade (2/3).

Este exemplo, embora simples, sublinha como a formalização probabilística é crucial para tomar as melhores decisões em situações de incerteza, mesmo quando a intuição pode levar a erros.

<p align="center">
  <a title="Erzbischof, CC BY-SA 3.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Monty_problem_monte_carlo.svg">
    <img width="512" alt="Monty problem monte carlo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Monty_problem_monte_carlo.svg/512px-Monty_problem_monte_carlo.svg.png?20091009153013">
  </a><br>
  <em>Figura 1: Distribuição de probabilidades no problema de Monty Hall após múltiplas simulações (Monte Carlo).</em>
</p>



Em resumo, a quantificação da incerteza por meio da probabilidade não é um luxo, mas uma necessidade para a Inteligência Artificial. Ela permite que agentes operem de forma mais robusta e racional em um mundo imprevisível, transformando dados incompletos e ruidosos em decisões inteligentes. Como visto nos slides da Aula 16, as Redes Bayesianas, que estudaremos a seguir, fornecem uma formalização gráfica para representar e raciocinar com essa incerteza de forma eficiente.

---
**Referências**

RUSSELL, Stuart J.; NORVIG, Peter. **Artificial Intelligence**: A Modern Approach. 3. ed. Upper Saddle River: Prentice Hall, 2010.

LUGER, George F. **Artificial Intelligence**: Structures and Strategies for Complex Problem Solving. 6. ed. Boston: Pearson Education, 2009.

Erzbischof, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons

---


| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 16/07/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

