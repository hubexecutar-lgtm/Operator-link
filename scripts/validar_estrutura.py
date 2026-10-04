#!/usr/bin/env python3
"""Valida a estrutura do repositório de governança.

Checa: índice mestre, schemas YAML, manifesto de fontes (sha256),
pastas de macroárea/seção e front matter dos documentos REG-*.
Uso: python3 scripts/validar_estrutura.py   (requer PyYAML)
"""
import csv
import hashlib
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
SCHEMAS = RAIZ / "02_schemas" / "v1.0.0"
INDICE = RAIZ / "01_indice" / "EXECUTAR_WORKBOOK_MASTER_INDEX_GRANULAR_v1.0.0.csv"
MANIFESTO = RAIZ / "10_acervo_integral" / "MANIFESTO_FONTES.csv"

erros = []


def erro(msg):
    erros.append(msg)


def validar_schemas():
    dados = {}
    for p in sorted(SCHEMAS.glob("*.yaml")):
        try:
            dados[p.name] = yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            erro(f"{p.name}: YAML inválido ({e})")
    return dados


def validar_indice(mapeamento):
    linhas = list(csv.DictReader(INDICE.open(encoding="utf-8-sig")))
    ids = [l["ID"] for l in linhas]
    vistos = set()
    for i in ids:
        if i in vistos:
            erro(f"índice: ID duplicado {i}")
        vistos.add(i)
    for l in linhas:
        if l["ID_PAI"] and l["ID_PAI"] not in vistos:
            erro(f"índice: {l['ID']} aponta para ID_PAI inexistente {l['ID_PAI']}")
    campos = {l["ID"] for l in linhas if l["TIPO"] == "CAMPO"}
    if mapeamento:
        total = mapeamento["total_campos"]
        mapeados = {str(c["id"]) for c in mapeamento["campos"]}
        if len(campos) != total:
            erro(f"índice: {len(campos)} campos; esperado {total}")
        if campos != mapeados:
            erro(f"índice x mapeamento divergem: {sorted(campos ^ mapeados)}")
    return linhas


def validar_manifesto():
    padrao = re.compile(r"^SRC-[0-9]{6}$")
    vistos = set()
    for l in csv.DictReader(MANIFESTO.open(encoding="utf-8")):
        fid = l["fonte_id"]
        if not padrao.match(fid) or fid in vistos:
            erro(f"manifesto: fonte_id inválido ou duplicado {fid}")
        vistos.add(fid)
        if l["disponibilidade"] != "DISPONIVEL":
            continue
        arq = RAIZ / l["uri_ou_caminho"]
        if not arq.is_file():
            erro(f"manifesto: {fid} marcado DISPONIVEL mas {arq} não existe")
        elif hashlib.sha256(arq.read_bytes()).hexdigest() != l["sha256"]:
            erro(f"manifesto: sha256 de {fid} não confere")


def validar_pastas(controles):
    cat = controles["catalogos"]
    for a in cat["macroareas"]:
        if not list((RAIZ / "20_manual_referencia").glob(f"{a['id']}_*/README.md")):
            erro(f"manual: pasta da macroárea {a['id']} ausente")
    for s in cat["secoes_operacionais"]:
        if not list((RAIZ / "30_caderno_operacional").glob(f"{s['id']}_*/README.md")):
            erro(f"caderno: pasta da seção {s['id']} ausente")


def validar_documentos(controles):
    macro = {a["id"] for a in controles["catalogos"]["macroareas"]}
    reg_ids = {}
    for p in RAIZ.rglob("REG-*.md"):
        texto = p.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
        rel = p.relative_to(RAIZ)
        if not m:
            erro(f"{rel}: sem front matter")
            continue
        fm = yaml.safe_load(m.group(1)) or {}
        rid = fm.get("registro_id", "")
        if not re.match(r"^REG-[0-9]{6}$", str(rid)) or rid == "REG-000000":
            erro(f"{rel}: registro_id inválido {rid}")
        elif rid in reg_ids:
            erro(f"{rel}: registro_id {rid} duplicado com {reg_ids[rid]}")
        else:
            reg_ids[rid] = rel
        if not p.name.startswith(f"{rid}_"):
            erro(f"{rel}: nome do arquivo não começa com {rid}_")
        if fm.get("macroarea_principal") not in macro:
            erro(f"{rel}: macroarea_principal inválida")
        if not fm.get("origens"):
            erro(f"{rel}: origens vazio (mínimo 1)")
    return reg_ids


def main():
    dados = validar_schemas()
    validar_indice(dados.get("02_MAPEAMENTO_94_IDS.yaml"))
    validar_manifesto()
    controles = dados.get("03_CONTROLES_EXCEL.yaml")
    if controles:
        validar_pastas(controles)
        regs = validar_documentos(controles)
    else:
        erro("03_CONTROLES_EXCEL.yaml ausente")
        regs = {}
    if erros:
        print(f"FALHOU — {len(erros)} erro(s):")
        for e in erros:
            print(f"  - {e}")
        return 1
    print(f"OK — schemas, índice, manifesto, pastas e {len(regs)} documento(s) REG validados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
