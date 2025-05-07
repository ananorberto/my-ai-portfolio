Com certeza! Aqui está a versão aprimorada do seu `.md`, com algumas pequenas expansões e ajustes de estilo para maior fluidez, clareza técnica e reforço dos fundamentos teóricos com base nas referências utilizadas:

---

## Projeto: Sistema de Busca Semântica em Relatórios Policiais sobre Armas Brancas

### Contexto e Relevância

A identificação automática de registros que mencionam **armas brancas** (como facas, canivetes ou machados) em relatórios policiais representa uma contribuição significativa para investigações criminais, inteligência policial e pesquisas acadêmicas sobre violência urbana. Ao automatizar a extração dessas informações em textos não estruturados, como os boletins de ocorrência, é possível melhorar a eficiência na análise de padrões criminais e subsidiar políticas públicas de segurança.

Este ideia nasceu a partir das discussões realizadas na aula do dia **06/05/2025**, em que o professor **Fabiano** apresentou exemplos de aplicação de técnicas de inteligência artificial em dados de segurança pública. Motivada por esse conteúdo, aprofundei uma pesquisa em soluções similares, como as propostas por Tompson et al. \[1], que aplicam mineração de texto em relatórios policiais para identificar padrões de crimes, e por Araújo et al. \[2], que exploram mecanismos de similaridade semântica em documentos policiais.

---

### Conexão com Experiência Prática

Durante a pesquisa observei que a proposta aqui apresentada está alinhada com os conteúdos explorados nos laboratórios da disciplina de **Programação para Sistemas Paralelos e Distribuídos (PSPD)** feitos  no semestre 2024/2. Em especial, destacam-se os experimentos com **pipelines de ingestão, processamento e visualização de dados** utilizando tecnologias como Kafka, Spark e Elasticsearch. Esse conhecimento prático foi essencial para compreender os desafios de escalabilidade e desempenho envolvidos no tratamento de grandes volumes de texto.

Além disso, referências como a de Ladanavar et al. \[3] mostram como arquiteturas semelhantes — combinando pré-processamento textual, embeddings BERT e Elasticsearch — já são aplicadas com sucesso em sistemas de busca semântica, reforçando a viabilidade técnica da nossa abordagem.

---

### Proposta Técnica

Inspirado por abordagens consolidadas em estudos recentes \[2]\[3], o sistema proposto é estruturado em três etapas principais:

1. **Pré-processamento Textual**
   Realiza a limpeza de texto (remoção de stopwords, pontuação irrelevante e padronização de caixa), normalização (lematização e correção ortográfica), e a extração de entidades nomeadas (NER), permitindo identificar automaticamente menções a armas brancas, locais, datas e participantes.

2. **Busca Semântica com Embeddings**
   Emprega o modelo `bert-base-portuguese-cased`, da NeuralMind \[4], para transformar os documentos e as consultas dos usuários em vetores densos. Isso permite capturar a semântica dos textos, mesmo quando diferentes palavras são utilizadas para expressar o mesmo conceito — algo essencial para lidar com a linguagem informal e ambígua dos relatos policiais.

3. **Classificação e Recuperação**
   Os vetores gerados são indexados em uma estrutura compatível com o Elasticsearch, que permite buscas por similaridade de cosseno. Com isso, é possível recuperar os relatórios mais semanticamente próximos à consulta fornecida, mesmo na ausência de termos exatos \[5].

#### Propriedades do Sistema

| Aspecto        | Classificação                 | Justificativa                                |
| -------------- | ----------------------------- | -------------------------------------------- |
| Tipo de Dados  | Texto livre (não estruturado) | Relatórios policiais com linguagem informal  |
| Escalabilidade | Alta                          | Grandes volumes de documentos históricos     |
| Linguagem      | Variada                       | Presença de gírias, siglas e inconsistências |
| Atualização    | Contínua                      | Inclusão frequente de novos relatos          |

---

### Exemplo de Código Usando Elasticsearch + BERT

```python
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

es = Elasticsearch("http://localhost:9200")
model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')

def search_weapons(query, top_k=10):
    query_embedding = model.encode(query)
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'doc_embedding') + 1.0",
                "params": {"query_vector": query_embedding.tolist()}
            }
        }
    }
    response = es.search(index="relatorios_policiais", body={"size": top_k, "query": script_query})
    return [hit["_source"] for hit in response["hits"]["hits"]]
```

---

### Considerações Finais

A aplicação de técnicas de inteligência artificial para análise de documentos textuais não estruturados abre novas perspectivas para a segurança pública. Estudos como os de Tompson et al. \[1], Araújo et al. \[2] e Ladanavar et al. \[3] mostram que já é possível empregar modelos de linguagem como o BERT e motores de busca como o Elasticsearch para extrair conhecimento de relatórios policiais.

Embora desafios como ambiguidade linguística, regionalismos e limitações éticas ainda precisem ser enfrentados, os resultados preliminares são promissores. O uso de ferramentas modernas permite construir soluções funcionais, escaláveis e alinhadas às necessidades reais das autoridades policiais.

---

### Referências Técnicas

**\[1]** TOMPSON, L. et al. *Unsupervised identification of crime problems from police free-text reports*. Crime Science, \[S.l.], v. 9, n. 1, p. 1–15, 2020. DOI: [https://doi.org/10.1186/s40163-020-00127-4](https://doi.org/10.1186/s40163-020-00127-4). Disponível em: [https://link.springer.com/article/10.1186/s40163-020-00127-4](https://link.springer.com/article/10.1186/s40163-020-00127-4). Acesso em: 7 maio 2025.

**\[2]** ARAÚJO, J. A. F. et al. *Police Report Similarity Search: A Case Study*. In: BRAZILIAN CONFERENCE ON INTELLIGENT SYSTEMS (BRACIS), 2023. Anais \[...]. Porto Alegre: SBC, 2023. p. 394-409. Disponível em: [https://sol.sbc.org.br/index.php/bracis/article/view/28428](https://sol.sbc.org.br/index.php/bracis/article/view/28428). Acesso em: 7 maio 2025.

**\[3]** LADANAVAR, S. M. et al. *Enhancing User Query Comprehension and Contextual Relevance with a Semantic Search Engine using BERT and ElasticSearch*. EAI Endorsed Transactions on Internet of Things, \[S.l.], v. 10, 2024. DOI: [https://doi.org/10.4108/eetiot.6993](https://doi.org/10.4108/eetiot.6993). Disponível em: [https://publications.eai.eu/index.php/IoT/article/view/6993](https://publications.eai.eu/index.php/IoT/article/view/6993). Acesso em: 7 maio 2025.

**\[4]** NEURALMIND. *BERTimbau: BERT pré-treinado para o português*. 2020. Disponível em: [https://github.com/neuralmind-ai/portuguese-bert](https://github.com/neuralmind-ai/portuguese-bert). Acesso em: 07 maio 2025.

**\[5]** ELASTICSEARCH. *Elasticsearch: The Definitive Guide*. \[S. l.]: Elastic, 2024. Disponível em: [https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html). Acesso em: 07 maio 2025.

---

### Histórico de versão

| Versão | Data       | Modificação          | Nome                 | GitHub                                         |
| ------ | ---------- | -------------------- | -------------------- | ---------------------------------------------- |
| `1.0`  | 06/05/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

---
