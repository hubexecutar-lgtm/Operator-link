# Operator-link — Governança EXECUTAR

Repositório de governança documental do **EXECUTAR**: acervo, manual de referência e
caderno operacional, controlados por um contrato de dados versionado e rastreável até
as fontes originais.

> **Estado atual:** estrutura preparada (v0.1.0). Contratos v1.0.0 carregados.
> Nenhum documento de conteúdo registrado ainda. Adaptação na etapa **MIG-01 (READY)**.

## Estrutura

```
.
├── CLAUDE.md                  # instruções para agentes de IA
├── CHANGELOG.md
├── 00_governanca/             # política de IDs, máquina de estados, convenções
├── 01_indice/                 # índice mestre granular (168 entidades, 94 campos)
├── 02_schemas/v1.0.0/         # contratos YAML — FONTE NORMATIVA
├── 10_acervo_integral/        # camada ACERVO_INTEGRAL — originais imutáveis + manifesto sha256
├── 20_manual_referencia/      # camada MANUAL_REFERENCIA — uma pasta por macroárea A00–A12
├── 30_caderno_operacional/    # camada CADERNO_OPERACIONAL — uma pasta por seção COP-S01–S07
├── 40_controle/               # histórico, evidências, plano MIG e gaps
├── 90_templates/              # registro, ficha de execução, evidência, ADR
├── scripts/validar_estrutura.py
└── .github/                   # CI de validação e template de PR
```

## Modelo conceitual

Cinco eixos **independentes** — nenhum substitui o outro:

| Eixo | Valores | Onde aparece |
|---|---|---|
| Macroárea | `A00`–`A12` | pastas de `20_manual_referencia/`, front matter |
| Domínio legado | `1`–`17` | índice, `ids_legados` |
| Campo legado | `1.1`–`17.3` (94, texto) | índice, mapeamento |
| Seção operacional | `COP-S01`–`COP-S07` | pastas de `30_caderno_operacional/` |
| Camada documental | acervo / manual / caderno | pastas `10_`, `20_`, `30_` |

### Macroáreas

| ID | Nome | ID | Nome |
|---|---|---|---|
| A00 | Governança Estratégia e Gestão | A07 | Corporativo e Suporte |
| A01 | Negócio e Go to Market | A08 | Conteúdo Comunicação e Growth |
| A02 | Produto e Experiência | A09 | Execução e Planejamento do Trabalho |
| A03 | Handoff Produto para Engenharia | A10 | Documentação e Governança do Conhecimento |
| A04 | Arquitetura Engenharia e Implementação | A11 | Ferramentas IA e Ativos Reutilizáveis |
| A05 | Operações Plataforma e Segurança | A12 | Stakeholders e Ecossistema |
| A06 | Dados Pesquisa e Conhecimento | | |

## Como adicionar documentação

1. **Fonte original** → copie para `10_acervo_integral/fontes/` sem alterar o nome e registre
   em `MANIFESTO_FONTES.csv` (`SRC-xxxxxx` + `sha256sum`).
2. **Documento de referência** → copie `90_templates/TEMPLATE_REGISTRO.md` para a pasta da
   macroárea principal como `REG-xxxxxx_titulo-curto.md`; preencha o front matter com
   `origens` apontando para o `SRC-`.
3. **Ficha de execução** → `90_templates/TEMPLATE_FICHA_EXECUCAO.md` em `30_caderno_operacional/COP-S04_fichas_execucao/`.
4. Atualize a tabela do README da pasta e, se houver mudança de estado, `40_controle/HISTORICO.csv`.
5. Valide e abra PR:

```bash
pip install pyyaml
python3 scripts/validar_estrutura.py
```

Detalhes: [00_governanca/CONVENCOES.md](00_governanca/CONVENCOES.md).

## Princípios

- **Rastreabilidade**: todo registro tem ao menos uma origem (`SRC-`); toda fonte tem sha256.
- **Imutabilidade**: IDs legados nunca são renumerados; originais nunca são editados.
- **Sem invenção**: o que não se sabe é `A DEFINIR`, nunca um valor plausível.
- **Evidência ≠ citação**: `VERIFIED` exige evidência `VERIFICADA` e aceite `ATENDIDO`.
- **WIP = 1** por escopo de execução.

## Pendências conhecidas

Ver [40_controle/README.md](40_controle/README.md). Destaque: **GAP-001** — seis documentos
citados no `WORKBOOK INDEX.txt` ainda não foram recebidos (bloqueia MIG-04).
