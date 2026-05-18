# Design System: Feng Yan Ce (烽烟策)

## 1. Visual Theme & Atmosphere

Feng Yan Ce is a mobile strategy game set in ancient warfare. Its visual identity is rooted in East Asian ink-brush aesthetics and classical culture — deep earthy browns, parchment-textured beige backgrounds, and punctuated quality-tier colors together construct a historically immersive battlefield atmosphere. The interface philosophy is "restrained yet ceremonious": UI elements recede into the background, allowing battle information and general quality to become the visual focal points.

The typography system is anchored by the Founder LiBian (方正隶变) typeface family. The stone-carved, archaic quality of the li-shu script aligns naturally with the game's classical aesthetic. Bold weight handles emphasis and titles; Regular weight handles information display. Together they establish a clear visual hierarchy without relying on font size alone.

The color system is split into two complete palettes: **Light Background (beige)** and **Dark Background (deep charcoal-black)**. Both palettes share identical semantic roles for text colors and quality colors, ensuring readability across different surface contexts. The quality color tier (Blue → Purple → Gold → Red) follows established RPG conventions, allowing players to intuit rarity levels without any learning curve.

**Key Characteristics:**
- Founder LiBian typeface family — archaic stone-carved aesthetic, Bold/Regular dual-weight hierarchy
- Dual background system: Light (`#f4f2ee` beige) and Dark (deep charcoal-black) for distinct contexts
- Quality color tier: Blue < Purple < Gold < Red — semantically unambiguous and cross-context consistent
- Modal background texture: large/medium/medium-small modals use a decorative texture anchored to the bottom-right corner, evoking ancient scroll aesthetics
- Strict semantic color roles: dedicated color values for headings, body text, secondary text, quality tiers, and faction relationships

---

## 2. Color Palette & Roles

### Light Background — Text Colors

| Hex | Role | Usage |
|-----|------|-------|
| `#321d14` | Primary Heading / Body | Highest-priority text on light backgrounds |
| `#593323` | Secondary Heading / Body 2 | Secondary titles and descriptive text on light backgrounds |
| `#645841` | Secondary Body | Supporting information and labels on light backgrounds |

### Dark Background — Text Colors

| Hex | Role | Usage |
|-----|------|-------|
| `#f4f2ee` | Heading / Body / Filled Input | Primary text on dark backgrounds; filled input field content |
| `#bfbdb0` | Heading / Body / Empty Input | Secondary text on dark backgrounds; input field placeholder |
| `#fee7c2` | Heading / Special Description | Special callouts and highlighted descriptions on dark backgrounds |
| `#a2a098` | Secondary Body | Supporting information on dark backgrounds |

### Quality Colors — Light Background

| Hex | Quality Tier | Semantic Extensions |
|-----|--------------|---------------------|
| `#204b93` | Blue (Common) | Alliance, Friendly Troops |
| `#804791` | Purple (Uncommon) | Purple Quality |
| `#ac591a` | Gold (Rare) | Highlights, Factions, Tactics, @-mentioned Players |
| `#a82f23` | Red (Epic / Legendary) | Negative, Enemy Troops, Place Names |
| `#2a6d3f` | Green (Positive) | Positive Attributes, Own Player, Landmarks |

### Quality Colors — Dark Background

| Hex | Quality Tier | Semantic Extensions |
|-----|--------------|---------------------|
| `#538dd9` | Blue (Common) | Alliance, Friendly Troops |
| `#be6bc5` | Purple (Uncommon) | Purple Quality |
| `#dd8441` | Gold (Rare) | Highlights, Factions, Tactics, @-mentioned Players |
| `#c33c3c` | Red (Epic / Legendary) | Negative, Enemy Troops, Place Names |
| `#409b6d` | Green (Positive) | Positive Attributes, Own Player, Landmarks |

### Alliance Colors

| Alliance | Color Identity |
|----------|----------------|
| Blue Alliance | Blue family |
| Pink Alliance | Pink family |
| Red Alliance | Red family |
| Yellow Alliance | Yellow family |
| Orange Alliance | Orange family |
| Green Alliance | Green family |
| Purple Alliance | Purple family |
| Neutral / Unoccupied | Gray family |

### Semantic Color Cross-Reference (Context-Agnostic Rules)

| Semantic Role | Light Background | Dark Background |
|---------------|------------------|-----------------|
| Own Player / Positive / Landmark | `#2a6d3f` | `#409b6d` |
| Enemy / Negative / Place Name | `#a82f23` | `#c33c3c` |
| Highlight / Faction / Tactic / Gold Quality | `#ac591a` | `#dd8441` |
| Alliance / Friendly Troops / Blue Quality | `#204b93` | `#538dd9` |
| Purple Quality | `#804791` | `#be6bc5` |

---

## 3. Typography Rules

### Font Family

- **Heading Font**: Founder LiBian Bold (方正隶变粗体)
- **Body Font**: Founder LiBian Regular (方正隶变)
- Both belong to the same typeface family; hierarchy is expressed through weight, not by mixing different typefaces

### Size Hierarchy

| Role | Size | Weight | Usage |
|------|------|--------|-------|
| Heading | 48px | Bold | Page-level titles, major milestone headings |
| Primary Button | 42px | Regular | Main action button labels |
| Primary Tab / Sub-heading | 38px | Regular | Navigation tabs, section sub-headings |
| Standard Body | 34px | Regular | General body copy across the UI |

**Modal Title Rules:**

| Modal Size | Font Size | Weight | Alignment | Overflow Behavior |
|------------|-----------|--------|-----------|-------------------|
| Large Modal Title | 46px | Bold | Left-aligned | Extends rightward |
| Medium Modal Title | 46px | Bold | Left-aligned | Extends rightward |
| Medium-Small Modal Title | 46px | Bold | Left-aligned | Extends rightward |
| Small Modal Title | 48px | Bold | Centered | Extends outward on both sides |

### Principles

- **Weight equals hierarchy**: Bold is reserved exclusively for headings and emphasis; Regular is for information display — never mix them arbitrarily
- **Restrained size scale**: Only four sizes are used — 34 / 38 / 42 / 48px — to avoid a fragmented scale
- **Input field text colors**: On dark backgrounds, use `#f4f2ee` for filled content and `#bfbdb0` for placeholders; body text must never have a drop shadow applied

---

## 4. Component Stylings

### Quality Badge

- **Sizes**: Small badge `154×154`, Wide banner `600×286`
- **Color**: Background filled with the corresponding quality color tier (Blue / Purple / Gold / Red)
- **Countdown overlay**: Placed at the top-left of wide banners, format: `Limited Time 15:12:00`
- **Quantity overlay**: e.g. `Currently Owned: 11`, overlaid within the badge

### Buttons

**Primary Button**
- Font size: 42px Founder LiBian Regular
- Purpose: Main actions (Confirm, Purchase, Deploy, etc.)
- Position: Bottom-right of modal (follows natural reading direction; confirm/positive actions are always on the right)

**Functional Button**
- Used for secondary actions (Ignore, Join, Cancel, etc.)
- Cancel / negative actions are always on the left
- Destructive actions (deletion, consuming rare resources) use red or a high-contrast accent color for emphasis

**Button Layout Rules:**
- Confirm / Positive / Recommended action → Right side
- Cancel / Negative / Secondary action → Left side
- A divider line separates the button area from the content area
- The button area is always centered, anchored to the bottom edge of the window
- Cost / resource consumption information is displayed above the button, not embedded in the button label

### Input Field

- **Single-line height**: 58px
- **Short text field width (small modals)**: 438px
- **Text color**: Follows dark background text color rules (`#f4f2ee` for filled, `#bfbdb0` for placeholder)
- No drop shadow on body text inside input fields
- Inner text-to-border padding: to be standardized

---

## 5. Modal System

### Modal Size Tiers

| Type | Typical Dimensions | Characteristics |
|------|-------------------|-----------------|
| Large Modal | Large | Supports background texture, full Tab system |
| Medium Modal | Medium | Supports background texture, Tab combinations |
| Medium-Small Modal | Medium-Small | Supports background texture |
| Small Modal (Standard) | ~934×588 | No texture, dual buttons, forms/input use cases |
| Small Modal (Confirmation) | ~934×588 | No texture, plain text only, 2–3 lines max |

### Background Texture Rules

- Only Large, Medium, and Medium-Small modals have a decorative background texture
- Texture position: **anchored to the bottom-right corner, flush with bottom and right edges**
- Small modals do not use background textures

### Tab System

**Primary Modal Tab Rules:**
- Level 1 Tab: Fixed to the left side, supports vertical scrolling
- Level 2 Tab: Non-scrolling by default; if too many items exist, prioritize converting to Level 1 Tab, dropdown, or tap-to-toggle formats
- Local Tab (Region Tab): May be used independently
- Restriction: **Level 2 Tab and Local (Region) Tab must never coexist in the same modal**
- Level 1 Tab + Local Tab combination requires a space sufficiency evaluation
- When no tabs are needed, the content area may expand to fill the available space

**Secondary Modal (Small Size):**
- Tabs are generally not used

### Small Modal Layout Structure

```
┌─────────────────────────────┐
│  [Title Area] Centered text │
├─────────────────────────────┤
│                             │
│  [Content Area] Text /      │
│  Input fields / Controls    │
│  Centered within the panel  │
│                             │
├─────────────────────────────┤
│    [Cancel]      [Confirm]  │
└─────────────────────────────┘
```

### Component Spacing

| Spacing Type | Value | Context |
|--------------|-------|---------|
| Same-type interactive components | 28px | Components requiring touch input (e.g. currency exchange, condition editing) |
| Different-type components | 45px | Separation between components of different types |
| Same-type informational components | Context-dependent | Pure text/prompt components |

---

## 6. Spacing & Layout Principles

- **Content area centered**: Modal content is horizontally centered within the panel — never flush to edges
- **Button area anchored to bottom**: The area below the divider line is always the button area, centered and anchored to the window's bottom edge
- **Cost information above buttons**: For any action involving resource consumption, display the cost above the button, not inside it
- **Title alignment by modal size**: Small modals use centered titles; Large and Medium modals use left-aligned titles

---

## 7. Do's and Don'ts

### Do
- Confirm / positive actions are **always on the right**; cancel / negative actions are **always on the left**
- Use **red or a high-contrast accent color** for destructive buttons (deletion, consuming rare resources)
- Modal title text should be **concise and descriptive**; overflow extends in the direction specified per modal size
- Background textures on large / medium / medium-small modals are **always anchored to the bottom-right corner**
- Quality colors must **switch to the corresponding palette** when the background changes — semantics stay the same, color values swap
- Alliance colors are used for faction identification and must be kept visually distinct from the quality color system
- Input field placeholders must use the **dedicated unfilled color** (`#bfbdb0` on dark / `#645841` on light)

### Don't
- Never use **Level 2 Tab and Local (Region) Tab simultaneously** in the same modal
- Never use **tabs in small modals**
- Never add **background textures to small modals**
- Never place the confirm button on the **left side** — this violates the established eye-tracking convention
- Never apply **drop shadows to body text** — this applies to text inside input fields as well
- Never use dark background quality color values directly in a light background context — the two palettes are not interchangeable
- When Level 2 Tab count is excessive, **do not force a scrolling solution** — redesign the interaction pattern first

---

## 8. Agent Prompt Guide

### Quick Color Reference

**Light Background Context:**
- Primary heading / body: `#321d14`
- Secondary heading / body 2: `#593323`
- Supporting text: `#645841`
- Positive / own player / landmark: `#2a6d3f`
- Negative / enemy / place name: `#a82f23`
- Highlight / Gold quality: `#ac591a`
- Purple quality: `#804791`
- Blue quality / alliance / friendly troops: `#204b93`

**Dark Background Context:**
- Primary text (filled): `#f4f2ee`
- Secondary text (unfilled): `#bfbdb0`
- Special callout: `#fee7c2`
- Supporting text: `#a2a098`
- Positive / own player / landmark: `#409b6d`
- Negative / enemy / place name: `#c33c3c`
- Highlight / Gold quality: `#dd8441`
- Purple quality: `#be6bc5`
- Blue quality / alliance / friendly troops: `#538dd9`

### Example Component Prompts

- **Standard small modal**: "Create a 934×588 small modal. Title area: centered at the top, Founder LiBian Bold 48px. Content area: centered layout with an input field (height 58px, width 438px). Button area: below a divider at the bottom, 'Cancel' on the left and 'Confirm' on the right, both centered. Dark background; body text `#f4f2ee`, placeholder `#bfbdb0`."
- **Quality badge**: "Create a quality badge at 154×154. Light background palette: Blue quality background `#204b93`, Purple `#804791`, Gold `#ac591a`, Red `#a82f23`. Badge label text in Founder LiBian Regular 34px, color `#f4f2ee`."
- **Primary modal with tabs**: "Large modal with a fixed Level 1 Tab column on the left, supporting vertical scroll. Tab labels in Founder LiBian 38px. Content area on the right. Bottom dual buttons (Cancel left / Confirm right). Decorative background texture anchored to the bottom-right corner."
- **Destructive action button**: "A confirm button for consuming rare resources. Use red accent (reference quality red `#a82f23` on light background or `#c33c3c` on dark background) to visually distinguish it from a standard confirm button. Position on the right side."

### Iteration Checklist

1. All modals: **Confirm always right, Cancel always left** — this rule does not change by modal size
2. Quality colors switch palette with background — **semantics are constant, color values swap**
3. Typography is always **Founder LiBian family only** — Bold for headings, Regular for body; no other typefaces introduced
4. Small modals have **no background texture and no tabs** — only Large / Medium / Medium-Small modals support these
5. **No drop shadow on body text** in input fields — even on dark backgrounds
6. Cost / resource prompts are **always above the button**, never embedded in the button label
7. Same-type component spacing is 28px (interactive); different-type component spacing is 45px — maintain consistent rhythm
