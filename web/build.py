#!/usr/bin/env python3
"""Genera web/index.html (un único archivo autocontenido) a partir de
web/data/guia.json y web/src/template.html.

Uso:  python3 web/build.py
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "guia.json"
TEMPLATE = ROOT / "src" / "template.html"
OUT = ROOT / "index.html"


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    errors, seen = [], set()

    # IDs estables: el progreso del jugador se guarda por ID, así que
    # no cambies un ID existente aunque renombres la misión.
    for ch in data["chapters"]:
        for m in ch["missions"]:
            m.setdefault("id", slug(m["n"]))
            if m["id"] in seen:
                errors.append(f"ID duplicado: {m['id']} (pon un 'id' explícito)")
            seen.add(m["id"])
            if m.get("w") not in data["legend"]["who"]:
                errors.append(f"{m['id']}: protagonista desconocido {m.get('w')}")
            if m.get("t") not in data["legend"]["type"]:
                errors.append(f"{m['id']}: tipo desconocido {m.get('t')}")

    for m in (m for ch in data["chapters"] for m in ch["missions"]):
        if m.get("after") and m["after"] not in seen:
            errors.append(f"{m['id']}: 'after' apunta a un ID inexistente {m['after']}")
    for g in data["gates"]:
        for ref in [g["before"], *g.get("requires", []), *g.get("recommended", [])]:
            if ref not in seen:
                errors.append(f"Punto de control '{g['title']}': ID inexistente {ref}")
    for s in data["secrets"]:
        if s["s"] not in data["legend"]["status"]:
            errors.append(f"Secreto {s['id']}: estado desconocido {s['s']}")

    if errors:
        print("ERRORES:\n  " + "\n  ".join(errors))
        return 1

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__GUIDE_DATA__", payload)
    OUT.write_text(html, encoding="utf-8")
    total = sum(len(ch["missions"]) for ch in data["chapters"])
    print(f"OK → {OUT.relative_to(ROOT.parent)} · {total} misiones · {len(data['secrets'])} secretos · {len(data['completion'])} requisitos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
