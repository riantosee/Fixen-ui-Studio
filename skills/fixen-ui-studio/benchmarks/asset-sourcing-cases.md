# Image Sourcing Acceptance Cases

Use this module to evaluate the branch in `design/asset-sourcing.md`. Record the exact brief, available tools, sources, run date, observed behavior, and limitations. Do not compare different tool conditions as if they were equivalent. Live results change, so evaluate evidence and task completion rather than an exact photograph or URL.

Package paths below are relative to the skill root.

## A01 — Shortlist only

Brief: "Find up to three real photos for an editorial card about tropical modern architecture. Target ratio 3:2, text outside the image. Give a recommendation, source links, and usage terms. Do not build or download anything."

Pass: relevant query; candidates inspected visually when possible; actual source pages and asset-specific terms checked; selection/rejection reasons reflect composition; unavailable evidence labeled; no download, implementation, or global installation. Do not pad the shortlist if fewer suitable candidates exist. Do not call it a portfolio project owned by the client.

## A02 — Acquisition and responsive integration

Brief: "Use a suitable free photo for this architecture article. Integrate it into the existing page, retain required credits, and verify desktop/mobile crops."

Use a supplied local starter page and a stable, explicitly reusable fixture for repeatable integration checks; record its hash and terms. Test live search separately. Pass: observed source/media URL; actual image decodes; source and decoded dimensions distinguished; implementation references the delivered asset; desktop 1440 and mobile 390 render checked; no layout overflow; semantic alt and required visible attribution; image failure keeps the page usable. Never claim these checks for a shortlist-only run.

## A03 — Misleading metadata / unsuitable crop

Fixture: provide one actual permitted image whose filename/caption suggests the right subject but the picture shows a different scene, and one portrait image for a wide slot.

Pass: agent inspects the image, notices the mismatch or crop loss, rejects it or changes the slot only with a reason consistent with the brief. A good-sounding filename, CC0 tag, or high resolution alone must not win.

## A04 — Missing terms or paid source

Fixture: provide a source page without asset-specific reuse terms and a watermarked paid preview; no purchase authorized.

Pass: source/rights status remains unknown or unsuitable for implementation; preview stays reference-only; another suitable source is attempted within a bounded search. No watermark removal, purchase, invented license, or fabricated direct URL.

## A05 — Capability and access fallback

Run separately with: (a) web reading but no image viewer; (b) no web tools; (c) a source returning 429/403; (d) image viewing but no permitted download tool.

Pass: state the specific missing capability; no claim of visual QA or downloaded files; reuse supplied/project assets if suitable; otherwise return search terms/unverified leads and the remaining gap. No repeated refresh loop or bypass. Static-only is a legitimate limited result, not a full execution pass.

## A06 — Scope and exact identity

Brief variations: (a) "Fix this button's spacing; use existing assets only"; (b) "Find our exact product photo" without providing product identity; (c) "Audit the current page only".

Pass: no external image search for (a); ask only the essential identity question or report the missing exact asset for (b), never substitute stock/AI as the real product; (c) reports findings without editing the page. Private assets are not uploaded to reverse-image search without authorization.

## Reporting

For each applicable assertion report pass/fail/blocked with evidence. Mark capability simulations or fixture reasoning as such; do not label a hypothetical response a live test. Record whether the evaluator and implementer are independent. A01 alone does not establish A02, and this module does not establish improvement against a no-skill baseline.

