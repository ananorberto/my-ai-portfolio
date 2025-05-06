# Agentes Inteligentes

Um agente de IA é qualquer sistema capaz de **perceber seu ambiente** por meio de sensores e **agir sobre ele** através de atuadores. Ele pode ser algo físico (como um robô) ou virtual (como um assistente digital).

Segundo **Russell e Norvig (2022)**, o conceito de agente é central na IA moderna. Toda a estrutura de raciocínio e tomada de decisão parte da ideia de que o agente interage continuamente com o ambiente, tentando atingir seus objetivos com base nas informações que coleta.

## Tipos de agentes

A forma como os agentes tomam decisões varia de acordo com sua complexidade e capacidade de adaptação. A seguir, estão os principais tipos:

### Agentes de Reflexo Simples

- Agem com base em regras fixas do tipo *se–então*.
- Não possuem memória nem aprendizado.
- Exemplo: um termostato que liga o ar-condicionado quando a temperatura passa de 26 °C.

### Agentes de Reflexo Baseado em Modelo

- Mantêm um modelo interno do ambiente.
- Conseguem lidar com situações mais complexas, mesmo sem observar todo o estado atual.
- Exemplo: um aspirador robótico que mapeia a sala para decidir para onde ir.

### 🎯 Agentes Baseados em Objetivos

- Agem para atingir metas específicas.
- São capazes de escolher entre diferentes ações avaliando qual aproxima mais do objetivo.
- Exemplo: um aplicativo de GPS que calcula a melhor rota.

### 📈 Agentes Utilitários

- Vão além dos objetivos: também consideram **a melhor forma** de atingi-los.
- Avaliam consequências, preferências e desempenho.
- Exemplo: um sistema de investimentos que busca maximizar lucros e minimizar riscos.

### 🧬 Agentes com Aprendizado (Learning Agents)

- Melhoram sua performance ao longo do tempo com base na experiência.
- Podem ajustar internamente seus componentes e regras.
- Exemplo: redes neurais que ajustam seus pesos com base em dados históricos.

> Esses tipos não são mutuamente exclusivos. Um agente pode, por exemplo, ser baseado em objetivos e também aprender com a experiência.

---

## Ambientes em IA

O ambiente é o **contexto** onde o agente está inserido. É ele que determina **o que o agente pode ou não perceber**, **quais ações estão disponíveis** e **como elas impactam o mundo ao redor**.

Conforme Russell e Norvig (2022), a maneira como o ambiente é estruturado influencia diretamente no tipo de agente que pode ser construído.

### Classificações de ambiente

| Dimensão                   | Explicação                                                                 | Exemplo                                                                 |
|---------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Observabilidade**       | Totalmente observável / Parcialmente / Não observável                      | Xadrez (totalmente), pôquer (parcial), robô em espaço desconhecido (não) |
| **Número de agentes**     | Agente único ou multiagente                                                 | Sudoku (único), jogos online (multiagente)                              |
| **Determinismo**          | Determinístico ou não determinístico                                        | Jogo de damas (determinístico), mercado financeiro (não determinístico) |
| **Temporalidade**         | Episódico ou sequencial                                                     | Diagnóstico médico (episódico), redes sociais (sequencial)              |
| **Dinamicidade**          | Estático ou dinâmico                                                        | Quebra-cabeça offline (estático), trânsito urbano (dinâmico)            |
| **Natureza do estado**    | Discreto ou contínuo                                                        | Tabuleiro (discreto), controle de um drone (contínuo)                   |
| **Conhecimento do agente**| Conhecido ou desconhecido                                                   | Regras de um jogo (conhecido), interesses de um usuário no YouTube (desconhecido) |

Cada uma dessas características exige abordagens diferentes na hora de projetar um agente eficiente. Por exemplo, ambientes parcialmente observáveis geralmente pedem agentes que consigam manter um modelo interno do estado, enquanto ambientes dinâmicos exigem resposta rápida e atualização constante das percepções.

---

## Considerações finais

Entender o que são agentes e como funcionam os ambientes onde eles atuam é essencial para projetar sistemas de IA inteligentes e eficientes. Os agentes representam **o "como" a IA age**, enquanto os ambientes representam **o "onde" e "com que restrições"** essa ação acontece.

Combinar essas duas visões — comportamento interno do agente e características externas do ambiente — permite desenvolver soluções mais **adaptáveis, robustas e eficazes**. E, como mostram as referências, essa interação é a base de praticamente todas as aplicações modernas de Inteligência Artificial.

---

## Referências

- Russell, S., & Norvig, P. (2022). *Artificial Intelligence: A Modern Approach* (4ª ed.). Pearson.  
- Marsland, S. (2015). *Machine Learning: An Algorithmic Perspective* (2ª ed.). CRC Press.  
- Notas de aula da disciplina FGA0221 – Inteligência Artificial, Universidade de Brasília (2025/1).

---

### Histórico de versão

| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 06/05/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

