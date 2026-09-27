"""Validador automatizado dos dados brutos da Fase D0.

Não cria nem corrige medições. Apenas verifica estrutura, integridade,
repetições, rastreabilidade básica e consistência H↔V quando houver
dados numéricos reais.
"""

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path(__file__).with_name("D0_GEOMETRIA_BRUTO.csv")
REQUIRED = [
    "id", "componente", "grandeza", "unidade", "metodo", "instrumento",
    "instrumento_id", "resolucao", "temperatura_c", "repeticao",
    "valor_bruto", "incerteza", "observacao", "data_hora", "status"
]
MISSING = {"", "NÃO MEDIDO", "NAO MEDIDO", "NÃO CALCULADO", "NAO CALCULADO"}
CRITICAL = {"D0-G01", "D0-G02", "D0-G03", "D0-G04", "D0-G05", "D0-G06", "D0-G07", "D0-G08"}

def num(value):
    if value is None or value.strip() in MISSING:
        return None
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return None

def main():
    if not RAW.exists():
        print(f"ERRO: arquivo não encontrado: {RAW}")
        return 2

    with RAW.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    errors, warnings = [], []

    if not rows:
        errors.append("CSV sem registros.")
    else:
        fields = set(rows[0].keys())
        for field in REQUIRED:
            if field not in fields:
                errors.append(f"Campo obrigatório ausente: {field}")

    ids = [r.get("id", "").strip() for r in rows]
    duplicates = [k for k, v in Counter(ids).items() if k and v > 1]
    if duplicates:
        errors.append(f"IDs duplicados: {duplicates}")

    by_group = defaultdict(list)
    for r in rows:
        group = r.get("grandeza", "").strip()
        if group in CRITICAL:
            by_group[group].append(r)

        value = r.get("valor_bruto", "").strip()
        if value and value not in MISSING and num(value) is None:
            errors.append(f"Valor não numérico em {r.get('id')}: {value}")

        if value not in MISSING and value != "" and not r.get("unidade", "").strip():
            errors.append(f"Unidade ausente para valor em {r.get('id')}.")

        if r.get("status", "").strip() not in {
            "ABERTO", "COLETADO", "REVISAR", "ACEITO", "REJEITADO", "PENDENTE"
        }:
            warnings.append(f"Status não padronizado em {r.get('id')}.")

    for group, group_rows in by_group.items():
        numeric = [num(r.get("valor_bruto", "")) for r in group_rows]
        numeric = [x for x in numeric if x is not None]
        if numeric and len(numeric) < 3:
            warnings.append(f"{group}: menos de 3 observações numéricas.")
        if not numeric:
            warnings.append(f"{group}: sem medição numérica; permanece pendente.")

    h, v = [], []
    for r in rows:
        g = r.get("grandeza", "").strip().upper()
        x = num(r.get("valor_bruto", ""))
        if x is None:
            continue
        if g in {"H", "ALTURA", "D0-G05"}:
            h.append(x)
        elif g in {"V", "VOLUME", "D0-G04"}:
            v.append(x)

    if h and v and len(h) == len(v):
        pairs = sorted(zip(h, v))
        for (h1, v1), (h2, v2) in zip(pairs, pairs[1:]):
            if h2 > h1 and v2 < v1:
                errors.append("H↔V não monotônica: volume diminuiu com aumento de altura.")
                break
    elif h or v:
        warnings.append("H↔V ainda não possui pares completos suficientes para teste.")

    print("=== D0 VALIDACAO AUTOMATIZADA ===")
    print(f"Arquivo: {RAW}")
    print(f"Registros: {len(rows)}")
    print(f"Erros: {len(errors)}")
    print(f"Alertas: {len(warnings)}")
    for item in errors:
        print(f"ERRO | {item}")
    for item in warnings:
        print(f"ALERTA | {item}")

    if errors:
        print("RESULTADO: REPROVADO")
        return 1
    if warnings:
        print("RESULTADO: PENDENTE — revisar alertas antes do fechamento D0")
        return 0
    print("RESULTADO: APTO PARA REVISÃO D0")
    return 0

if __name__ == "__main__":
    sys.exit(main())
