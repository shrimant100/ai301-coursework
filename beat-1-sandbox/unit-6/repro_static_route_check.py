"""One-off repro helper for OWASP/Nest #5259 (not for upstream PR)."""
from __future__ import annotations

import ast
import re
from datetime import UTC, datetime
from pathlib import Path

NEST_ROOT = Path(__file__).resolve().parent.parent.parent.parent / "Nest"
BASE = NEST_ROOT / "backend/src/apps/sitemap/views/base.py"
STATIC = NEST_ROOT / "backend/src/apps/sitemap/views/static.py"


def static_route_paths(base_py: str) -> list[str]:
    paths = re.findall(r'"path":\s*"([^"]+)"', base_py)
    return paths


def mapped_paths(static_py: str) -> set[str]:
    tree = ast.parse(static_py)
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [k.value for k in node.keys if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "/chapters" in keys and "/projects" in keys:
                return set(keys)
    raise RuntimeError("path_to_model dict not found")


def main() -> None:
    base_text = BASE.read_text(encoding="utf-8")
    static_text = STATIC.read_text(encoding="utf-8")
    routes = static_route_paths(base_text)
    mapped = mapped_paths(static_text)
    unmapped = [p for p in routes if p not in mapped]

    print(f"commit: run from Nest clone at {NEST_ROOT}")
    print(f"STATIC_ROUTES ({len(routes)}): {', '.join(routes)}")
    print(f"path_to_model keys ({len(mapped)}): {', '.join(sorted(mapped))}")
    print(f"unmapped static routes: {unmapped}")
    print()
    print("Simulated StaticSitemap.lastmod branch (missing key => datetime.now fallback):")
    now = datetime.now(UTC)
    for path in ("/repositories", "/projects", "/chapters"):
        if path in mapped:
            print(f"  {path}: would call model.objects.aggregate(Max('updated_at'))")
        else:
            print(f"  {path}: datetime.now(UTC) => {now.isoformat()}")


if __name__ == "__main__":
    main()
