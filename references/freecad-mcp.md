# FreeCAD MCP workflow

Use this route for existing FCStd documents, assemblies, imported hardware, enclosure development, and tasks that need interactive FreeCAD state.

## Connection and document safety

1. Check MCP health before mutating a document.
2. Open the requested document or inspect already-open documents; do not create a duplicate source document unnecessarily.
3. Save development work to a new revision unless the user explicitly wants the original overwritten.
4. Keep arbitrary FreeCAD Python execution disabled unless a typed tool cannot perform the required operation and the user-authorized task requires it.
5. After a timeout, inspect operation status before retrying or issuing another mutation.

## Tool routing

Prefer typed MCP operations for document/object inspection, bounding boxes, placements, primitive and shell creation, booleans, edge finishing, splits, enclosure features, collision checks, screenshots, and STEP/STL exchange.

For advanced enclosure tools, use the installed server's available capabilities for tongue-and-groove joints, alignment features, snap-fits, ribs, heat-set insert profiles, louvers, minimum-wall analysis, overhang analysis, print-bed fit, part packing, screwdriver access, and cable/adapter swept volumes. Discover the current tool list rather than assuming a specific server version.

If an advanced typed tool is absent:

- do not emulate it with unrestricted Python merely for convenience;
- construct geometry with safe typed primitives where practical;
- use bounding boxes, collision checks, sectioned test bodies, or exported-mesh analysis as conservative evidence;
- state which check remains approximate.

## Validation cadence

After each structural phase:

1. recompute and inspect affected objects;
2. run geometry validity checks;
3. compare bounding boxes and placements with intended parameters;
4. check collisions with component and keep-out envelopes;
5. capture a useful view and inspect it;
6. save a revision only after the checks pass.

Before final export, verify assembly access, part separation, print orientation, bed fit, and round-trip one representative STEP and STL artifact when practical.
