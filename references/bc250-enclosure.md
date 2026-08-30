# BC250 enclosure project profile

Use this reference only for the BC250 console-style enclosure project.

## Known project inputs

- Component dimensions and model identity are recorded in [bc250-components.yaml](bc250-components.yaml). Read it before creating or moving enclosure geometry.
- Compute board: AMD BC250. The authoritative project reference is the detailed `amd-bc-250.stl` whose SHA-256 and exact mesh bounds are recorded in the component profile. Verify the file with `scripts/measure_reference_mesh.py`; do not silently substitute `bc250.stl` or a simplified bounding box.
- Power supply: Dell N870P-S0. Its nominal metal enclosure is 206 × 76 × 67 mm. Model that exact solid envelope plus separate parameterized clearance and interface keep-outs. The envelope does not define the fan opening, hot-swap connector, AC inlet, handle, latch, or mounting features.
- Printer build volume: 256 × 256 × 256 mm.
- Aesthetic direction: compact Xbox One X-inspired horizontal enclosure with a restrained two-part exterior, black lower band, white upper shell, and integrated ventilation.
- Documentation sources:
  - https://github.com/mothenjoyer69/bc250-documentation
  - https://bc-250.com/wiki
  - https://bc-250.com/cad
  - https://bc-250.com/
  - https://github.com/elektricM/amd-bc250-docs

Do not infer mechanical dimensions from photographs. Label unverified dimensions and keep them parameterized.

## Reference geometry procedure

1. Locate the BC250 reference STL and verify its SHA-256 against `bc250-components.yaml`.
2. Measure the mesh in millimetres and compare all three coordinate extents within the profile tolerance. STL files are unitless, so the millimetre assumption must be explicit.
3. Import the verified mesh into the FreeCAD assembly without scaling. Preserve its source origin and record any placement transform separately.
4. Create collision and mounting geometry from the detailed mesh, not only its bounding box. Use the PCB outline only for cross-checking orientation.
5. Create a separate Dell PSU envelope solid at 206 × 76 × 67 mm. Add independent keep-out objects for insertion/removal travel, exhaust, connector/adapter, mains wiring, and cable bend radius.
6. When a measured PSU model becomes available, replace the nominal PSU envelope and rerun every collision, screwdriver, cable-sweep, and bed-split check affected by it.

Example verification:

```powershell
python scripts/measure_reference_mesh.py C:\Users\Alex\Downloads\amd-bc-250.stl `
  --expect-sha256 9D6880DD5BADDD6F24315B0AD206D83C2323033A163C96A561351DBAEDA0E832 `
  --expect-extents 31.499878 312.156800 143.772300 --tolerance 0.05
```

## Required construction features

- parameterized tongue-and-groove seams;
- alignment pins and receiving holes;
- printable snap-fit latches where maintenance permits;
- stiffness ribs that avoid airflow and component keep-outs;
- standard heat-set insert profiles with material-appropriate pilot geometry;
- angled louvers with controlled blade angle, spacing, and minimum thickness;
- serviceable fasteners with verified screwdriver approach volumes;
- cable routes checked across installation motion and final bend radius, including rigid 90-degree adapters.

## Required release evidence

- minimum-wall analysis for every printable shell;
- FDM overhang analysis in the intended orientation;
- independent 256 × 256 × 256 mm bed-fit result for every part;
- automatic non-overlapping export layout where useful;
- collisions checked with BC250, PSU, cooling, connectors, fasteners, and cable swept volumes;
- the BC250 evidence records a matching reference-mesh hash and extents;
- the Dell evidence distinguishes the 206 × 76 × 67 mm body from every interface and service keep-out;
- intake and exhaust paths remain unobstructed;
- each service operation can be performed without removing unrelated permanent joints;
- final FCStd revision, one STL per printable part, STEP interchange exports, preview images, and a validation report.

Passing the bounding-box check alone is not sufficient to authorize a full print. Unknown PSU, connector, cooling, or fastener geometry remains a release blocker for the affected interfaces.
