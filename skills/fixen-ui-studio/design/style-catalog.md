# Style and Composition Catalog

Use as a vocabulary, not as presets to apply blindly.

## Direction families
- Swiss / International: grid discipline, typography, clarity, deliberate asymmetry.
- Editorial luxury: strong type, generous whitespace, restrained palette, image-led storytelling.
- Technical minimalism: precise data hierarchy, compact controls, clear system feedback.
- Neo-brutalist: assertive type, strong borders, deliberate rawness, high contrast.
- Organic / human: warm colors, softer forms, approachable language and imagery.
- Immersive / cinematic: large visual fields, layered depth, controlled motion.
- Playful product: expressive shapes, illustration, friendly microcopy, clear task flow.
- Data-dense operations: compact but legible tables, filtering, status hierarchy, keyboard efficiency.
- Commerce editorial: product focus, trust cues, discovery, comparison, conversion clarity.
- Experimental portfolio: unusual composition, strong narrative, controlled interaction.

## Composition patterns
- Editorial grid, split hero, bento (only when content supports it), asymmetric columns
- Sidebar + workspace, master-detail, command center, timeline, table-first
- Product gallery, comparison layout, narrative scroll, case-study chapters
- Mobile bottom navigation, task-focused single column, progressive disclosure

## Selection test
Ask: Does this direction reinforce the product's promise and make the primary task easier? If not, reject it.

## Direction recipes
Starting points for turning a family into decisions. They are vocabulary, not templates; change at least two decisions to fit the product. Fonts named are widely available examples; check licensing and loading in the project.

| Direction | Typography | Color logic | Composition signature | Avoid |
|---|---|---|---|---|
| Swiss / International | Neutral grotesk, one family, strong size contrast | Near-white ground, near-black ink, one signal accent | Visible grid, flush-left text, asymmetric whitespace | Decorative gradients, centered everything |
| Editorial luxury | High-contrast serif display with a quiet sans body | Warm neutral ground, ink, one muted accent | Large imagery, narrow text column, generous margins | Cramped cards, loud buttons |
| Technical minimalism | Sans plus a monospace for data | Cool neutrals, status colors with text labels | Dense aligned tables, compact controls | Color as the only status signal |
| Neo-brutalist | Heavy grotesk, tight leading | Flat saturated fills, black outlines | Hard borders, offset blocks, raw grid | Soft shadows, unreadable low contrast |
| Organic / human | Rounded or humanist type | Earth tones, ink never pure black | Soft but varied shapes, real photography | Identical pill buttons everywhere |
| Warm local commerce | Friendly display for names, plain sans for prices | Cream or kraft ground, ink, one food- or brand-derived accent | Price-board lists, large product visual, one-tap order action | Stock-photo grids, invented reviews, fake badges |
| Data-dense operations | Tabular figures, small but legible | Quiet ground, strong status hierarchy | Filters, sticky headers, keyboard flow | Decorative charts |

## Palette construction
1. Choose a ground and an ink with at least 7:1 contrast.
2. Add one accent that carries the primary action; test it as text on the ground and as a fill with text on it (4.5:1 for body text, 3:1 for large text and UI boundaries).
3. Add at most one supporting hue from the product's world (a food, material, or place), used sparingly.
4. Derive tints by mixing with the ground, not by adding gray.

## Type pairing
Pair by contrast of role, not decoration: a distinctive display face for names and headlines with a plain, readable text face for body and data. Limit to two families and few weights. Check script coverage before committing (`systems/localization.md`).

## Differentiators
Choose at most three: composition, typography, color, imagery, interaction, content. If every dimension is loud, nothing leads.

