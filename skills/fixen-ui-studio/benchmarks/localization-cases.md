# Localization Evaluation Briefs

These are briefs, not recorded passing tests. Record the exact brief, tools available, fonts, viewports, run date, observed behavior, and limits. Do not compare runs under different tool conditions as equivalent. Paths below are relative to the skill root; see `systems/localization.md` for the guidance under test.

## L01 — Preserve an existing language
Brief: "Add a pricing section to this existing Indonesian landing page." Supply a starter page with Indonesian copy and `lang="id"`.
Pass: new copy is Indonesian in the same register as the page; `lang` unchanged; no English filler; prices use the page's existing format; no locale infrastructure added. Fail: translating the page to English, or adding an i18n library nobody asked for.

## L02 — Bilingual with RTL
Brief: "Make this product page available in English and Arabic with a language switcher."
Pass: `lang`/`dir` set per language; logical properties instead of left/right; directional icons mirrored, logo and media controls not; switcher labels languages in their own names without flags; mixed-direction strings isolated. State whether RTL was rendered or only reviewed in code.

## L03 — Currency, date, and time zone
Brief: "Show a checkout summary for the same cart in IDR, JPY, and EUR, with a delivery time for a Jakarta customer."
Pass: formats come from `Intl` or the project's formatter; IDR and JPY have no invented decimals; currency choice separate from language; delivery time shows its zone; no parsed display strings.

## L04 — Text expansion
Brief: "Localize the navigation, a primary button, and a data table header into German and Finnish."
Pass: layout wraps or grows without clipping at 390 px and 1440 px; no fixed-width buttons or `nowrap` truncation of key labels; long compound words handled (`overflow-wrap`, hyphenation with correct `lang`). Evidence: rendered screenshot or an explicit static-only label.

## L05 — CJK typography
Brief: "Create a Japanese-language article page with headings, body copy, and a pull quote."
Pass: font stack covers Japanese with sensible fallbacks; line-breaking checked; no faux italics or wide letter-spacing; `lang="ja"` set; line length and line height suited to the script. Fail: Latin font metrics applied unchanged.

## Scoring
Use `benchmarks/scoring-rubric.md`. Localization failures that block reading or the core task are core failures regardless of aesthetic score.
