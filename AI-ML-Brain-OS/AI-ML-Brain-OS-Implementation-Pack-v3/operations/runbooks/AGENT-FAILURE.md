# Runbook: falha ou comportamento anômalo de agente

## Sinais
- Loop ou excesso de passos.
- Aumento de timeout, custo ou erros de ferramenta.
- Saída sem evidências, citações quebradas ou schema inválido.
- Ação não autorizada ou acesso a dados fora do escopo.

## Triage
1. Capturar `run_id`, `correlation_id`, versão de prompt/modelo/tools/corpus.
2. Determinar se houve efeito externo; se sim, conter primeiro.
3. Verificar trace, sequência de tool calls, erros e mudanças recentes.
4. Classificar incidente por impacto e sensibilidade.
5. Desabilitar ferramenta, modelo ou rota se houver risco em curso.

## Recuperação
- Retry apenas se a operação for segura e idempotente.
- Não repetir ações de escrita sem consultar idempotency key/estado externo.
- Retomar do último checkpoint consistente.
- Usar fallback determinístico ou resposta inconclusiva quando possível.
- Exigir aprovação humana se o estado externo for ambíguo.

## Pós-incidente
- Registrar causa raiz, impacto, duração e correção.
- Criar caso de teste de regressão.
- Atualizar runbook e threat model.
- Avaliar se a falha exige rollback de prompt/modelo/corpus.
