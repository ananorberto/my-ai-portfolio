# 1. Introdução ao Portfólio de Aprendizado de Máquina

Este portfólio marca o encerramento da disciplina de Inteligência Artificial e tem como foco principal o **Aprendizado de Máquina (Machine Learning)** — uma das áreas mais empolgantes e transformadoras dentro da IA. Ao longo do semestre, vimos em aula que o aprendizado de máquina permite que agentes se tornem mais inteligentes ao aprenderem com dados e experiências, em vez de dependerem apenas de regras fixas programadas manualmente.

Como discutido nos slides e nas aulas, essa capacidade é fundamental para que sistemas atuem em situações imprevisíveis ou muito complexas para que um programador especifique todas as possibilidades. Russell e Norvig (2010, p. viii) destacam exatamente esse ponto, ao explicar que o aprendizado permite que agentes operem de forma autônoma em ambientes que seus projetistas não conseguem antecipar completamente, como no caso de robôs explorando outros planetas ou sistemas de recomendação lidando com milhões de usuários.

Neste portfólio, organizei três projetos práticos que representam os principais tipos de aprendizado que estudamos:

* **Aprendizado Supervisionado**
* **Aprendizado Não Supervisionado**
* **Aprendizado por Reforço**

Cada um desses projetos foi pensado para ilustrar como diferentes abordagens de aprendizado ajudam agentes a extrair conhecimento, tomar decisões e melhorar seu desempenho com o tempo.

O **aprendizado supervisionado**, por exemplo, é aquele em que o agente aprende a partir de exemplos com respostas corretas (rótulos). Como foi mostrado nos slides, esse tipo de aprendizado é usado em tarefas como classificação (ex: prever se vai chover ou não) ou regressão (ex: estimar a temperatura). Um exemplo que vimos em aula foi a classificação de peixes entre Salmões e Robalos com base em características físicas que é um caso clássico explicado também por Russell e Norvig (2010, p. 727), que mencionam ainda o uso de redes neurais artificiais nesse contexto.

Já no **aprendizado não supervisionado**, o agente não recebe rótulos ou respostas corretas. Em vez disso, ele tenta identificar padrões e estruturas escondidas nos dados. Isso pode ser feito por meio de **agrupamento** (clustering) ou **transformações de dados**, como vimos nos códigos e nos exemplos práticos em aula. Embora mais desafiador de avaliar, esse tipo de aprendizado é muito útil quando não temos dados rotulados disponíveis, o que é bem comum no mundo real.

Por fim, o **aprendizado por reforço** é talvez o mais interessante de todos, porque simula a forma como muitos seres vivos aprendem: por tentativa e erro. O agente recebe recompensas ou punições com base em suas ações, e com isso aprende a agir de forma mais eficaz ao longo do tempo. Como vimos nos slides e nos exemplos com Q-Learning, esse tipo de aprendizado é especialmente importante para situações em que o agente precisa aprender a explorar um ambiente sem conhecer todas as regras de antemão. Russell e Norvig (2010, p. 102) descrevem esse tipo de aprendizado como uma miniatura do problema geral da IA, o que mostra o quanto ele é fundamental.

Ao longo deste portfólio, vou apresentar os três projetos com explicações, trechos de código e reflexões sobre como essas abordagens contribuem para tornar agentes mais inteligentes. Foi um desafio desenvolver cada um deles, mas também uma ótima forma de consolidar tudo que aprendi ao longo da disciplina.

---

### Referências

RUSSELL, Stuart J.; NORVIG, Peter. *Artificial Intelligence: A Modern Approach*. 3. ed. Upper Saddle River: Pearson Education, Inc., 2010.
SOARES, Fabiano. *Slides FGA0221 – Inteligência Artificial*. \[s.l.]: \[s.n.], \[2025?].

---

| Versão | Data       | Modificação          | Nome                 | GitHub                                         |
| ------ | ---------- | -------------------- | -------------------- | ---------------------------------------------- |
| `1.0`  | 27/07/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

