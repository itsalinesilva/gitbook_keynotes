# Política de memória e conhecimento

## Classes
- **Session context**: dados transitórios de uma execução.
- **User preference**: preferência explicitamente declarada e com escopo limitado.
- **Project memory**: decisões, definições e fatos do projeto com proveniência.
- **Operational memory**: falhas, métricas e runbooks.
- **Source knowledge**: documentos externos e internos com versionamento.
- **Policy**: regra de governança controlada por processo de mudança, não por geração espontânea.

## Ciclo de vida
Proposta → validação de evidências → análise de conflito → revisão de privacidade → aprovação → versionamento → monitoramento → expiração/retirada.

## Regras
- Não converter automaticamente qualquer saída do modelo em fato ou política.
- Manter origem, data, escopo, validade e responsável.
- Permitir correção e invalidação com trilha de auditoria.
- Aplicar retenção mínima necessária.
- Evitar armazenar segredos e dados sensíveis sem necessidade e base autorizada.
- Distinguir ausência de evidência de evidência de ausência.
- Registrar quando uma memória é hipótese, preferência, decisão ou fato verificado.
