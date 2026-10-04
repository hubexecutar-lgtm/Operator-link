# 01 — Índice mestre

`EXECUTAR_WORKBOOK_MASTER_INDEX_GRANULAR_v1.0.0.csv` — índice granular de todas as
entidades catalogadas (168 linhas). Arquivo **preservado byte a byte** (UTF-8 com BOM);
não editar manualmente — nova versão = novo arquivo `_vX.Y.Z.csv` + entrada no `CHANGELOG.md`.

## Colunas

| Coluna | Significado |
|---|---|
| `ID` | Identificador (texto) |
| `ID_PAI` | Agrupador ou domínio pai |
| `TIPO` | `AGRUPADOR`, `MACROAREA`, `DOMINIO`, `CAMPO`, `SECAO`, `CAMADA`, `ABA`, `ETAPA_ADAPTACAO` |
| `TITULO` | Rótulo literal |
| `MACROAREAS` | Macroáreas associadas (`;`) — a primeira é a principal proposta |
| `LOCALIZACAO` | Onde está na fonte original |
| `ORIGEM_ID` | `LEGADO` ou `PROPOSTO` |
| `STATUS` | Estado de catalogação/execução |

## Composição

| TIPO | Qtde | Agrupador |
|---|---|---|
| MACROAREA | 13 | `IDX-MACRO` |
| DOMINIO | 17 | `IDX-DOM` |
| CAMPO | 94 | domínios 1–17 |
| SECAO | 7 | `IDX-CADERNO` |
| CAMADA | 3 | `IDX-CAMADAS` |
| ABA | 21 | `IDX-ABAS` |
| ETAPA_ADAPTACAO | 7 | `IDX-MIGRACAO` |
| AGRUPADOR | 6 | — |

Integridade verificada por `scripts/validar_estrutura.py`.
