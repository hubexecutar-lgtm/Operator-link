# 02 — Schemas (fonte normativa)

Contratos versionados. **Fonte de verdade** para estrutura, IDs, enums e regras.
Arquivos preservados como recebidos (origem: `SRC-000003`).

| Arquivo (v1.0.0) | ID | Conteúdo |
|---|---|---|
| `00_PLANO_ADAPTACAO.yaml` | EXECUTAR-WORKBOOK-ADAPTACAO-001 | Contrato, evidências, arquitetura, gaps (GAP-001…005), plano MIG-01…07 |
| `01_SCHEMA_CONTROLE.yaml` | urn:executar:workbook:controle:1.0.0 | JSON Schema (2020-12) das entidades: fonte, navegação, registro, cobertura, relação, execução, evidência, histórico |
| `02_MAPEAMENTO_94_IDS.yaml` | EXECUTAR-WORKBOOK-MAPEAMENTO-001 | Classificação proposta dos 94 campos legados |
| `03_CONTROLES_EXCEL.yaml` | EXECUTAR-WORKBOOK-CONTROLES-001 | Catálogos, política de IDs, abas, validações, máquina de estados, regras de impressão |

## Versionamento

- Nunca editar uma versão publicada. Mudança = nova pasta `vX.Y.Z/` + `CHANGELOG.md`.
- MAJOR: quebra de contrato (campo removido, enum alterado). MINOR: adição compatível. PATCH: texto.
