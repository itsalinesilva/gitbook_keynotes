# Threat model — Brain OS

## Ativos
- Dados internos e pessoais.
- Credenciais, tokens e segredos.
- Índices de conhecimento, memórias e fontes.
- Ferramentas com capacidade de escrita/execução.
- Artefatos, relatórios e decisões.
- Políticas, prompts, schemas e dados de avaliação.

## Limites de confiança
- Usuário ↔ gateway.
- Modelo ↔ ferramenta.
- Conteúdo recuperado ↔ instruções de sistema.
- Agente especialista ↔ orquestrador.
- Ambiente de teste ↔ produção.
- Conectores externos ↔ armazenamento interno.
- Memória proposta ↔ memória aprovada.

## Ameaças prioritárias
1. Prompt injection direto/indireto em páginas, documentos e resultados de ferramentas.
2. Exfiltração de dados através de respostas, logs, URLs ou chamadas de ferramentas.
3. Uso excessivo de permissões ou confused deputy.
4. Poisoning de corpus, fontes e memória.
5. Execução de ações externas sem consentimento.
6. SSRF, path traversal, abuso de parsers e conteúdo malformado.
7. Vazamento de segredos em traces e datasets de avaliação.
8. Ataques de cadeia de suprimentos em pacotes, modelos e servidores MCP.
9. Denial of wallet por loops, consultas caras ou contexto excessivo.
10. Alteração silenciosa de schema, prompt, modelo ou configuração.

## Controles mínimos
- Tratar conteúdo recuperado como dado não confiável, nunca como política.
- Separar permissões de leitura, escrita e execução.
- Allowlist de ferramentas e recursos; validação de argumentos no servidor.
- Aprovação explícita para side effects relevantes.
- Segredos fora de prompts, logs e repositórios.
- Sandboxing e egress control para execução de código.
- Rate limits, limites de passos, orçamento de tokens/custo e timeouts.
- Proveniência e hashes para artefatos críticos.
- Revisão de dependências, pinning, SBOM quando apropriado.
- Logs com redaction e controle de acesso.
- Red-team periódico e testes de regressão de segurança.

## Resposta a incidente
1. Conter: revogar credenciais, desabilitar ferramenta ou rota afetada.
2. Preservar evidências: traces redigidos, IDs de execução, hashes e timeline.
3. Determinar escopo e impacto.
4. Corrigir causa raiz e adicionar teste de regressão.
5. Restaurar com rollout controlado.
6. Revisar política, treino operacional e comunicação necessária.
