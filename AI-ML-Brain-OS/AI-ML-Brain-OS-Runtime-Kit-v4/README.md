# AI/ML Brain OS Runtime Kit v4

Runtime mínimo executável de referência. Python 3.11+.

## Executar
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
brain-os health
brain-os run "Mapear padrões de arquitetura de agentes"
```

Inclui runtime determinístico, allowlist de ferramentas, política de aprovação, SQLite para fontes/documentos/propostas de memória, logs estruturados, testes, CI e Dockerfile.

**Limitação:** é um starter, não produção. Não tem LLM conectado por padrão, banco vetorial, autenticação corporativa, tracing distribuído ou conectores reais configurados. Ver `docs/PRODUCTION-GAP-ANALYSIS.md`.
