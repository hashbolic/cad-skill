import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)


@pytest.fixture
def tmp_stl(tmp_path):
    """Generate a watertight 10mm cube STL on demand."""
    import trimesh

    stl = tmp_path / "cube.stl"
    trimesh.creation.box(extents=(10, 10, 10)).export(stl)
    return stl


@pytest.fixture
def good_script(tmp_path):
    """CadQuery script that writes a watertight cube next to itself."""
    script = tmp_path / "good_model.py"
    script.write_text(
        "import cadquery as cq\n"
        "r = cq.Workplane('XY').box(10, 10, 10)\n"
        "cq.exporters.export(r, 'good_model.stl',"
        " tolerance=0.01, angularTolerance=0.1)\n"
    )
    return script


@pytest.fixture
def step_script(tmp_path):
    """CadQuery script that writes both an STL and a STEP next to itself."""
    script = tmp_path / "step_model.py"
    script.write_text(
        "import cadquery as cq\n"
        "r = cq.Workplane('XY').box(10, 10, 10)\n"
        "cq.exporters.export(r, 'step_model.stl',"
        " tolerance=0.01, angularTolerance=0.1)\n"
        "cq.exporters.export(r, 'step_model.step')\n"
    )
    return script


@pytest.fixture
def bad_script(tmp_path):
    """CadQuery script that raises (fillet radius too large)."""
    script = tmp_path / "bad.py"
    script.write_text(
        "import cadquery as cq\n"
        "cq.Workplane('XY').box(10, 10, 10).edges('|Z').fillet(99)\n"
    )
    return script


@pytest.fixture
def empty_script(tmp_path):
    """Script that exits 0 without writing any STL."""
    script = tmp_path / "empty.py"
    script.write_text('print("no export called")\n')
    return script
