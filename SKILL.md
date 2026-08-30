---
name: parametric-3d-printing
description: Design and validate manufacturable parametric parts and enclosures with FreeCAD MCP or CadQuery. Use for FDM-ready cases, brackets, mounts, joints, ventilation, fit checks, STL/STEP export, and existing FCStd models; do not use for digital-only art or animation.
---

# Parametric CAD for Codex

Produce editable geometry, printable exports, and evidence that the design fits its real components and manufacturing limits.

## Choose the modeling route

- Use **FreeCAD MCP** when an FCStd document already exists, the design contains an assembly or imported hardware, or placement, BREP inspection, collision checking, and continued interactive editing matter. Read [references/freecad-mcp.md](references/freecad-mcp.md).
- Use **CadQuery** for isolated parametric parts, fast headless iteration, regression fixtures, or when no live FreeCAD document is involved.
- Use a **hybrid workflow** for enclosure projects: keep the assembly and authoritative geometry in FreeCAD; use CadQuery only for independent generated parts or test fixtures, exchanging STEP where editability matters and STL only for print validation.
- For the BC250 enclosure project, also read [references/bc250-enclosure.md](references/bc250-enclosure.md).

Do not replace an editable FCStd/STEP source with mesh-only geometry unless the user explicitly accepts that loss.

## Work autonomously

Inspect available models, files, metadata, and authoritative dimensions before asking questions. Make reversible engineering assumptions explicit and continue. Ask only when a missing physical measurement or design choice can invalidate fit, safety, airflow, or assembly.

Build in logical phases—envelope, interfaces, functional features, finish—but do not stop for approval after every phase unless the user requests checkpoints. Render and self-review each meaningful phase. Surface progress in concise commentary while continuing.

## Engineering workflow

1. Establish the source of truth, units, coordinate system, component envelopes, keep-outs, printer volume, material, nozzle, and service requirements.
2. Research or measure real interfaces. Never guess connector bodies, mounting patterns, cable bend radii, PSU envelopes, or fastener geometry when fit depends on them. Record each value's source or mark it as an assumption.
   For reference meshes, run `scripts/measure_reference_mesh.py` and retain its hash, bounds, extents, units assumption, and validity result with the design evidence.
3. Put user-adjustable dimensions and tolerances in one parameter section. Use descriptive names and millimetres.
4. Build the simplest valid solids first. Add interfaces and clearances before cosmetic details. Preserve recoverable intermediate parts and meaningful object names.
5. Validate geometry and assembly after material changes. Fix root causes of failed booleans, self-intersections, zero-thickness faces, or non-manifold meshes.
6. Check printability and serviceability before export. Read [design-review.md](design-review.md) for the mesh and visual review loop.
7. Export editable sources plus manufacturing artifacts and retain a preview and validation summary.

## CadQuery execution

CadQuery requires Python 3.10–3.12. Use a dedicated environment; do not install it into a Python 3.13 FreeCAD/MCP environment.

Run a model and generate a strict preview:

```bash
python run_cadquery_model.py model.py --preview --strict
```

If the command reports an error or a non-watertight mesh, correct the model and rerun it. Use `preview.py` for render-only checks and `stl_to_3mf.py` when a 3MF artifact is required. For Gridfinity, reuse `gridfinity.py` rather than recreating the base profile.

CadQuery scripts must:

- expose dimensions, material allowances, fit clearances, and printer assumptions as parameters;
- place the intended print surface consistently at Z=0;
- prefer robust constructive geometry and avoid silent fallback around failed fillets or booleans;
- export STL with explicit tessellation tolerances and STEP when future CAD editing is useful;
- export each printable part separately.

## Release gate

Before calling a design printable, verify all applicable items:

- critical dimensions and component clearances match their sources;
- solids are valid and exported meshes are watertight;
- minimum walls and features suit the nozzle, material, and loads;
- overhangs, bridges, orientation, and support strategy are understood;
- every printable part fits the configured build volume in at least one allowed orientation;
- joints, pins, snap-fits, threaded inserts, fasteners, and tool access have usable clearances;
- cables and rigid/90-degree adapters have collision-free swept volumes and acceptable bend radii;
- ventilation openings, louvers, ribs, and mounting bosses do not conflict with components;
- multi-part exports are named, oriented, and laid out deliberately;
- the preview has been inspected from multiple useful views.

If a required automated check is unavailable, report the missing evidence and use a conservative geometric proxy; do not silently mark it passed.

## Deliverables

Return the editable source (`FCStd` and/or parameterized Python), STEP where interchange matters, one STL per printable part, a multi-view preview, and a concise validation report. Include key parameters, unresolved assumptions, print orientation, material, layer height, wall count, infill, and support notes.
