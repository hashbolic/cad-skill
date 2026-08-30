# BC250 enclosure project profile

Use this reference only for the BC250 console-style enclosure project.

## Known project inputs

- Compute board: AMD BC250, represented by the user's FreeCAD model. Treat measured geometry in that model as the primary local source.
- Power supply: Dell N870P-S0. Require a measured model or authoritative dimensions for its complete envelope, mounting points, connector body, cable exit, and airflow direction before freezing interfaces.
- Printer build volume: 256 × 256 × 256 mm.
- Aesthetic direction: compact Xbox One X-inspired horizontal enclosure with a restrained two-part exterior, black lower band, white upper shell, and integrated ventilation.
- Documentation sources:
  - https://github.com/mothenjoyer69/bc250-documentation
  - https://bc-250.com/wiki
  - https://bc-250.com/cad
  - https://bc-250.com/
  - https://github.com/elektricM/amd-bc250-docs

Do not infer mechanical dimensions from photographs. Label unverified dimensions and keep them parameterized.

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
- intake and exhaust paths remain unobstructed;
- each service operation can be performed without removing unrelated permanent joints;
- final FCStd revision, one STL per printable part, STEP interchange exports, preview images, and a validation report.

Passing the bounding-box check alone is not sufficient to authorize a full print. Unknown PSU, connector, cooling, or fastener geometry remains a release blocker for the affected interfaces.
