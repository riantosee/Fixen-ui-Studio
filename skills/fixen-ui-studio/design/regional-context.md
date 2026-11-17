# Regional and Local-Business Context

Use when the brief names a market, a small or local business, or an audience whose habits differ from a generic global SaaS user. Infer what you can from the brief; ask or placeholder what only the business knows.

## Business facts are not copy
Headlines, descriptions, and microcopy can be inferred and written. These cannot: business name, prices, address, opening hours, phone/WhatsApp/social handles, payment methods accepted, certifications or labels (for example halal, organic), reviews, ratings, customer counts, awards. Use what the user supplied. For the rest, use a visible bracketed placeholder (`[HARGA]`, `[ALAMAT]`, `[JAM BUKA]`), keep it easy to find, and list every placeholder in the handoff. Never invent testimonials, statistics, or claims to make a page look finished.

## Local-business page pattern
Order of need for a walk-in or order-by-chat business: what it is and sells → menu or catalogue with prices → how to order or reach it → where and when → proof that is real. Make the primary action one tap on a phone (call, chat, map, or order link). Put hours and location near the action, not buried in a footer.

## Worked example: Indonesia
- **Order by chat.** WhatsApp links use `https://wa.me/<number>` with country code and no `+`, spaces, or leading zero (`62…`). An optional `?text=` prefills the message (URL-encode it). Do not ship a fake number; use a placeholder until given one.
- **Currency.** Rupiah is written `Rp 15.000` (dot as thousands separator, usually no decimals). Use `Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 })`.
- **Payment cues.** Show only methods the business confirms: cash, bank transfer, e-wallet, QRIS, cash on delivery. Do not show logos or badges for methods not confirmed.
- **Time zones.** Indonesia spans WIB, WITA, and WIT. Show the zone on opening hours if customers may be elsewhere.
- **Register.** Choose deliberately between casual (`kamu`) and formal (`Anda`) to match the brand; keep it consistent. Avoid literal translations of English marketing idioms.
- **Devices and data.** Design mobile-first for mid-range phones and variable connections: light pages, compressed and correctly sized images, system-font fallbacks, no autoplay video, and no critical content that waits on a large script.
- **Tap targets and thumbs.** Primary actions reachable at the bottom half of a phone screen; at least 44 px tap targets.

## Other markets
Run the same checklist: naming and address conventions, phone format, usual order or payment channel, trading days and holidays, legal text required by the business type, and reading direction. Ask only when a missing answer would change the result; otherwise state the assumption.

## Boundaries
Regional context sharpens a design; it must not become stereotype. Do not decorate with national symbols or cultural motifs unless the brief asks and the motif fits the product.
