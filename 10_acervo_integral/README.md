# 10 — Acervo integral

Camada **ACERVO_INTEGRAL**: originais preservados sem alteração. É a base de
rastreabilidade de todo o repositório.

```
10_acervo_integral/
├── MANIFESTO_FONTES.csv   # catálogo SRC-xxxxxx com sha256 e disponibilidade
└── fontes/                # arquivos originais, nome literal, nunca editados
```

## Regras

1. Todo arquivo em `fontes/` tem uma linha em `MANIFESTO_FONTES.csv` com `sha256` conferido.
2. Originais são **imutáveis**. Correções viram nova fonte (novo `SRC-`) + relação no controle.
3. `disponibilidade`: `DISPONIVEL` (no repositório), `INDISPONIVEL` (conhecido, não recebido), `A DEFINIR`.
4. Não inventar conteúdo de fonte indisponível.

## Pendências

- **GAP-001 (BLOCKED)** — seis documentos mencionados no `WORKBOOK INDEX.txt` não foram fornecidos.
  Bloqueia MIG-04. Ao recebê-los: adicionar em `fontes/`, registrar `SRC-`, calcular `sha256`.
- `SRC-000001` (planilha original `.xlsx`) e `SRC-000002` (`WORKBOOK INDEX.txt`) são conhecidos
  apenas por hash; adicionar os arquivos quando disponíveis e confirmar o hash.
