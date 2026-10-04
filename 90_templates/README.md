# 90 — Templates

| Template | Uso | Contrato (01_SCHEMA_CONTROLE.yaml) |
|---|---|---|
| [TEMPLATE_REGISTRO.md](TEMPLATE_REGISTRO.md) | Qualquer documento do manual ou do caderno | `registro` |
| [TEMPLATE_FICHA_EXECUCAO.md](TEMPLATE_FICHA_EXECUCAO.md) | Tarefa/ação em `COP-S04` | `registro` + `execucao` |
| [TEMPLATE_EVIDENCIA.md](TEMPLATE_EVIDENCIA.md) | Evidência em `40_controle/evidencias/` | `evidencia` |
| [TEMPLATE_ADR.md](TEMPLATE_ADR.md) | Decisão de arquitetura (campos legados `3.8`, `3.9`) | `registro` (tipo `DECISAO`) |

Copie o template, renomeie conforme `00_governanca/CONVENCOES.md` e substitua os valores.
Mantenha `A DEFINIR` onde a informação não existir.

> **Campos auxiliares do repositório**: `camadas` (front matter) e `execucao.depends_on`
> não fazem parte do contrato `registro`/`execucao`. Na exportação viram linhas de
> `cobertura` e relações `DEPENDS_ON`, respectivamente.
