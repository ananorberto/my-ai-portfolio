
# Introdução aos Agentes Lógicos na Inteligência Artificial

A Inteligência Artificial (IA) é um campo muito vasto intrigante, cujo objetivo principal é estudar e construir **agentes inteligentes** capazes de perceber o ambiente e realizar ações (Russell & Norvig, 2010, p. 5). Dentre as diversas abordagens para se alcançar a inteligência artificial, a dos **agentes lógicos** se destaca por focar na capacidade de um agente de raciocinar sobre o conhecimento. Para mim, o mais interessante é como essa abordagem permite que os agentes formem representações complexas do mundo, utilizem processos de inferência para derivar novas informações e, a partir delas, deduzam a melhor forma de agir.

A história dos agentes lógicos remonta a raízes profundas na filosofia. Tudo começou, em certa medida, com **Aristóteles** (384-322 a.C.), que foi o primeiro a formalizar um conjunto de leis que governavam a parte racional da mente, estabelecendo as bases para o raciocínio lógico (Russell & Norvig, 2010, p. 36). Séculos depois, no contexto da IA, um marco importante foi o trabalho de **Warren McCulloch e Walter Pitts** em 1943, que propuseram um modelo de neurônios artificiais baseado na lógica proposicional (Russell & Norvig, 2010). Posteriormente, **Allen Newell e Herbert Simon** apresentaram o Logic Theorist (LT) em 1956, um dos primeiros programas de raciocínio, e as contribuições de **John McCarthy** em 1958, com a linguagem Lisp e a concepção do Advice Taker, foram cruciais. McCarthy defendia a ideia central de ter uma representação formal e explícita do mundo e a capacidade de manipulá-la com processos dedutivos, inaugurando o que se conhece como a **abordagem declarativa** para a construção de sistemas (Russell & Norvig, 2010).

A principal característica de um agente lógico é sua **Base de Conhecimento (KB)**, que é um conjunto de sentenças expressas em uma linguagem de representação de conhecimento (Russell & Norvig, 2010, p. 118, 133). O agente interage com essa base de conhecimento por meio de duas operações fundamentais: **TELL**, que informa à KB o que o agente percebe ou as ações que executa, e **ASK**, que consulta a KB para determinar qual ação deve ser realizada (Russell & Norvig, 2010, p. 119). Para ilustrar esses conceitos, Russell e Norvig (2010) apresentam o **Mundo do Wumpus**, um ambiente simples que permite demonstrar como um agente lógico pode inferir informações (como a localização de poços ou do Wumpus) a partir de seus perceptos (brisa, fedor), garantindo que as conclusões são corretas se as informações iniciais também forem, uma propriedade fundamental do raciocínio lógico (Russell & Norvig, 2010).

No entanto, a complexidade do mundo real logo impõe desafios a esses agentes puramente lógicos. Algo que me chamou a atenção, e que é reforçado pelos slides da disciplina, é que **agentes no mundo real precisam lidar com a incerteza**, seja por observabilidade parcial, não determinismo ou adversidades (FGA0221 – IA, s.d.). Assim como visto em sala, os agentes lógicos e solucionadores de problemas, tendem a lidar com a incerteza acompanhando todos os estados de mundo possíveis, o que pode levar a um crescimento arbitrário dos planos de contingência (FGA0221 – IA, s.d.). Russell e Norvig (2010, p. 369, 370) reforçam essa ideia ao afirmar que tentar usar a lógica proposicional para domínios complexos, como o diagnóstico médico, é impraticável devido à necessidade de listar um conjunto exaustivo de antecedentes e consequentes (o **problema da qualificação**), e à ignorância teórica e prática inerente a esses domínios. A lógica proposicional, por si só, não tem expressividade suficiente para ambientes de tamanho ilimitado, como o tempo, o espaço e os padrões universais (Russell & Norvig, 2010, p. 134).

Para superar essas limitações, foi possível que a IA evoluiu para integrar a **teoria da probabilidade**. De acordo com o conteúdo da aula, a teoria da probabilidade fornece uma maneira de resumir a incerteza que vem da nossa falta de tempo e ignorância, resolvendo assim o problema da qualificação, ao permitir que o agente tenha um grau numérico de crença entre 0 e 1 (FGA0221 – IA, s.d.). Essa transição é fundamental, e a próxima etapa natural é a utilização da **Lógica de Primeira Ordem**, uma linguagem muito mais poderosa capaz de representar conhecimento de forma mais concisa e expressiva (Russell & Norvig, 2010).

Neste portfólio, pretendo aprofundar a compreensão sobre os agentes lógicos, desde seus fundamentos em lógica proposicional até a necessidade de linguagens mais expressivas. Além disso, explorarei como o raciocínio probabilístico, em particular as **Redes Bayesianas**, se torna uma ferramenta indispensável para lidar com a incerteza, permitindo que os agentes tomem decisões racionais mesmo em ambientes complexos e imprevisíveis.

---

## Referências

FGA0221 – Inteligência Artificial. (s.d.). *Quantificando Incertezas*. Slides da disciplina.

FGA0221 – Inteligência Artificial. (s.d.). *Quantificando Incertezas – 2ª Parte*. Slides da disciplina.

FGA0221 – Inteligência Artificial. (s.d.). *Redes Bayesianas*. Slides da disciplina.

Russell, S. J., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd ed.). Prentice Hall.

---

| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 23/06/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

