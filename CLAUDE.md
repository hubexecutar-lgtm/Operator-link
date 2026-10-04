# CLAUDE.md

Instruções para agentes de IA que trabalham neste repositório.

## O que é este repositório

Repositório de **governança documental** do EXECUTAR (não é código de aplicação).
Contém o acervo original, o manual de referência por macroárea e o caderno operacional,
todos controlados pelos contratos em `02_schemas/v1.0.0/`.

Idioma: **português do Brasil**. Enums e chaves do schema ficam como definidos (`VERIFIED`, `DEPENDS_ON`…).

## Fonte de verdade (ordem de precedência)

1. `02_schemas/v1.0.0/*.yaml` — contratos normativos. Em conflito, o YAML vence.
2. `01_indice/EXECUTAR_WORKBOOK_MASTER_INDEX_GRANULAR_v1.0.0.csv` — catálogo de entidades.
3. `10_acervo_integral/MANIFESTO_FONTES.csv` — fontes e hashes.
4. `00_governanca/*.md` — resumos legíveis das regras acima.

READMEs de macroárea/seção contêm tabelas **derivadas** do `02_MAPEAMENTO_94_IDS.yaml`; não são fonte.

## Regras invioláveis

- **Nunca inventar conteúdo.** Informação ausente = `A DEFINIR` (campos humanos) ou `null` (raiz/tempo).
  Não preencher respostas dos 94 campos sem fonte explícita do usuário.
- **Nunca editar** arquivos em `10_acervo_integral/fontes/`, `01_indice/*.csv` ou uma versão
  publicada de `02_schemas/vX.Y.Z/`. Mudança = nova versão + `CHANGELOG.md`.
- **IDs legados são texto e imutáveis**: `1.10` ≠ `1.1`. Nunca renumerar domínios 1–17 nem
  convertê-los em `Axx`. "AREA 04" do TXT **não** é `A04` (GAP-002).
- **Alocação de IDs** (`REG/SRC/NAV/COV/REL/EVD/EVT-` + 6 dígitos): procure o maior existente
  (`grep -rhoE 'REG-[0-9]{6}' . | sort -u | tail -1`) e use o próximo. Nunca reutilize.
  `REG-000000`, `SRC-000000` e `EVD-000000` são placeholders de template, nunca IDs reais.
- **Evidência citada ≠ verificada.** Só marque `VERIFIED`/`VERIFICADA` com método, data e
  responsável reais. `DECLARED_DONE` não é `VERIFIED`.
- **`40_controle/HISTORICO.csv` é append-only.** Nunca reescrever linhas existentes.
- **WIP = 1** por `escopo_wip_id`. `IN_PROGRESS` exige `owner` definido.
- Não consolidar divergências silenciosamente (GAP-004): registre cada ocorrência e a relação.
- Fontes indisponíveis (GAP-001, SRC-000001, SRC-000002) não devem ser reconstruídas por inferência.

## Onde colocar cada coisa

| Conteúdo | Destino | Template |
|---|---|---|
| Arquivo original recebido | `10_acervo_integral/fontes/` + linha em `MANIFESTO_FONTES.csv` | — |
| Documento de referência | `20_manual_referencia/Axx_*/REG-xxxxxx_titulo.md` (macroárea principal) | `TEMPLATE_REGISTRO.md` |
| Decisão de arquitetura | `20_manual_referencia/A04_*/adr/` | `TEMPLATE_ADR.md` |
| Tarefa/ação executável | `30_caderno_operacional/COP-S04_fichas_execucao/` | `TEMPLATE_FICHA_EXECUCAO.md` |
| Item do caderno (outras seções) | `30_caderno_operacional/COP-Sxx_*/` — referencia um REG do manual | `TEMPLATE_REGISTRO.md` |
| Evidência | `40_controle/evidencias/EVD-xxxxxx_*.md` | `TEMPLATE_EVIDENCIA.md` |
| Mudança de estado/baseline | linha nova em `40_controle/HISTORICO.csv` | — |

Ao adicionar um documento, atualize também a tabela "Documentos"/"Conteúdo" do README da pasta.

## Fluxo de trabalho

1. Ler o schema relevante antes de criar/editar entidades.
2. Ao receber nova fonte: copiar sem alterar, `sha256sum`, registrar `SRC-`.
3. Criar documentos a partir de `90_templates/`; nome `REG-xxxxxx_titulo-curto.md` (sem acentos/espaços).
4. Validar: `python3 scripts/validar_estrutura.py` (requer `pip install pyyaml`). Deve terminar em `OK`.
5. Commit com prefixo de escopo: `acervo:`, `manual(Axx):`, `caderno(COP-Sxx):`, `controle:`,
   `schema:`, `governanca:`, `infra:`.
6. Merge em `main` exige revisão humana (gate humano — campo legado `6.2`).

## Comandos

```bash
python3 scripts/validar_estrutura.py                       # valida índice, schemas, manifesto, pastas e REGs
sha256sum 10_acervo_integral/fontes/<arquivo>              # hash para o manifesto
grep -rhoE 'REG-[0-9]{6}' --include='*.md' . | sort -u     # IDs REG em uso
```

## Estado atual

- v0.1.0: estrutura pronta, nenhum REG criado.
- Plano de adaptação: MIG-01 READY; MIG-04 BLOCKED por GAP-001. Ver `40_controle/README.md`.
