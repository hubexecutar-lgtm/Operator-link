# Política de IDs

Fonte: `02_schemas/v1.0.0/03_CONTROLES_EXCEL.yaml` → `catalogos.id_policies` e
`02_schemas/v1.0.0/01_SCHEMA_CONTROLE.yaml`.

## Eixos independentes

Os eixos abaixo **não** são equivalentes entre si. Nunca converter um no outro
automaticamente (ver GAP-002).

| Eixo | Formato | Exemplo | Regra |
|---|---|---|---|
| Domínio legado | `1`–`17` | `6` | Organização original dos campos. Não renumerar para `Axx`. Novos domínios só a partir de `18`, se realmente necessários. |
| Campo legado | `domínio.campo` (texto) | `1.10` | Imutável. **Texto**, nunca decimal (`1.10` ≠ `1.1`). |
| Macroárea | `A00`–`A12` | `A05` | Classificação temática transversal: uma principal + zero ou mais secundárias. |
| Seção operacional | `COP-S01`–`COP-S07` | `COP-S04` | Organiza leitura e impressão do caderno. Não é fase nem estado. |
| Camada documental | enum | `MANUAL_REFERENCIA` | `ACERVO_INTEGRAL`, `MANUAL_REFERENCIA`, `CADERNO_OPERACIONAL`. Uma unidade pode ocorrer em várias camadas. |
| Rótulo AREA (navegação) | `NAV-000000` | `NAV-000001` | Preservar rótulo literal. "AREA 04" **não** é `A04`. |

## Chaves de entidades de controle

Seis dígitos sequenciais, imutáveis, nunca derivados do número da linha.

| Prefixo | Entidade | Padrão |
|---|---|---|
| `REG-` | Registro (unidade de conteúdo/entidade) | `^REG-[0-9]{6}$` |
| `SRC-` | Fonte | `^SRC-[0-9]{6}$` |
| `NAV-` | Navegação | `^NAV-[0-9]{6}$` |
| `COV-` | Cobertura | `^COV-[0-9]{6}$` |
| `REL-` | Relação | `^REL-[0-9]{6}$` |
| `EVD-` | Evidência | `^EVD-[0-9]{6}$` |
| `EVT-` | Evento de histórico | `^EVT-[0-9]{6}$` |

## Regras

1. **Alocação central**: antes de criar um ID, verificar o maior ID existente do
   prefixo e usar o próximo. Validar unicidade antes de salvar.
2. **Imutabilidade**: um ID nunca é reutilizado, mesmo após arquivamento.
3. **Hierarquia** via `parent_id`; sem autorreferência e sem ciclos.
4. **Não reutilizar ID de campo como ID de tarefa.**
5. **Escopo**: `REG` é único no repositório. Referências externas exigem
   `workbook_id` + `registro_id`.
6. Rótulos incompletos ou sem numeração estável (GAP-003) recebem chave interna;
   o rótulo original e sua localização são preservados.
