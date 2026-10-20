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
