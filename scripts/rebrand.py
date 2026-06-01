#!/usr/bin/env python3
"""Rebrand all 8 mockups to Punk Solar Solutions and refocus copy on the
actual Asheville solar business (install / storage / off-grid / microgrids)."""
import sys

EDITS = {
    "01_verdant-systems_rewild-terminal.html": [
        ("<title>VERDANT SYSTEMS — Rewild Terminal</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Terminal)</title>"),
        ("⬡ VERDANT SYSTEMS", "⬡ PUNK SOLAR SOLUTIONS"),
        ("Blue Ridge Solar Collective", "Punk Solar Solutions · Asheville"),
        ("© 2026 VERDANT SYSTEMS LLC", "© 2026 PUNK SOLAR SOLUTIONS LLC"),
    ],
    "02_solstice-energy_golden-hour.html": [
        ("<title>Solstice Energy Co. — Golden Hour</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Golden Hour)</title>"),
        ('<span class="logo-text">Solstice Energy Co.</span>',
         '<span class="logo-text">Punk Solar Solutions</span>'),
        ("<span>Solstice Energy Co. · Asheville, NC 28801</span>",
         "<span>Punk Solar Solutions · Asheville, NC 28801</span>"),
        ("hello@solsticeenergy.co", "hello@punksolarsolutions.com"),
    ],
    "03_offgrid-avl_punk-zine.html": [
        ("<title>OffGrid AVL — Punk Zine</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Zine)</title>"),
        ('<div class="logo">OFF<span>GRID</span>AVL</div>',
         '<div class="logo">PUNK<span>SOLAR</span></div>'),
        ('<div class="footer-logo">OffGrid AVL · Asheville, NC</div>',
         '<div class="footer-logo">Punk Solar Solutions · Asheville, NC</div>'),
        ("power@offgridavl.com", "hello@punksolarsolutions.com"),
    ],
    "04_rhizogrid_biopunk-lab.html": [
        ("<title>RhizoGrid — Biopunk Lab</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Bio Lab)</title>"),
        ('<div class="logo-name">RHIZO<span>GRID</span></div>',
         '<div class="logo-name">PUNK<span>SOLAR</span></div>'),
        ('<div class="footer-logo">RHIZO<span>GRID</span> · Asheville NC</div>',
         '<div class="footer-logo">PUNK<span>SOLAR</span> SOLUTIONS · Asheville NC</div>'),
        ("grid@rhizogrid.io", "hello@punksolarsolutions.com"),
    ],
    "05_heliotrope_the-uprising.html": [
        ("<title>HELIOTROPE — Asheville Solarpunk Systems</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Uprising)</title>"),
        ('<div class="logo">HELIOTROPE</div>', '<div class="logo">PUNK SOLAR</div>'),
        ("Solarpunk infrastructure for a world that refuses to die. Asheville-based. Globally deployed.",
         "Solar, battery storage, and off-grid systems for the people of Asheville and Western North Carolina. Locally owned. Unapologetically independent."),
        ("No borders. No bosses. Only biology.",
         "No monopolies. No middlemen. Just sunlight."),
        ("Every system we deploy is a middle finger to the extractive economy. We design living architecture, regenerative grids, and autonomous ecosystems that serve communities, not shareholders.",
         "Every panel we install is a middle finger to the energy monopoly. We design solar arrays, battery backups, and community microgrids that serve neighbors — not shareholders."),
        ("01 / LIVING ARCHITECTURE", "01 / SOLAR INSTALLATION"),
        ("<h3>Bio-Integrated Structures</h3>", "<h3>Rooftop &amp; Ground Arrays</h3>"),
        ("Buildings that breathe, filter, and produce. Mycelium framing, algae facades, and self-healing concrete.",
         "Terrain-tuned panels engineered for mountain shade, ridge wind, and Appalachian weather. Residential and commercial."),
        ("02 / ENERGY AUTONOMY", "02 / BATTERY BACKUP"),
        ("<h3>Micro-Grid Systems</h3>", "<h3>Whole-Home Storage</h3>"),
        ("Community-owned solar, wind, and kinetic harvesting. No utility company required.",
         "LiFePO4 battery systems with 3–10 day capacity. Outlast any storm or Duke Energy outage with full power."),
        ("03 / FOOD FORESTS", "03 / COMMUNITY POWER"),
        ("<h3>Agroecological Design</h3>", "<h3>Microgrid Co-ops</h3>"),
        ("Permaculture at scale. Edible landscapes that regenerate soil and feed neighborhoods.",
         "Neighbor-owned shared energy networks. Pool resources, share storage, and quit the utility together."),
        ("Heliotrope Systems © 2026 — Asheville, NC / Everywhere",
         "Punk Solar Solutions © 2026 — Asheville, NC"),
    ],
    "06_spora_the-biosphere.html": [
        ("<title>SPORA — Regenerative Systems Lab</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Biosphere)</title>"),
        ('<div class="logo">Spora</div>', '<div class="logo">Punk Solar</div>'),
        ("<h1>Designing <em>living</em><br>infrastructure</h1>",
         "<h1>Powering <em>off-grid</em><br>Appalachia</h1>"),
        ("We merge ecological science with spatial design to create systems that regenerate rather than extract. From Asheville to the Amazon, every project is a hypothesis tested against reality.",
         "We design and install solar, storage, and microgrid systems for homes and communities across Asheville and Western North Carolina. Rigorous engineering, radically local."),
        ("<h3>Atmospheric Carbon Capture</h3>", "<h3>Solar Installation</h3>"),
        ('<div class="metric">12,847 t</div>', '<div class="metric">1,240+</div>'),
        ("Bioreactor arrays in urban corridors converting CO₂ to algal biomass. Operating in 14 cities across 3 continents.",
         "Rooftop and ground-mount PV arrays designed for mountain terrain — shade-mapped, ridge-tuned, built to last decades."),
        ("<h3>Regenerative Water Cycles</h3>", "<h3>Battery Storage</h3>"),
        ('<div class="metric">98.2%</div>', '<div class="metric">5–10 day</div>'),
        ("Closed-loop hydrological systems for off-grid communities. Rain harvesting, bio-filtration, and gravity distribution.",
         "Whole-home LiFePO4 backup. Keep the lights, the well pump, and the fridge running through any outage."),
        ("<h3>Mycelium Structural Networks</h3>", "<h3>Off-Grid Systems</h3>"),
        ('<div class="metric">4,200 m²</div>', '<div class="metric">94%</div>'),
        ("Grown-not-built architecture using fungal substrates. Fire-resistant, carbon-negative, and fully biodegradable.",
         "Complete energy independence for cabins, farms, and homesteads beyond the reach of the grid."),
        ("<h3>Community Energy Grids</h3>", "<h3>Community Microgrids</h3>"),
        ("Regenerative Systems Lab<br>Asheville, North Carolina<br>Remote operations worldwide",
         "Solar · Storage · Microgrids<br>Asheville, North Carolina<br>Serving all of Western NC"),
    ],
    "07_verdant-atelier_the-atelier.html": [
        ("<title>VERDANT — Solarpunk Atelier</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Editorial)</title>"),
        ('<div class="logo">Verdant Atelier</div>',
         '<div class="logo">Punk Solar Solutions</div>'),
        ('<span class="label">Solarpunk Systems — Vol. 04</span>',
         '<span class="label">Solar · Asheville, NC</span>'),
        ("An Asheville-based design practice engineering regenerative infrastructure for communities that refuse to accept the default future.",
         "An Asheville solar company designing and installing solar, storage, and off-grid systems for people who refuse to accept the utility's default future."),
        ("Solar arrays that double as public art. Water towers that function as observation decks. Power grids that strengthen communities instead of exploiting them.",
         "Solar arrays that double as public art. Battery walls you're proud to show off. Microgrids that strengthen neighborhoods instead of utilities that exploit them."),
        ("Our studio operates from the Blue Ridge Mountains, but our work knows no coordinates. We deploy remotely, consult globally, and build locally. The solarpunk aesthetic is not a veneer we apply to greenwashed products—it is the logical outcome of systems that respect the intelligence of living things.",
         "We work out of the Blue Ridge Mountains and install across Western North Carolina. The solarpunk look isn't a veneer on greenwashed products—it's what happens when energy systems respect both people and place."),
        ('data-caption="Solar Canopy — Nashville, TN"', 'data-caption="Rooftop Array — West Asheville"'),
        ('data-caption="Algae Bioreactor"', 'data-caption="Battery Backup — Black Mountain"'),
        ('data-caption="Mycelium Study"', 'data-caption="Ground Mount — Weaverville"'),
        ('data-caption="Rainwater Cathedral"', 'data-caption="Off-Grid Cabin — Madison County"'),
        ('data-caption="Community Grid"', 'data-caption="Community Microgrid — Asheville"'),
        ('data-caption="Asheville Studio"', 'data-caption="Punk Solar HQ — Asheville"'),
        ("— Verdant Design Principles, 2026", "— Punk Solar Solutions, 2026"),
        ("studio@verdant.systems", "hello@punksolarsolutions.com"),
        ("Remote operations worldwide<br>Studio visits by appointment",
         "Serving Asheville &amp; Western NC<br>Free site visits by appointment"),
    ],
    "08_antenna_the-signal.html": [
        ("<title>ANTENNA — Distributed Ecological Systems</title>",
         "<title>Punk Solar Solutions — Asheville, NC (Signal)</title>"),
        ('<div class="logo">Antenna</div>', '<div class="logo">Punk Solar</div>'),
        ("<h1>Transmitting <span>regenerative</span> infrastructure across all coordinates</h1>",
         "<h1>Solar power for every <span>ridge</span>, holler, and rooftop in Western NC</h1>"),
        ("We are a distributed collective of designers, engineers, and ecologists. Headquartered in Asheville. Deployed everywhere. Building the solarpunk reality one node at a time.",
         "Punk Solar Solutions designs and installs solar, battery, and off-grid systems. Headquartered in Asheville. Wired into every corner of Western North Carolina."),
        ("[ SIGNAL DISTRIBUTION ]", "[ COVERAGE MAP ]"),
        ("N. AMERICA", "ASHEVILLE&nbsp;"),
        ("S. AMERICA", "BLACK MTN&nbsp;"),
        ("EUROPE", "WEAVERVL"),
        ("ASIA", "HENDRSNVL"),
        ("AFRICA", "BREVARD"),
        ("OCEANIA", "MARSHALL"),
        ("Asheville — Nashville — Portland — Berlin — Mexico City — Tokyo — Lagos — São Paulo — Melbourne — Asheville — Nashville — Portland — Berlin — Mexico City — Tokyo — Lagos — São Paulo — Melbourne —",
         "Asheville — Black Mountain — Weaverville — Hendersonville — Brevard — Marshall — Mars Hill — Fairview — Asheville — Black Mountain — Weaverville — Hendersonville — Brevard — Marshall — Mars Hill — Fairview —"),
        ("<h3>Water Sovereignty</h3>", "<h3>Battery Backup</h3>"),
        ("Rain capture, bio-filtration, and closed-loop distribution. Every drop accounted for. Every system owned by its users.",
         "Whole-home LiFePO4 storage with 3–10 day capacity. Keep power through every storm and outage. Every system owned by its user."),
        ("<h3>Food Networks</h3>", "<h3>Off-Grid Systems</h3>"),
        ("Urban agroforestry and vertical growing systems. Community-operated, zero-mile supply chains. Biology as logistics.",
         "Complete energy independence for cabins, farms, and homesteads beyond the grid. Solar plus storage, engineered to stand alone."),
        ('<p style="opacity:0.6;font-size:0.9rem;">Distributed Ecological Systems</p>',
         '<p style="opacity:0.6;font-size:0.9rem;">Solar · Storage · Off-Grid · Microgrids</p>'),
        ("signal@antenna.systems", "hello@punksolarsolutions.com"),
        ("Open source by default.<br>All systems documented.<br>Nothing proprietary.",
         "No hidden fees.<br>No lock-in contracts.<br>Every quote itemized."),
    ],
}

warnings = 0
for fname, edits in EDITS.items():
    with open(fname, encoding="utf-8") as fh:
        content = fh.read()
    for old, new in edits:
        if old not in content:
            print(f"  !! NOT FOUND in {fname}: {old[:60]!r}")
            warnings += 1
            continue
        content = content.replace(old, new)
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"updated {fname} ({len(edits)} edits)")

print("WARNINGS:", warnings)
sys.exit(1 if warnings else 0)
