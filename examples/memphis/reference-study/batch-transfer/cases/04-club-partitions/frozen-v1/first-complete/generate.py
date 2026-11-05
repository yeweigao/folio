#!/usr/bin/env python3
"""Original native SVG composition for the supplied Night Assembly brief."""
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
PAPER = '#F9F9F6'
INK = '#000000'
BLUE = '#0969F9'
RED = '#FF3A06'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
  <title id="poster-title">Night Assembly — 17.07.27 — FORMA CLUB</title>
  <desc id="poster-description">Rosa Flux and Mika Lo, B2B until dawn. LOWER ROOM: Alba Phase, Dorian East, NEX. Starts at 23:00.</desc>
  <!-- FONTS -->
  <style>
    text {{ font-family:"Study Sans",sans-serif; fill:{INK}; }}
    .names {{ font-weight:700; letter-spacing:-1.4px; }}
    .rule {{ fill:none; stroke:{INK}; stroke-width:10; stroke-linecap:square; stroke-linejoin:miter; }}
  </style>
  <defs>
    <clipPath id="upper-field"><path d="M450 264H900V690H450Z"/></clipPath>
    <clipPath id="lower-field"><path d="M0 588H450V1034H0Z"/></clipPath>
  </defs>

  <!-- A stepped scaffold. The two artist rectangles remain completely clear. -->
  <rect width="900" height="1200" fill="{PAPER}"/>
  <path d="M0 0H732V264H0Z" fill="{INK}"/>
  <path d="M732 0H900V264H732Z" fill="{BLUE}"/>
  <path d="M450 264H732V690H450Z" fill="{RED}"/>
  <path d="M732 264H900V690H732Z" fill="{INK}"/>
  <path d="M0 588H450V1034H0Z" fill="{BLUE}"/>

  <!-- The secondary vertical partition is crossed by one continuous white contour. -->
  <path d="M732 0V690" class="rule"/>
  <g clip-path="url(#upper-field)">
    <path d="M420 250
      C566 235 669 281 738 341
      C798 393 854 410 920 352
      L920 528
      C854 585 772 570 706 523
      C633 470 608 427 550 428
      C501 428 466 468 420 510Z"
      fill="{PAPER}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>
  </g>

  <!-- A reversed lower contour turns the blue field into a large black/white mass. -->
  <g clip-path="url(#lower-field)">
    <path d="M-30 651
      C62 580 173 594 239 649
      C316 713 290 795 358 834
      C392 854 424 848 480 812
      L480 1064H-30Z" fill="{INK}"/>
    <path d="M-30 651
      C62 580 173 594 239 649
      C316 713 290 795 358 834
      C392 854 424 848 480 812
      L480 981
      C403 1041 318 1019 266 972
      C196 908 215 823 157 787
      C108 757 45 775 -30 832Z"
      fill="{PAPER}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>
  </g>

  <!-- Structural black frames are part of the composition. -->
  <path d="M0 264H900 M0 588H450 M450 690H900 M450 264V1034 M0 1034H900 M450 1034V1200" class="rule"/>
  <rect x="5" y="5" width="890" height="1190" class="rule"/>

  <!-- Live, editable display type. -->
  <text fill="{PAPER}" font-weight="700" letter-spacing="-4.5" aria-label="Night Assembly">
    <tspan x="28" y="106" font-size="100" fill="{PAPER}">Night </tspan>
    <tspan x="28" y="225" font-size="126" fill="{PAPER}">Assembly</tspan>
  </text>

  <!-- First artist group. -->
  <g id="main-artists">
    <text x="28" y="360" font-size="60" class="names">Rosa Flux</text>
    <text x="28" y="432" font-size="60" class="names">Mika Lo</text>
    <text x="30" y="535" font-size="24" font-weight="400">B2B until dawn</text>
  </g>

  <!-- Second artist group. -->
  <g id="lower-room-artists">
    <text x="478" y="742" font-size="23" font-weight="700" letter-spacing="0.2">LOWER ROOM</text>
    <text x="477" y="816" font-size="52" class="names">Alba Phase</text>
    <text x="477" y="888" font-size="52" class="names">Dorian East</text>
    <text x="477" y="960" font-size="52" class="names">NEX</text>
  </g>

  <!-- The hard bottom fact band. -->
  <g id="event-facts">
    <text x="28" y="1142" font-size="67" font-weight="700" letter-spacing="-2">17.07.27</text>
    <text x="478" y="1110" font-size="52" font-weight="700" letter-spacing="-1">23:00</text>
    <text x="479" y="1170" font-size="28" font-weight="700" letter-spacing="0.1">FORMA CLUB</text>
  </g>
</svg>
'''
(HERE / 'raw.svg').write_text(svg)
subprocess.run([
    '/private/tmp/folio-memphis-tools/bin/python',
    str(CASE / 'input/embed_fonts.py'), str(CASE / 'input/fonts'),
    str(HERE / 'raw.svg'), str(HERE / 'poster.svg'),
], check=True)
