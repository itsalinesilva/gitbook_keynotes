# Contratos entre componentes

## Regras globais
- Todo objeto de execução contém `schema_version`, `run_id`, `created_at`, `actor_id` e `correlation_id`.
- IDs são estáveis e não contêm informação pessoal.
- Datas usam ISO 8601 UTC.
- Estados são enums versionados; nunca inferir sucesso a partir da ausência de erro.
- Valores desconhecidos são `unknown`/`null`, não inventados.
- Campos de confiança precisam declarar método e calibração; não usar confiança verbal do modelo como probabilidade calibrada.
- Artefatos devem incluir versão de prompt, modelo, ferramentas, corpus e configuração relevantes.
- Erros são tipados, redigidos para não expor segredos e classificados como retryable ou terminal.

## Entidades principais
1. `TaskEnvelope`: solicitação, restrições, prazo, risco, critérios de aceite.
2. `Plan`: subtarefas, dependências, orçamento, condição de parada.
3. `ToolCall`: nome, versão, argumentos tipados, permissão, timeout e idempotency key.
4. `SourceRecord`: identidade, URL canônica, tipo, autoria, datas, confiabilidade, direitos/uso.
5. `EvidenceRecord`: trecho, localização, hash, fonte, data de captura e relevância.
6. `ClaimRecord`: afirmação, tipo (fact/inference/hypothesis), evidências e estado de revisão.
7. `EvaluationResult`: suíte, versão, métricas, limites, falhas e decisão.
8. `ArtifactManifest`: arquivos, hashes, fontes, versões e aprovadores.
9. `MemoryProposal`: proposta, evidência, escopo, expiração, aprovador e status.
10. `IncidentRecord`: impacto, timeline, causa, mitigação, ações preventivas.

## Compatibilidade
- Mudança aditiva opcional: minor.
- Alteração semântica ou obrigatória: major.
- Correção que não muda contrato: patch.
- Consumidores devem rejeitar versões incompatíveis explicitamente.
