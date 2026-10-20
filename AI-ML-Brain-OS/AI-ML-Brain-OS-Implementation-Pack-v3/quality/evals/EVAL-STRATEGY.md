# Estratégia de avaliação

Nenhuma métrica única representa a qualidade de um sistema de IA. Usar um portfólio de testes, com métricas alinhadas à tarefa.

## Camadas
1. **Determinística**: schemas, tipos, invariantes, permissões, parsing e regras de negócio.
2. **Golden set**: exemplos representativos e casos difíceis rotulados por especialistas.
3. **Model-graded**: avaliador com rubrica explícita, calibrado contra julgamentos humanos.
4. **Human review**: decisões ambíguas, alto impacto, qualidade editorial e trade-offs.
5. **Adversarial**: prompt injection, fontes maliciosas, instruções conflitantes, tool misuse, dados contaminados.
6. **Production monitoring**: feedback, taxa de abstenção, custo, latência, drift, erros e resultados downstream.

## Métricas possíveis
- Retrieval: recall@k, precision@k, MRR, nDCG, taxa de evidência relevante.
- RAG: faithfulness/groundedness, relevância, cobertura de fontes, correção de citações, abstenção adequada.
- Agentes: task success, tool selection accuracy, schema validity, loops, escalonamento correto, custo por tarefa.
- Pesquisa: cobertura de fontes primárias, claims suportados, contraevidência, frescor, diversidade geográfica e independência das fontes.
- ML preditivo: métricas de tarefa, calibração, fairness, robustez, drift, latência e custo.
- Operação: disponibilidade, taxa de falha, retries, MTTR, custo por workflow.

## Regras
- Fixar versão do dataset e rubric.
- Incluir casos negativos e casos em que a resposta correta é abster-se.
- Separar tuning set de holdout.
- Medir por subgrupo/idioma quando pertinente.
- Avaliar mudanças de modelo, prompt, retrieval, corpus e ferramentas como mudanças independentes quando possível.
- Guardar exemplos de falha, não apenas score agregado.
- Não promover com base em um LLM-as-judge isolado.
