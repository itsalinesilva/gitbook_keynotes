# Checklist de revisão arquitetural

## Produto e domínio
- [ ] Usuário, problema e valor mensurável estão claros?
- [ ] O sistema é necessário ou uma função determinística resolve?
- [ ] Escopo e não-objetivos estão documentados?

## Arquitetura
- [ ] Fronteiras, componentes, fluxos e dependências estão claros?
- [ ] Estado, eventos, retries, cancelamento e idempotência estão definidos?
- [ ] Contratos não dependem de detalhes de um fornecedor sem necessidade?
- [ ] Dados de controle e dados de conteúdo estão separados?

## Dados e conhecimento
- [ ] Linhagem, direitos, retenção e exclusão são conhecidos?
- [ ] Fonte, evidência, claim e inferência estão diferenciados?
- [ ] Retrieval tem benchmark e critérios de frescor?
- [ ] Memória tem curadoria, versionamento e expiração?

## Segurança
- [ ] Modelo de ameaças e fronteiras de confiança estão documentados?
- [ ] Privilégios mínimos e aprovação por risco são aplicados?
- [ ] Prompt injection e exfiltração foram testados?
- [ ] Logs, traces e artefatos não vazam dados sensíveis?

## Qualidade e operação
- [ ] Evals cobrem casos positivos, negativos, adversariais e abstinência?
- [ ] Observabilidade liga a solicitação a cada chamada de ferramenta?
- [ ] Orçamento e SLO são explícitos?
- [ ] Rollback, incidentes e recuperação foram testados?

## Governança
- [ ] Donos, revisores e aprovadores estão definidos?
- [ ] Mudanças de schema, prompt, modelo e política são versionadas?
- [ ] Há processo de descontinuação e migração?
