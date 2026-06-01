# Solarpunk Solar Co. — Asheville, NC · Client Design Review

A static client-review site presenting **8 website design directions** for a solarpunk
solar-energy company in Asheville, NC. Theme: *PUNK meets Captain Planet.*

**Live gallery:** open `index.html` — it links to all 8 live, animated designs and
embeds the microscopy motion reel.

## Structure

| Path | What |
|------|------|
| `index.html` | Client review gallery (the hub to share) |
| `0?_*.html` | The 8 design mockups |
| `assets/img/` | Original microscopy + Asheville imagery |
| `assets/video/biosphere_reel.mp4` | Generated Ken Burns motion reel |
| `assets/enhance.js` | Wires imagery/video into each mockup |

## The 8 designs

1. Verdant Systems — dark forest terminal
2. Solstice Energy Co. — warm amber luxe
3. OffGrid AVL — punk zine ★
4. RhizoGrid — biopunk lab
5. Heliotrope — neon-green uprising ★
6. Spora — organic biosphere
7. Verdant Atelier — editorial gallery
8. Antenna — CRT signal

## Run locally

```bash
python3 -m http.server 8744
# visit http://127.0.0.1:8744/
```

## Status / next steps

This is the **design-selection** phase. Once the client picks a direction, the build-out
adds: real copy, ADA / WCAG 2.1 AA accessibility, and full legal pages
(Privacy Policy, Terms, Cookie Policy + consent, Accessibility Statement) covering
CCPA/CPRA, GDPR, and CAN-SPAM.

> Legal pages will be drafted to a strong template standard and must be reviewed by
> counsel before launch.
