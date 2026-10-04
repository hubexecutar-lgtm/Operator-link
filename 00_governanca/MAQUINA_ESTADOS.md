# Máquina de estados

Fonte: `02_schemas/v1.0.0/03_CONTROLES_EXCEL.yaml` → `maquina_estados`,
`integridade_entre_linhas`.

## Status documental (documentos/registros)

`ORIGINAL` · `DRAFT` · `PREPARED` · `SUBMITTED` · `APPROVED` · `RELEASED` · `ARCHIVED`

## Status de execução (fichas/tarefas)

Fluxo nominal: `NOT_READY → READY → IN_PROGRESS → DECLARED_DONE → VERIFIED`.

| De | Para permitido |
|---|---|
| `NOT_READY` | `READY`, `BLOCKED` |
| `READY` | `IN_PROGRESS`, `NOT_READY`, `BLOCKED` |
| `IN_PROGRESS` | `DECLARED_DONE`, `BLOCKED` |
| `BLOCKED` | `NOT_READY`, `READY` |
| `DECLARED_DONE` | `VERIFIED`, `IN_PROGRESS`, `BLOCKED` |
| `VERIFIED` | `NOT_READY` (reabertura: exige evento com motivo e revisão do aceite) |

## Regras de transição

- **READY** exige entradas presentes e todas as dependências (`DEPENDS_ON`) em `VERIFIED`.
- **IN_PROGRESS** exige `owner` definido (≠ `A DEFINIR`). **WIP = 1** por `escopo_wip_id`.
- **BLOCKED** exige campo `bloqueio` preenchido.
- **VERIFIED** exige `resultado_aceite: ATENDIDO`, ao menos uma evidência vinculada
  e ao menos uma evidência com `natureza: VERIFICADA` (com método, data e responsável).
- `DECLARED_DONE` ≠ `VERIFIED`: declarar concluído não é provar.
- Toda transição gera uma linha em `40_controle/HISTORICO.csv` (append-only).
- Conflitos não resolvidos bloqueiam apenas as tarefas afetadas, não o repositório.

## Natureza da evidência

| Valor | Significado |
|---|---|
| `CITADA` | Fonte mencionada, não conferida |
| `VERIFICADA` | Conferida, com `metodo_verificacao`, `verificado_em`, `verificado_por` |
| `HIPOTESE` | Afirmação ainda sem suporte |
