#!/usr/bin/env python3
"""Measure and identify a reference STL for repeatable enclosure work."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import trimesh


def measure_mesh(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    mesh = trimesh.load_mesh(path, force="mesh")
    if mesh.is_empty:
        raise ValueError(f"Mesh is empty: {path}")

    return {
        "path": str(path.resolve()),
        "sha256": hashlib.sha256(data).hexdigest().upper(),
        "units_assumption": "mm",
        "bounds_min_xyz": [float(value) for value in mesh.bounds[0]],
        "bounds_max_xyz": [float(value) for value in mesh.bounds[1]],
        "extents_xyz": [float(value) for value in mesh.extents],
        "vertices": int(len(mesh.vertices)),
        "faces": int(len(mesh.faces)),
        "watertight": bool(mesh.is_watertight),
        "volume_mm3": float(mesh.volume),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report STL identity and dimensions, optionally enforcing expected values."
    )
    parser.add_argument("mesh", type=Path)
    parser.add_argument("--expect-sha256")
    parser.add_argument("--expect-extents", type=float, nargs=3, metavar=("X", "Y", "Z"))
    parser.add_argument("--tolerance", type=float, default=0.05)
    args = parser.parse_args()

    result = measure_mesh(args.mesh)
    checks: dict[str, Any] = {}

    if args.expect_sha256:
        checks["sha256_matches"] = result["sha256"] == args.expect_sha256.upper()
    if args.expect_extents:
        deltas = [
            abs(actual - expected)
            for actual, expected in zip(result["extents_xyz"], args.expect_extents)
        ]
        checks["extent_deltas"] = deltas
        checks["extents_match"] = all(delta <= args.tolerance for delta in deltas)

    result["checks"] = checks
    result["verified"] = all(
        value for key, value in checks.items() if key.endswith("_matches") or key.endswith("_match")
    ) if checks else None
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["verified"] is not False else 1


if __name__ == "__main__":
    raise SystemExit(main())
