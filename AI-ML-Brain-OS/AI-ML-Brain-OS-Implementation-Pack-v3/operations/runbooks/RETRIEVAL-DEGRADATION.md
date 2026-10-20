# Runbook: degradação de retrieval/RAG

## Indicadores
- Queda de recall@k ou relevância.
- Mais respostas sem evidência.
- Citações para conteúdo removido ou desatualizado.
- Latência e custo acima do orçamento.

## Diagnóstico
1. Conferir frescor, falhas de ingestão e contagem de documentos.
2. Verificar schema, chunking, filtros e permissões de tenant.
3. Comparar busca lexical, vetorial e híbrida no conjunto golden.
4. Inspecionar reranking, duplicação, documentos contaminados e idioma.
5. Comparar versão atual do corpus/index com a última versão saudável.

## Mitigação
- Reverter índice ou pipeline de ingestão.
- Desativar filtros ou transformações somente após revisão de segurança.
- Reduzir escopo e comunicar limitações.
- Não preencher lacunas com conteúdo não verificado.

## Encerramento
Registrar causa, métricas antes/depois, documentos afetados e novo teste de regressão.
