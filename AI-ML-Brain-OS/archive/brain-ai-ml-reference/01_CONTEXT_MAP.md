# Context Map --- mapa mestre

  -----------------------------------------------------------------------------------------------
  Tipo de pedido    Leia primeiro                             Leia também       Saída esperada
  ----------------- ----------------------------------------- ----------------- -----------------
  Alterar           `docs/AI-ML-Brain-OS-Manual.md` §§ 3--6,  padrões de        ADR + diagrama +
  arquitetura       ADRs                                      arquitetura       trade-offs

  Criar             `_system/templates/ROLE_SPEC.md`          políticas, evals  spec versionada +
  agente/papel                                                                  evals

  Criar skill       `_system/templates/SKILL.md`              tool contracts    skill +
                                                                                exemplos + testes

  Fazer pesquisa    `_system/templates/RESEARCH_DOSSIER.md`   fontes,           dossiê
                                                              evidências,       rastreável +
                                                              política          propostas
                                                              editorial         

  Adicionar         `_system/templates/TOOL_CONTRACT.md`      permissões e      contrato +
  ferramenta                                                  threat model      testes + política

  Alterar regra     políticas globais + ADR                   suite de          PR com aprovação
  global                                                      regressão         

  Incidente         `_system/incident-response/README.md`     traces e runbooks registro do
                                                                                incidente +
                                                                                remediação
  -----------------------------------------------------------------------------------------------

## Regra

Se o contexto necessário não estiver disponível, declarar a lacuna. Não
inventar conteúdo nem afirmar que um arquivo foi lido quando não foi.
