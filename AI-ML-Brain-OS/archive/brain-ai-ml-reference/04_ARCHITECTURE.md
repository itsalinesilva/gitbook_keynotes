# Arquitetura

Veja o manual completo em `docs/AI-ML-Brain-OS-Manual.md`.

## Separação fundamental

-   Knowledge plane: fontes, documentos, evidências, memória e índices.
-   Control plane: políticas, permissões, roteamento, limites e
    aprovações.
-   Execution plane: runtime, agentes, ferramentas, workflows e
    pipelines.
-   Evaluation plane: datasets, evals, traces, métricas e auditorias.

## Regra

A arquitetura do conhecimento deve continuar utilizável sem um
orquestrador específico.
