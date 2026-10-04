# 40 — Controle

Entidades de controle do contrato `01_SCHEMA_CONTROLE.yaml` e acompanhamento da adaptação.

```
40_controle/
├── HISTORICO.csv     # tblHistorico — append-only, uma linha por evento (EVT-xxxxxx)
└── evidencias/       # EVD-xxxxxx_*.md (template: 90_templates/TEMPLATE_EVIDENCIA.md)
```

Registros (`REG`) vivem como documentos no manual/caderno; cobertura (`COV`) e relações (`REL`)
serão criadas aqui como `COBERTURA.csv` e `RELACOES.csv` quando houver o primeiro registro.

## Plano de adaptação (snapshot de `00_PLANO_ADAPTACAO.yaml`)

| ID | Ação | Depende de | Estado |
|---|---|---|---|
| MIG-01 | Registrar baseline e catálogo literal de navegação | — | READY |
| MIG-02 | Implementar tabelas e validações do contrato | MIG-01 | NOT_READY |
| MIG-03 | Aplicar classificação dos 94 campos | MIG-02 | NOT_READY |
| MIG-04 | Inventariar unidades documentais e cobertura | MIG-03 | BLOCKED (GAP-001) |
| MIG-05 | Preparar fichas operacionais e grafo de dependências | MIG-04 | NOT_READY |
| MIG-06 | Construir Hub e visão de impressão | MIG-05 | NOT_READY |
| MIG-07 | Verificar migração e registrar handoff | MIG-06 | NOT_READY |

## Gaps e conflitos abertos

| ID | Tipo | Resumo | Status |
|---|---|---|---|
| GAP-001 | LACUNA | Seis arquivos citados no TXT não anexados | BLOCKED |
| GAP-002 | AMBIGUIDADE | "AREA 04/06" ≠ `A04`/`A06` — manter namespaces distintos | A DEFINIR |
| GAP-003 | LACUNA | Rótulos sem numeração estável — usar chave interna | A DEFINIR |
| GAP-004 | DUPLICIDADE | Índice do caderno e três camadas reaparecem no TXT | PREPARED |
| GAP-005 | COBERTURA | A07 com poucos campos legados | A DEFINIR |

> Estados acima são snapshot da v1.0.0. Mudanças de estado: registrar em `HISTORICO.csv`.
