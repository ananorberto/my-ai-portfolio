
# Agentes Lógicos: Representando o Conhecimento e Raciocinando sobre o Mundo

Este tópico do portfólio aprofundará o conceito de **agentes lógicos**, uma abordagem fundamental na Inteligência Artificial que visa construir sistemas capazes de raciocinar sobre o conhecimento. Os agentes inteligentes no mundo real precisam lidar com a incerteza e tomar decisões baseadas em informações, e os agentes lógicos oferecem uma base para isso através da representação explícita de conhecimento e do uso de processos de inferência para derivar novas conclusões.

## 1. Definição e Importância dos Agentes Lógicos

**Agentes lógicos** são sistemas de IA que utilizam a lógica para representar o conhecimento sobre o mundo e para raciocinar sobre esse conhecimento, a fim de tomar decisões. A ideia central é que a inteligência pode ser alcançada por meio de **representações internas de conhecimento** e **processos de raciocínio** que operam sobre essas representações (RUSSELL; NORVIG, 2010, p. 234).

A importância dessa abordagem é imensa. Ao invés de meros mecanismos reflexivos, agentes lógicos podem **combinar e recombinar informações para múltiplos propósitos**, adaptar-se a mudanças no ambiente atualizando seu conhecimento e aceitar novas tarefas na forma de objetivos explicitamente descritos (RUSSELL; NORVIG, 2010, p. 235). Essa capacidade de raciocínio simbólico foi um dos pilares iniciais da IA e continua sendo relevante para a compreensão de como sistemas inteligentes podem funcionar.

## 2. Arquitetura Geral dos Agentes Baseados em Conhecimento

A estrutura de um agente lógico é centrada em sua **Base de Conhecimento (KB)**, que é um conjunto de sentenças que representam assertions sobre o mundo. Russell e Norvig (2010, p. 235) definem uma sentença como um termo técnico, expressa em uma **linguagem de representação de conhecimento**. O agente interage com essa KB por meio de duas operações básicas:

*   **TELL**: Adiciona novas sentenças à KB, informando o agente sobre o que ele percebe no ambiente (seus perceptos) ou as ações que executa.
*   **ASK**: Consulta a KB para determinar que ação deve ser realizada, fazendo perguntas sobre o estado do mundo e possíveis consequências.

Essa arquitetura básica pode ser visualizada no pseudocódigo `KB-AGENT` (RUSSELL; NORVIG, 2010, p. 236):

```
function KB-AGENT(percept) returns an action
  persistent: KB, a knowledge base
              t, a counter, initially 0, indicating time
  TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
  action <- ASK(KB, MAKE-ACTION-QUERY(t))
  TELL(KB, MAKE-ACTION-SENTENCE(action, t))
  t <- t + 1
  return action
```

Como visto em sala nos slides (FGA0221 –IA, s.d., Redes Bayesianas), a base de conhecimento de uma rede Bayesiana também carrega informações de probabilidade em seus nós. Essa arquitetura permite uma **abordagem declarativa** para a construção de sistemas, onde o designer "diz" ao agente o que ele precisa saber, ao invés de codificar diretamente os comportamentos desejados (RUSSELL; NORVIG, 2010, p. 236).

## 3. O Mundo do Wumpus como Exemplo de Ambiente

Para ilustrar o funcionamento de um agente lógico, Russell e Norvig (2010, p. 236) introduzem um ambiente simples, mas desafiador: o **Mundo do Wumpus**. Este ambiente, geralmente representado como uma grade de quadrados, contém um Wumpus (um monstro que come quem entrar em seu quadrado), poços (que matam quem cair neles) e ouro (o objetivo do agente). O agente tem sensores limitados:

*   **Brisa**: Sentida em quadrados adjacentes a um poço.
*   **Fedor**: Sentido em quadrados adjacentes ao Wumpus.
*   **Brilho**: Sentido no quadrado que contém o ouro.
*   **Batida**: Sentida ao bater em uma parede.
*   **Grito**: Ouvido quando o Wumpus morre.

O ambiente do Wumpus é caracterizado como **discreto, estático e de agente único**, mas também é **parcialmente observável**, pois o agente não pode ver diretamente a localização dos poços ou do Wumpus, apenas seus efeitos indiretos (RUSSELL; NORVIG, 2010, p. 237).

A partir dos perceptos, o agente usa seu raciocínio lógico para inferir informações sobre o ambiente e tomar decisões seguras. Por exemplo, se o agente está no quadrado e não sente brisa nem fedor, ele pode inferir que os quadrados adjacentes e são seguros (RUSSELL; NORVIG, 2010, p. 238). Uma propriedade fundamental do raciocínio lógico, crucial para o agente do Wumpus, é que **as conclusões são garantidas como corretas se as informações iniciais forem corretas** (RUSSELL; NORVIG, 2010, p. 240).

## 4. Elementos da Lógica Proposicional

A **lógica proposicional** é uma das linguagens lógicas mais simples, mas já permite ilustrar todos os conceitos básicos da lógica (RUSSELL; NORVIG, 2010, p. 243).

### 4.1. Sintaxe
A **sintaxe** da lógica proposicional define as sentenças permitidas. Ela é composta por:
*   **Símbolos de proposição**: Representam proposições que podem ser verdadeiras ou falsas (ex: `P1,2`, `B2,1`, `WumpusAlive`). Existem também `True` (sempre verdadeiro) e `False` (sempre falso) (RUSSELL; NORVIG, 2010, p. 244).
*   **Conectivos lógicos**: Permitem construir sentenças complexas a partir de sentenças mais simples, utilizando parênteses. Os conectivos são:

    *   `¬` (negação)
    *   `∧` (conjunção)
    *   `∨` (disjunção)
    *   `⇒` (implicação)
    *   `⇔` (bicondicional)

### 4.2. Semântica
A **semântica** de uma linguagem lógica define o significado das sentenças, ou seja, como a verdade de uma sentença é determinada (RUSSELL; NORVIG, 2010, p. 243). Na lógica proposicional, isso é feito através de **modelos**. Um modelo é uma atribuição de valores de verdade (verdadeiro/falso) para cada símbolo de proposição (RUSSELL; NORVIG, 2010, p. 245). Por exemplo, para um pequeno conjunto de símbolos, podemos listar todos os 2^n possíveis modelos. Uma sentença é verdadeira em um modelo se a atribuição de valores de verdade a seus símbolos resulta em "verdadeiro" de acordo com as regras dos conectivos lógicos.

Russell e Norvig (2010, p. 242) também discutem o conceito de **grounding**, que é a conexão entre os processos de raciocínio lógico e o ambiente real. Nossos sensores criam essa conexão: se o agente detecta um fedor, ele cria uma sentença que afirma "há fedor". Essa sentença, ao ser adicionada à base de conhecimento, passa a ser considerada verdadeira no mundo real.

### 4.3. Entailment
O conceito de **entailment** (implicação lógica) é central para o raciocínio. Uma sentença `α` é *entailed* por uma base de conhecimento `KB` (escrito `KB |= α`) se `α` é verdadeira em todos os modelos em que `KB` é verdadeira (RUSSELL; NORVIG, 2010, p. 247). Isso significa que se tudo na `KB` for verdade, então `α` também deve ser verdade. O objetivo dos algoritmos de inferência é determinar se `KB |= α`.

## 5. Processos de Inferência

A inferência é o processo de derivar novas sentenças a partir da base de conhecimento. Para agentes lógicos, essa é a capacidade de "pensar" e tirar conclusões.

### 5.1. Model Checking
Uma forma direta de verificar o *entailment* é o **model checking**. Isso envolve enumerar todos os modelos possíveis, e para cada modelo em que a KB é verdadeira, verificar se a sentença `α` também é verdadeira (RUSSELL; NORVIG, 2010, p. 247). O algoritmo `TT-ENTAILS?` (Truth-Table Enumeration) faz exatamente isso.

```
function TT-ENTAILS?(KB, alpha) returns true or false
  symbols <- a list of all proposition symbols in KB and alpha
  return TT-CHECK-ALL(KB, alpha, symbols, {})

function TT-CHECK-ALL(KB, alpha, symbols, model) returns true or false
  if EMPTY?(symbols) then
    if PL-TRUE?(KB, model) then return PL-TRUE?(alpha, model)
    else return true // KB is false in this model, so it doesn't matter
  else
    P <- FIRST(symbols)
    rest <- REST(symbols)
    return TT-CHECK-ALL(KB, alpha, rest, model UNION {P=true}) and
           TT-CHECK-ALL(KB, alpha, rest, model UNION {P=false})
```
*Pseudocódigo adaptado de Russell e Norvig (2010, p. 249).*

A desvantagem do model checking é sua **complexidade exponencial** no número de símbolos de proposição (2^n) (RUSSELL; NORVIG, 2010, p. 248). Para ambientes com muitos símbolos, como um Mundo do Wumpus maior, isso se torna impraticável.

### 5.2. Encadeamento Direto (Forward Chaining)
O encadeamento direto (ou *forward chaining*) é um método de inferência que funciona aplicando regras de inferência (como Modus Ponens) de forma exaustiva para derivar todas as novas sentenças possíveis a partir da KB (RUSSELL; NORVIG, 2010, p. 157). Ele começa com os fatos conhecidos e adiciona todas as conclusões que podem ser inferidas diretamente. É completo para bases de conhecimento em **forma de cláusula de Horn**, o que significa que se uma sentença é *entailed* pela KB, o encadeamento direto a encontrará (RUSSELL; NORVIG, 2010, p. 157).

### 5.3. Encadeamento Reverso (Backward Chaining)
O encadeamento reverso (ou *backward chaining*) é uma estratégia de inferência orientada a objetivos. Ele começa com a consulta que se deseja provar e procura por sentenças na KB que possam concluir essa consulta. Se essas sentenças dependem de outras, o processo continua recursivamente até que todas as premissas sejam fatos conhecidos na KB ou possam ser provadas. Como visto nos slides da disciplina, a inferência em redes Bayesianas pode ser realizada tanto de forma causal (predição) quanto diagnóstica (inferindo causas a partir de efeitos), o que tem uma semelhança conceitual com o encadeamento direto e reverso, respectivamente (FGA0221 – Inteligência Artificial, s.d., Regra de Bayes, slide 12).

### 5.4. Inferência por Refutação (DPLL)
A inferência por refutação busca provar que `KB |= α` mostrando que `KB ∧ ¬α` é insatisfazível (uma contradição). O algoritmo **DPLL (Davis–Putnam–Logemann–Loveland)** é um método eficiente para verificar a satisfatibilidade de sentenças na lógica proposicional (RUSSELL; NORVIG, 2010, p. 263). Ele combina backtracking com heurísticas para podar o espaço de busca, como a **propagação de unidades** (RUSSELL; NORVIG, 2010, p. 264).

```
function DPLL(clauses, symbols, model) returns true or false
  if every clause in clauses is true in model then return true
  if some clause in clauses is false in model then return false
  
  // Find a pure symbol (always appears with same truth value)
  P, value <- FIND-PURE-SYMBOL(clauses, symbols, model)
  if P is not null then
    return DPLL(clauses, symbols - {P}, model UNION {P=value})
  
  // Find a unit clause (clause with only one literal whose truth value is not determined)
  P, value <- FIND-UNIT-CLAUSE(clauses, symbols, model)
  if P is not null then
    return DPLL(clauses, symbols - {P}, model UNION {P=value})
  
  P <- FIRST(symbols)
  rest <- REST(symbols)
  return DPLL(clauses, rest, model UNION {P=true}) or
         DPLL(clauses, rest, model UNION {P=false})
```
*Pseudocódigo adaptado de Russell e Norvig (2010, p. 264).*

## 6. Pseudocódigos e Exemplo de Agente Híbrido

O livro de Russell e Norvig (2010) apresenta pseudocódigos importantes para a compreensão dos agentes lógicos. Além do `KB-AGENT` e do `DPLL` já citados, um exemplo interessante é o `HYBRID-WUMPUS-AGENT`, que mostra como um agente pode combinar a dedução de aspectos do estado do mundo com regras de condição-ação e algoritmos de resolução de problemas (RUSSELL; NORVIG, 2010, p. 269).

```
function HYBRID-WUMPUS-AGENT(percept) returns an action
  persistent: KB, a knowledge base
              t, a counter, initially 0, indicating time
              plan, an action sequence, initially empty
              safe_squares, a set of squares known to be safe
              unvisited_squares, a set of squares not yet visited

  // Update knowledge base
  TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
  TELL(KB, MAKE-ACTION-SENTENCE(last_action, t - 1)) // If applicable

  // Deduce new facts (using logical inference, e.g., DPLL for queries)
  // For each square [x,y]:
  //   Infer if it is safe, infer if it has a pit, infer if it has wumpus, etc.
  //   Add these inferences to KB (e.g., TELL(KB, OKx,y), TELL(KB, ¬Px,y), etc.)
  
  // Update safe and unvisited squares based on new inferences

  // If there's no current plan or it's completed
  if plan is empty then
    // 1. Try to find gold
    if ASK(KB, HAS-GLITTER(current_location, t)) then
      action <- GRAB
    // 2. Try to move to an unvisited safe square
    else if unvisited_safe_square exists then
      plan <- ROUTE-PROBLEM(current_location, unvisited_safe_square, safe_squares)
      action <- FIRST(plan)
      plan <- REST(plan)
    // 3. Try to move to a previously visited safe square (explore more)
    else if visited_safe_square exists then
      plan <- ROUTE-PROBLEM(current_location, visited_safe_square, safe_squares)
      action <- FIRST(plan)
      plan <- REST(plan)
    // 4. No safe moves, shoot or climb out
    else if ASK(KB, HAS-WUMPUS(current_location, t)) and HAS-ARROW() then
      action <- SHOOT
    else
      action <- CLIMB_OUT
  else
    action <- FIRST(plan)
    plan <- REST(plan)

  last_action <- action
  return action
```
*Pseudocódigo adaptado de Russell e Norvig (2010, p. 269-270).*

Este pseudocódigo demonstra como um agente pode usar a lógica proposicional para inferir o estado do mundo e, em seguida, combinar essa informação com um algoritmo de busca (`ROUTE-PROBLEM` e `A*-GRAPH-SEARCH` seriam definidos separadamente) para planejar uma rota, garantindo que suas ações sejam baseadas no conhecimento mais seguro possível.

## 7. Limitações dos Agentes Lógicos e Necessidade de Agentes Probabilísticos

Apesar de sua elegância e rigor, a lógica proposicional, e os agentes puramente lógicos baseados nela, possuem limitações significativas em ambientes complexos e incertos.

**1. Problema da Qualificação**: Como discutido nos slides da disciplina (FGA0221 – Inteligência Artificial, s.d., Quantificando Incertezas, slide 2), é extremamente difícil listar todas as qualificações necessárias para que uma regra lógica seja totalmente exaustiva e sem exceções. Por exemplo, "Dor de dente ⇒ Cárie" é uma regra falha, e tentar adicionar todas as exceções a ela torna a base de conhecimento impraticável (RUSSELL; NORVIG, 2010, p. 268, 480). Russell e Norvig (2010, p. 369) reforçam essa ideia, mencionando que a lógica proposicional é impraticável para domínios complexos como o diagnóstico médico devido à necessidade de uma listagem exaustiva de antecedentes e consequentes.

**2. Expressividade Limitada para Ambientes de Tamanho Ilimitado**: A lógica proposicional carece de poder expressivo para lidar concisamente com tempo, espaço e padrões universais de relacionamento entre objetos (RUSSELL; NORVIG, 2010, p. 273, 134). Por exemplo, expressar "se há um poço em [x,y], então há uma brisa em [x-1,y], [x+1,y], [x,y-1] e [x,y+1]" de forma universal para qualquer `x` e `y` é impossível na lógica proposicional sem escrever uma sentença separada para cada quadrado. Isso leva a bases de conhecimento com milhões de sentenças em ambientes maiores, tornando-as impraticáveis (RUSSELL; NORVIG, 2010, p. 273).

**3. Lidar com a Incerteza**: A principal limitação, como bem destacado nos slides (FGA0221 – Inteligência Artificial, s.d., Quantificando Incertezas, slide 1), é que agentes no mundo real precisam lidar com a incerteza devido à observabilidade parcial, não determinismo ou adversidades. Agentes lógicos puros lidam com a incerteza acompanhando todos os estados de mundo possíveis, mas isso pode levar a planos de contingência que crescem arbitrariamente, considerando eventualidades improváveis (FGA0221 – Inteligência Artificial, s.d., Quantificando Incertezas, slide 1). Em muitos casos, não há um plano que garanta o sucesso, e o agente precisa comparar os méritos de planos não garantidos (FGA0221 – Inteligência Artificial, s.d., Quantificando Incertezas, slide 1).

Para superar essas limitações, a Inteligência Artificial evoluiu para abordagens que quantificam a incerteza. Como vimos em sala, a **teoria da probabilidade** fornece a principal ferramenta para lidar com graus de crença, permitindo que um agente tenha um grau numérico de crença entre 0 e 1 em uma sentença, resolvendo assim o problema da qualificação (FGA0221 – Inteligência Artificial, s.d., Quantificando Incertezas, slide 4, 5). Russell e Norvig (2010, p. 481) também mencionam que a teoria da probabilidade permite que o agente tenha um "grau de crença" nos resultados.

Além disso, para aprimorar a expressividade, foi desenvolvida a **Lógica de Primeira Ordem**, que permite representar conhecimento sobre objetos e relações de forma muito mais concisa e universal (RUSSELL; NORVIG, 2010, p. 285). Essa transição para a lógica de primeira ordem e, posteriormente, para o raciocínio probabilístico com **Redes Bayesianas** (como as discutidas nos slides FGA0221 – Inteligência Artificial, s.d., Redes Bayesianas, slides 1-3), é essencial para a construção de agentes verdadeiramente robustos em ambientes complexos. As redes Bayesianas, por exemplo, oferecem um método sistemático para representar relações de independência condicional explicitamente e realizar inferência probabilística de forma eficiente (RUSSELL; NORVIG, 2010, p. 510).

Em suma, embora os agentes lógicos forneçam uma base sólida para a representação do conhecimento e o raciocínio dedutivo, a complexidade e a incerteza do mundo real exigem a integração com ferramentas mais poderosas, como a lógica de primeira ordem e a teoria da probabilidade, que serão exploradas em detalhes nos próximos tópicos do portfólio.

---

## Referências

FGA0221 – Inteligência Artificial. (s.d.). *Quantificando Incertezas*. Slides da disciplina.

FGA0221 – Inteligência Artificial. (s.d.). *Quantificando Incertezas – 2ª Parte*. Slides da disciplina.

FGA0221 – Inteligência Artificial. (s.d.). *Redes Bayesianas*. Slides da disciplina.

RUSSELL, S. J.; NORVIG, P. *Artificial Intelligence: A Modern Approach*. 3. ed. Upper Saddle River: Prentice Hall, 2010.

---

| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 24/06/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |
