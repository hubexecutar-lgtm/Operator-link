# Convenções

## Idioma

Português do Brasil. Termos técnicos e enums do schema permanecem como definidos
(ex.: `VERIFIED`, `DEPENDS_ON`).

## Nomes de arquivos

| Tipo | Padrão | Exemplo |
|---|---|---|
| Registro documental | `REG-000000_titulo-curto.md` | `REG-000012_estrategia-branch.md` |
| Ficha de execução | `REG-000000_FICHA_titulo-curto.md` | `REG-000031_FICHA_migrar-indice.md` |
| ADR | `ADR-000_titulo-curto.md` dentro de `20_manual_referencia/A04_*/adr/` | `ADR-001_banco-de-dados.md` |
| Fonte original | nome original, sem alteração | `WORKBOOK INDEX.txt` |

Sem acentos, espaços ou maiúsculas no `titulo-curto`. Fontes originais mantêm o nome literal.

## Front matter obrigatório

Todo documento em `20_manual_referencia/` e `30_caderno_operacional/` começa com o
bloco YAML do template `90_templates/TEMPLATE_REGISTRO.md` (contrato `registro`).

## Valores desconhecidos

- Campos humanos desconhecidos: texto literal `A DEFINIR`.
- Raiz de hierarquia ou tempo desconhecido: `null`.
- Nunca preencher com valores fictícios ou plausíveis.

## Fluxo de alteração

1. Criar branch a partir de `main`.
2. Alocar IDs (ver `POLITICA_IDS.md`), criar/editar documentos a partir dos templates.
3. Atualizar o README da pasta de destino (tabela "Documentos"/"Conteúdo").
4. Registrar evento em `40_controle/HISTORICO.csv` quando houver mudança de estado ou baseline.
5. Rodar `python3 scripts/validar_estrutura.py`.
6. Abrir PR. Gate humano obrigatório para merge (campo legado `6.2`).

## Commits

Mensagem no imperativo, em português, com prefixo de escopo:
`acervo:`, `manual(A05):`, `caderno(COP-S04):`, `controle:`, `schema:`, `governanca:`, `infra:`.
