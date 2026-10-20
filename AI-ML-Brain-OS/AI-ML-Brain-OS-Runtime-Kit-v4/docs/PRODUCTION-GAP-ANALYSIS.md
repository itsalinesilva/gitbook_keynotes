# Gap analysis

| Capability | Included in this kit | Remaining for production |
|---|---|---|
| Executable runtime | Yes, deterministic local demo | LLM adapter, durable workflow, auth |
| Tool integration | Registry, echo, bounded HTTPS adapter | Real connectors, secrets, rate limits, policy review |
| Knowledge/memory | SQLite registry, docs, memory proposals | Full ingestion, hybrid/vector retrieval, evidence graph, ACL/retention |
| CI/tests | pytest tests and GitHub Actions workflow | Run CI in target repo, coverage, SAST, integration tests |
| Deploy | Dockerfile and local CLI | Registry, secret injection, rollout/rollback, probes |
| Monitoring/recovery | Structured logs and health check | OpenTelemetry backend, dashboards, alerts, SLOs, incident ownership |
| Runtime security | Allowlist and approval gates | AuthN/Z, tenant isolation, sandbox, egress, audit and red team |
| Model evaluations | Test scaffolding | Golden datasets, task-specific evals, thresholds, calibration |
