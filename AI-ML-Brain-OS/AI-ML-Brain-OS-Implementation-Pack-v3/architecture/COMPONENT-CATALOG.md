# Catálogo de componentes e responsabilidades

| Componente | Responsabilidade única | Entrada | Saída | Falha esperada / fallback |
|---|---|---|---|---|
| Intake Gateway | autenticar, validar e normalizar pedido | solicitação | envelope validado | rejeitar ou pedir esclarecimento |
| Risk Classifier | estimar risco e classe de ação | envelope | rótulos + justificativa | classificação conservadora |
| Planner | criar plano verificável | objetivo + limites | DAG de tarefas | plano simples ou escalonamento |
| Orchestrator | estado, dependências, retries, cancelamento | plano | eventos de execução | checkpoint e retomada |
| Specialist | executar escopo delimitado | subtarefa + contexto | resultado tipado | retornar inconclusivo |
| Source Resolver | resolver identidade e reputação de fontes | URL/consulta | registro de fonte | fonte não verificada |
| Retriever | recuperar evidência relevante | consulta | evidências ranqueadas | resposta sem suporte / abstenção |
| Evidence Ledger | rastrear afirmação para fonte | claim + evidence | relação versionada | bloquear claim sem suporte |
| Synthesizer | resolver concordâncias e conflitos | resultados | síntese estruturada | expor conflito não resolvido |
| Evaluator | executar testes apropriados | entrada + saída | scores e falhas | bloquear promoção |
| Policy Engine | autorizar ferramenta e ação | identidade + contexto | allow/deny/approval | deny by default |
| Tool Gateway | validar e executar ferramentas | chamada tipada | resultado tipado | timeout, retry seguro, circuit breaker |
| Memory Curator | propor atualização de memória | feedback/evidência | proposta versionada | revisão humana |
| Artifact Publisher | entregar versão assinada/rastreável | artefato aprovado | ID + localização | não publicar |
| Telemetry | emitir traces/logs/métricas | eventos | telemetria correlacionada | fila local/alerta |
