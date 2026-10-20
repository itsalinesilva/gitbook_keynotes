# AI Engineering Release Checklist

## Problem and architecture
- [ ] AI System Brief approved; baseline and non-AI alternative recorded.
- [ ] Solution class justified: deterministic, ML, LLM, RAG, agent or hybrid.
- [ ] Quality attributes, SLOs, risk class, owner and source of truth defined.
- [ ] ADR documents options and trade-offs.

## Data and retrieval
- [ ] Rights, provenance, freshness, ACL and retention defined.
- [ ] Data contracts and ingestion validation automated.
- [ ] Retrieval evals cover lexical, semantic, hybrid and metadata filters as relevant.
- [ ] Citation/claim traceability tested; unsupported claims can be abstained.

## Model and agent
- [ ] Model/provider/prompt/skill/tool/index versions captured.
- [ ] Structured outputs validated against schemas and domain invariants.
- [ ] Agent loops have max iterations, deadline, token/cost budgets and stop criteria.
- [ ] Tools have least privilege, schema validation, idempotency and audit.
- [ ] Untrusted retrieved content cannot modify policies or permissions.

## Quality and safety
- [ ] Unit, contract, integration, end-to-end and regression tests run.
- [ ] Evals include representative, edge, adversarial and segment-specific cases.
- [ ] Human judge calibration and LLM-as-judge limitations documented.
- [ ] Threat model includes injection, data leakage, tool abuse, supply chain and denial of service.
- [ ] Human approval gates defined for material external or irreversible actions.

## Production readiness
- [ ] Traces, logs, metrics, costs and redaction tested.
- [ ] Timeout, bounded retry, circuit breaker, dedupe and dead-letter behavior tested.
- [ ] Alert thresholds, runbooks, incident owner and rollback tested.
- [ ] Canary/shadow release and stop criteria defined.
- [ ] Post-release review and feedback loop scheduled.
