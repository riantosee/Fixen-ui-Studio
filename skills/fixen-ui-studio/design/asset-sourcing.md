# Real Image Sourcing

Use for finding visual references or photos/illustrations needed by a UI. This is an optional branch of Fixen UI Studio, not an instruction to browse for every design task. The host's available tools and the user's request determine what can be done.

Package paths in this guide are relative to the skill root. Output paths follow the user's project conventions.

## 1. Define the slot, not just a keyword

Inspect supplied/project assets first. Reuse suitable material instead of searching again. For each needed image, state a brief containing:

- Purpose: reference, hero, editorial card, product detail, background, or supporting visual.
- Subject and factual context: what must really appear; whether an exact product, person, building, or place is required.
- Art direction: palette, light, mood, texture, composition, and consistency with adjacent images.
- Crop constraints: desktop and mobile ratios, focal point, and negative space if text overlays the image.
- Resolution/delivery needs appropriate to the actual rendered slot; avoid upscaling a thumbnail or downloading a huge master unnecessarily.
- User restrictions: supplied assets only, free or already licensed sources, selected providers, privacy, and any approved budget.

Use reasonable assumptions for a vague brief and state them. Ask only if a missing identity, source restriction, or paid choice blocks the task. A data dashboard often needs no external photography.

## 2. Choose an available retrieval path

Use the smallest path that provides evidence:

| Capability | Use | If unavailable |
|---|---|---|
| Image search | Discover visual candidates matching the brief | Web-search for specific asset pages |
| Web search / page reading | Verify the asset page, creator, dimensions, and terms | Read the page in a browser |
| Browser / image viewer | Inspect the actual picture and a sufficiently large preview | Keep visual suitability unverified; do not judge from the filename |
| Download / project file access | Acquire a selected asset through a source-permitted path | Deliver source links and mark download pending |
| UI rendering | Verify the actual delivered image, crop, contrast, and fallback | State static-only checks and pending render checks |

Prefer native search tools when available; use browser navigation for source pages, visual inspection, or sites whose relevant details require interaction. Tool names differ across hosts; follow the actual tool documentation. Do not invent tool calls, install a browser, or imply that this skill grants access.

## 3. Search intentionally

Build a concise query from subject + composition/material + setting, adding a provider restriction when useful. Try the user's language; English synonyms can broaden a sparse result set. Example: `tropical modern architecture exterior concrete landscape`.

Source examples, not a mandated provider list:

- Client/project media for exact products and authentic portfolio work.
- A creator's or institution's media page when it expressly permits the intended reuse.
- Stock libraries such as Unsplash or Pexels, checking current source terms and delivery requirements rather than assuming every image is unrestricted.
- Wikimedia Commons or public collections with individual file records, creator attribution, and asset-specific license information.
- Illustration libraries when their style and specific reuse terms suit the brief.

A search engine, moodboard, Pinterest pin, design gallery, or social post can point to inspiration; it is not itself evidence of permission to embed the underlying image. Never treat a search engine's licensing filter as sufficient proof.

For a small task, start with one focused query and inspect a few strong candidates. If it returns nothing or the wrong subject, make one focused rewrite or change source. Stop when a suitable set exists. If that attempt also fails, report the gap and continue with existing assets or a clearly labeled fallback. Do not pad a shortlist with off-topic images to meet a quota.

## 4. Inspect and shortlist

Open each promising asset page and visually inspect an adequate preview with the browser/image viewer. Record what was actually seen separately from page claims. The picture may not match its title, caption, or search thumbnail.

For a small image request, usually compare 2–3 candidates or as many as the user requested. A single strong exact match may suffice. Evaluate:

- Subject and product fit; no stock photo presented as evidence of a client's own work or results.
- Composition at the required ratio, focal point, background clutter, text placement, and mobile crop.
- Coherent light, palette, and visual language across a set; avoid mixing unrelated treatments.
- Adequate usable dimensions and image quality; visible watermarks or a tiny preview are not final assets.
- Source/usage confidence and whether its credit obligations can be met in the intended delivery.

Give a short selection/rejection reason. Do not invent numerical aesthetic scores. If visual review is unavailable, deliver candidates as unverified leads rather than visually approved selections.

## 5. Verify the individual source

Separate three questions: Does it look right? Does the source permit the intended use? Has the real file been acquired and tested?

Record the asset page URL, creator, license or usage-terms URL, original dimensions when available, and the date checked. Keep source-reported dimensions separate from dimensions decoded from a downloaded file. Mark unknowns explicitly.

Read file-specific licensing on collection sites. A footer that licenses page text or structured metadata does not automatically license the photograph. Keep attribution and adaptation requirements when applicable; do not assume a share-alike photo means the whole website must use that license. For provider APIs, follow their documented image-delivery and attribution rules.

If terms are missing, conflicting, or incompatible, keep the image reference-only or choose another suitable source. Do not buy a license, create an account, accept new terms, or spend credits merely because a page suggests it. Those actions need authorization appropriate to the task. Do not remove a watermark or bypass access controls. Use generic public search terms; do not upload private project media to a visual-search service without authorization.

## 6. Acquire and integrate only within the requested scope

For a shortlist/reference-only request, stop after recommendations and source links. A UI-build request that needs imagery normally includes selecting and integrating suitable assets, subject to source restrictions and the host's permissions.

Use download controls or media URLs actually observed on the source page; never guess CDN filenames, IDs, transformations, or extensions. A source-permitted derivative at adequate resolution may be better than an unnecessarily large original. Prefer project-local delivery when terms permit; preserve provider-required remote delivery when applicable. Do not use rotating/random-image URLs or transient search thumbnails as production dependencies.

When downloading, verify that the file exists, decodes as the expected image type, and has usable dimensions. Record the local path relative to the project and any resize/crop/format conversion. Do not execute downloaded content. Only mark it integrated after it is actually referenced by the implementation.

Use `templates/asset-register.md` for traceability when implementing or handing off a set. A small shortlist can keep the same information in chat; do not generate needless paperwork. Keep image licensing separate from the code license.

In the UI:

- Set intrinsic dimensions or a deliberate aspect ratio to reserve layout space.
- Set `object-fit` and `object-position` from the focal point, checking mobile separately; prefer a separate mobile source if needed and permitted.
- Optimize size with available project tools, using responsive sources where they help. Prioritize the above-fold primary image; lazy-load appropriate below-fold images.
- Provide contextual alt text for meaningful content and empty alt for purely decorative images. Required credits belong in visible credits, not only alt text or comments.
- If text overlays an image, test contrast on the actual crop. Move text to a solid surface when a safe overlay cannot be verified.
- Preserve a usable layout and honest fallback when the image fails. Do not silently replace an exact product image with an unrelated photo or AI-generated substitute.

## 7. Verify and report by stage

Track stages independently: source inspected, image visually inspected, terms checked, downloaded, integrated, and rendered. A later stage does not imply that earlier unknowns were resolved. A discovered URL is not a successful download; a successful download is not visual QA.

Render the actual implementation at representative desktop and mobile widths. Inspect the real network/local image, resolution, focal point, crop, overflow, alt behavior, loading stability, credit placement, and image-failure fallback. Record untested states without inventing results.

If a source is blocked, rate-limited, or requires login, use another relevant permitted source or a source-reading tool that already works; do not repeatedly refresh, evade restrictions, or use that as evidence of confirmed rights. A CDN preview may support visual review while the asset page remains unverified. Report this distinction.

Handoff should state what was selected and why, where the source/credit record is, what was actually acquired/integrated, what was rendered, and any remaining gap. Image discovery alone should never become a claim of production readiness.

