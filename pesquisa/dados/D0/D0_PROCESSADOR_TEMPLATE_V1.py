"""D0 processor template — no physical data are generated.

Reads the D0 raw CSV when populated and produces a separate processed CSV.
It preserves missing values and refuses to turn placeholders into measurements.
"""

from __future__ import annotations
import csv
import math
from pathlib import Path

RAW = Path("pesquisa/dados/D0/D0_GEOMETRIA_BRUTO.csv")
OUT = Path("pesquisa/dados/D0/D0_GEOMETRIA_PROCESSADO.csv")

def valid_number(value: str) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if not value or value.upper() in {"NÃO MEDIDO", "NAO MEDIDO", "NÃO CALCULADO", "NAO CALCULADO"}:
        return None
    try:
        return float(value)
    except ValueError:
        return None

def sample_std(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / (len(values) - 1))

def process() -> None:
    if not RAW.exists():
        raise FileNotFoundError(RAW)

    groups: dict[tuple[str, str, str], list[float]] = {}
    with RAW.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            x = valid_number(row.get("valor_bruto", ""))
            if x is None:
                continue
            key = (row.get("componente", ""), row.get("grandeza", ""), row.get("unidade", ""))
            groups.setdefault(key, []).append(x)

    rows = []
    for (component, quantity, unit), values in groups.items():
        mean = sum(values) / len(values)
        s = sample_std(values)
        u_a = s / math.sqrt(len(values)) if s is not None and len(values) >= 2 else None
        rows.append({
            "id": f"D0-PROC-{len(rows)+1:04d}",
            "componente": component,
            "grandeza": quantity,
            "unidade": unit,
            "n_repeticoes": len(values),
            "media": mean,
            "desvio_padrao": s if s is not None else "NÃO CALCULADO",
            "incerteza_tipo_A": u_a if u_a is not None else "NÃO CALCULADO",
            "incerteza_tipo_B": "PENDENTE",
            "incerteza_combinada": "NÃO CALCULADO",
            "status": "PROCESSADO",
            "observacao": "Origem rastreável em D0_GEOMETRIA_BRUTO.csv",
        })

    if not rows:
        return

    fields = list(rows[0].keys())
    write_header = not OUT.exists() or OUT.stat().st_size == 0
    with OUT.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    process()
