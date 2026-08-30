from __future__ import annotations

import hashlib
from pathlib import Path

import trimesh

from scripts.measure_reference_mesh import measure_mesh


def test_measure_mesh_reports_identity_and_extents(tmp_path: Path) -> None:
    path = tmp_path / "reference.stl"
    trimesh.creation.box(extents=(10.0, 20.0, 30.0)).export(path)

    measured = measure_mesh(path)

    assert measured["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest().upper()
    assert measured["extents_xyz"] == [10.0, 20.0, 30.0]
    assert measured["watertight"] is True
