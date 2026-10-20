
# Roadmap de implementação — 12 semanas de referência

O cronograma é indicativo. Ajustar ao tamanho da equipe, requisitos, dependências, risco e maturidade atual.

## Fase 0 — Descoberta e inventário (semana 1)
**Entregas:** inventário do que existe; objetivos e stakeholders; mapa de dados; riscos; baseline de qualidade/custo/latência.
**Gate:** não iniciar migração sem identificar sistemas e fontes de verdade.

## Fase 1 — Contratos e arquitetura (semanas 2–3)
**Entregas:** System Brief, schemas, ADRs, classificação de risco, matriz de permissões, desenho de estado.
**Gate:** contratos revisados e exemplos validados.

## Fase 2 — Vertical slice mínimo (semanas 4–5)
**Entregas:** um fluxo de intake → retrieval → evidências → síntese → avaliação → artefato; logging e limites.
**Gate:** casos básicos e negativos passam; nenhuma ação externa automática.

## Fase 3 — Knowledge & evidence (semanas 6–7)
**Entregas:** source registry, ingestão versionada, deduplicação, índices, ledger de claims/evidências, política de frescor.
**Gate:** benchmark de retrieval e citação atinge limites definidos.

## Fase 4 — Orquestração durável (semanas 8–9)
**Entregas:** estado persistente, retries idempotentes, cancelamento, checkpoints, quotas, roteamento especializado limitado.
**Gate:** recuperação de falha e orçamento testados.

## Fase 5 — Segurança, avaliação e rollout (semanas 10–11)
**Entregas:** threat model, red team, golden set, traces, dashboards, runbooks, aprovação humana por risco.
**Gate:** quality gates completos e rollback testado.

## Fase 6 — Piloto e melhoria (semana 12)
**Entregas:** rollout controlado, feedback estruturado, métricas de produto, backlog de falhas e roadmap seguinte.
**Gate:** decisão explícita de ampliar, manter, reduzir ou descontinuar.

## Ordem de prioridade
1. Contratos e proveniência.
2. Segurança e limites de execução.
3. Avaliação e observabilidade.
4. Retrieval e qualidade do conhecimento.
5. Orquestração complexa e multiagentes.
6. Personalização, memória avançada e otimização de custo.

## Métricas de saída
- % claims relevantes com evidência rastreável.
- Precisão de citações e taxa de resposta sem suporte.
- Taxa de conclusão por classe de tarefa.
- Taxa de intervenção humana e acerto do escalonamento.
- Custo por tarefa útil e latência p50/p95.
- Taxa de falha, repetição e recuperação.
- Incidentes de permissão/segurança.
- Frequência de regressões detectadas antes da produção.
