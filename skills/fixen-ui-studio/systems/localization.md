# Localization and Locale-Aware UI

Use when the product has more than one language or region, when the brief names a market, or when copy, currency, dates, or text direction affect layout. For a single-language product, preserve its language and conventions and skip the rest.

## 1. Decide locale facts separately
Language, region, currency, and time zone are four independent choices. A page in Indonesian can price in USD; a page in English can serve Jakarta. Record each in the blueprint (`templates/design-blueprint.md`) and do not infer one from another.

## 2. Message structure
- One complete message per key. Never build sentences by concatenating fragments, because word order differs by language.
- Keep variables inside the message (`"{count} item"`), and use the project's plural/select mechanism (ICU MessageFormat or equivalent) where it exists. Some languages have no plural forms (Indonesian, Japanese); others have several (Arabic, Polish).
- Do not hard-code copy inside components when the project already has a message catalog.
- Machine-translated or generated translations of legal, medical, financial, or price copy need human review. Say so in the handoff instead of presenting them as final.

## 3. Formats
Prefer platform APIs over hand-written formats: `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, `Intl.ListFormat`.
- Currency: `new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 })` renders Rupiah without decimals. JPY also has no minor unit; most others use two.
- Separators swap by locale (`1.234,50` vs `1,234.50`). Never parse a displayed number.
- Dates: store ISO/UTC, display in the user's or business's zone, and show the zone when it matters (booking, opening hours).
- Names, addresses, and phone numbers: do not assume first/last name, postal-code shape, or a fixed phone length. Use one flexible "full name" field unless the backend needs more.

## 4. Text expansion and contraction
English strings are often shorter than German, Finnish, or Indonesian equivalents (plan for roughly 30–40% growth in short UI labels), while CJK text is shorter but taller. Design buttons, tabs, and table headers to wrap or grow instead of clipping. Test with a long pseudo-string, not only the shortest label.

## 5. Fonts and scripts
- Confirm the chosen font covers the script. If not, declare a fallback stack per script and check that metrics do not shift the layout.
- Set `lang` on `<html>`, and on inline fragments in another language, so hyphenation, quotes, screen readers, and font selection work.
- Avoid letter-spacing on connected scripts such as Arabic. Avoid faux italics for CJK. For CJK, check line-breaking (`word-break`, `line-break`) rather than assuming spaces.
- Use typographic quotes native to the language in copy a reader sees; keep straight quotes in code.

## 6. Direction (RTL)
- Set `dir="rtl"` on the document or the relevant subtree, not per element.
- Use CSS logical properties (`margin-inline-start`, `padding-inline`, `inset-inline-end`, `text-align: start`) instead of left/right.
- Mirror directional icons (arrows, back/forward, progress) and layout order; do not mirror logos, clocks, media transport controls, or numerals in running code.
- Mixed content (a Latin product name inside Arabic) needs `<bdi>` or `unicode-bidi: isolate`.

## 7. Language selector
- Label each language in its own name (`Bahasa Indonesia`, `العربية`), not with a flag, because flags represent countries.
- Do not silently switch language from browser or IP guesses; offer it and remember the choice.
- Keep the selector reachable by keyboard and mark the current language (`aria-current`).
- When URLs differ by language, link alternates with `hreflang`.

## 8. Culture and imagery
Check color meanings, gestures, and sample names/photos for the target market. Do not use a single stereotype to stand for a region. Real people, places, and brands in sample content need the same sourcing care as any other image (`design/asset-sourcing.md`).

## 9. What to report
State the locales and interactions actually checked (rendered, static-only, or not run). Do not claim a language or RTL layout works because the text was translated.
