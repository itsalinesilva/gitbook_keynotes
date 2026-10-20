
# Quality gates e política de promoção

## Gate 0 — Especificação
- Objetivo, usuário, escopo e fora de escopo explícitos.
- Critérios de aceitação mensuráveis.
- Risco e classificação de dados definidos.
- Dono e plano de rollback atribuídos.

## Gate 1 — Contratos
- Schemas validados.
- Estados de sucesso, falha, timeout, cancelamento e inconclusão definidos.
- Compatibilidade de versões testada.
- Chamadas de ferramentas têm limites e validação.

## Gate 2 — Qualidade funcional
- Unit tests e contract tests aprovados.
- Golden dataset e regressão avaliados.
- Métricas mínimas atingidas.
- Claims críticos possuem evidências rastreáveis.
- Não há afirmações inventadas em testes de referência.

## Gate 3 — Segurança e privacidade
- Threat model revisado.
- Testes de prompt injection e exfiltração.
- Controle de permissões validado.
- Segredos não aparecem em logs/artefatos.
- Retenção, acesso e exclusão documentados.

## Gate 4 — Operabilidade
- Traces correlacionados por run_id.
- Alertas e dashboards funcionam.
- Limites de custo, latência, retries e concorrência definidos.
- Runbooks e responsável de incidente atribuídos.
- Teste de recuperação/rollback concluído.

## Gate 5 — Release
- Revisão humana conforme risco.
- Versões de modelo, prompt, ferramentas e corpus registradas.
- Canary/shadow ou rollout progressivo quando apropriado.
- Critérios de interrupção e rollback configurados.

## Gate 6 — Pós-release
- Monitoramento de qualidade, drift, custo e feedback.
- Revisão periódica de fontes, permissões e memória.
- Incidentes e falhas alimentam testes de regressão.
- Descontinuação e migração têm plano.

## Política de bloqueio
Falha crítica de segurança, violação de permissão, regressão acima do limite ou falta de proveniência em claim de alto impacto bloqueia a promoção.



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



# Definition of Done — sistema IA/ML

Um componente só pode ser considerado pronto quando:
- [ ] Problema, owner, fronteiras e critérios de aceitação documentados.
- [ ] Contratos e schemas versionados e testados.
- [ ] Testes unitários, de integração, contrato e falha executados.
- [ ] Golden set/evals relevantes executados e resultados registrados.
- [ ] Segurança, privacidade e permissões revisadas.
- [ ] Limites de custo, tempo, concorrência e passos definidos.
- [ ] Telemetria e redaction validadas.
- [ ] Runbook, alertas, rollback e responsável operacional definidos.
- [ ] Dependências e versões registradas.
- [ ] Limitações e modos de falha conhecidos documentados.
- [ ] Aprovação humana obtida quando o risco exige.
- [ ] Mudanças relevantes possuem ADR e changelog.
