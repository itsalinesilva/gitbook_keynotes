# Threat model --- baseline

## Ativos

Dados privados, credenciais, código, decisões, reputação, orçamento e
serviços de produção.

## Ameaças mínimas

-   Prompt injection direta/indireta;
-   Exfiltração de dados;
-   Tool misuse;
-   Acesso excessivo;
-   Poisoning de memória/índice;
-   Loop de custo;
-   Dependência comprometida;
-   Logs com dados sensíveis.

## Controles

-   Menor privilégio;
-   Allowlist e schemas de ferramentas;
-   Sandboxing;
-   Secrets manager;
-   Redação de logs;
-   Aprovação humana para ações de risco;
-   Testes adversariais;
-   Runbooks e rollback.

## Estado

Este documento é uma lista inicial; realizar análise específica antes de
produção.
