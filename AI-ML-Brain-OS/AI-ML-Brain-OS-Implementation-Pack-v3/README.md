# AI/ML Brain OS — Implementation & Validation Pack v3.0

Este pacote complementa o manual de arquitetura e o scaffold anterior. Ele transforma recomendações em contratos, gates, testes, runbooks e critérios de aceitação.

## Princípios
1. **Contract-first**: interfaces, schemas e estados são definidos antes da implementação.
2. **Evidence-first**: afirmações importantes devem apontar para evidências rastreáveis.
3. **Eval-driven**: uma mudança só é promovida quando passa pelos testes adequados ao risco.
4. **Least privilege**: agentes recebem somente as ferramentas, dados e permissões necessárias.
5. **Human accountability**: automação não elimina a responsabilidade por decisões de alto impacto.
6. **Replaceable components**: modelos, vetores, orquestradores e provedores devem poder ser substituídos por interfaces estáveis.
7. **Observable by default**: cada execução deve ter identidade, estado, custos, duração, decisões e erros observáveis.
8. **Fail closed for consequential actions**: ações irreversíveis, externas ou de alto impacto exigem autorização explícita.

## Como usar
1. Leia `architecture/REFERENCE-ARCHITECTURE.md`.
2. Adapte os contratos em `contracts/` ao domínio e aos dados reais.
3. Preencha os templates de `templates/`.
4. Defina os gates e os casos de avaliação em `quality/`.
5. Faça threat modeling com `security/THREAT-MODEL.md`.
6. Planeje a implantação por fases em `roadmap/IMPLEMENTATION-ROADMAP.md`.
7. Valide cada requisito com evidência antes de marcar como implementado.

## Status
Este é um pacote de referência. Não inclui runtime de agentes, credenciais, conectores operacionais nem integração validada com sistemas externos.
