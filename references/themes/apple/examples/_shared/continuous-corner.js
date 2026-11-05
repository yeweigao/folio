/* continuous-corner.js — Apple continuous corner, as a vector path.
 *
 * The control points below are not a mathematical squircle and not a circular
 * border-radius. They are normalised from an actual macOS SwiftUI
 *   RoundedRectangle(cornerRadius: 22, style: .continuous)
 * export kept in exports/apple-continuous-corner/native/paths.json, verified in
 * AUDIT.md. Coordinates (u, v) run inward from a corner, in units of R:
 *
 *   A = (0, 1)                     the point where the straight edge ends
 *   C (0, .96) (0, .82) (.07491, .63149)
 *   C (.16906, .37282) (.37282, .16906) (.63149, .07491)
 *   C (.86841, 0) (1.08849, 0) (1.52866, 0)
 *   B = (1.52866, 0)              the point where the next straight edge begins
 *
 * The 1.52866R shoulder extent is the measured native value. Fill, stroke and
 * image clip use this one path. Plain CSS border-radius, SVG rect rx and
 * superellipses are not substitutes.
 *
 * Use: <div class="card" data-cc="18" data-cc-fill="#ffffff"
 *           data-cc-stroke="#e0e0e0" data-cc-stroke-width="1"> live text </div>
 *      <div class="media" data-cc="18" data-cc-clip> <img ...> </div>
 *
 * Scripts are loaded from ../../_shared/continuous-corner.js relative to a
 * piece folder (examples/<world>/<slug>/). No build step, no network.
 */
(function () {
  'use strict';
  var EXT = 1.52866;
  var SEG = [
    [[0, 0.96], [0, 0.82], [0.07491, 0.63149]],
    [[0.16906, 0.37282], [0.37282, 0.16906], [0.63149, 0.07491]],
    [[0.86841, 0], [1.08849, 0], [EXT, 0]]
  ];
  var A = [0, 1], B = [EXT, 0];

  function n(v) { return Math.round(v * 1000) / 1000; }
  function pt(cx, cy, dx, dy, r, p) {
    return n(cx + dx * r * p[0]) + ' ' + n(cy + dy * r * p[1]);
  }

  // One 90-degree turn. forward: A -> B; reverse: B -> A.
  function corner(cx, cy, dx, dy, r, forward) {
    var f = function (p) { return pt(cx, cy, dx, dy, r, p); };
    var out = [], i, s, triples;
    if (forward) {
      for (i = 0; i < 3; i++) {
        s = SEG[i];
        out.push('C ' + f(s[0]) + ' ' + f(s[1]) + ' ' + f(s[2]));
      }
    } else {
      triples = [
        [A, SEG[0][0], SEG[0][1], SEG[0][2]],
        [SEG[0][2], SEG[1][0], SEG[1][1], SEG[1][2]],
        [SEG[1][2], SEG[2][0], SEG[2][1], B]
      ];
      for (i = 2; i >= 0; i--) {
        s = triples[i];
        out.push('C ' + f(s[2]) + ' ' + f(s[1]) + ' ' + f(s[0]));
      }
    }
    return out.join(' ');
  }

  // Fit the shoulder to the available dimensions, so adjacent shoulders never
  // overlap on narrow or saturated controls.
  function ccPath(w, h, radius) {
    var r = Math.min(radius, h / 2, w / (2 * EXT));
    if (r <= 0) return 'M 0 0 H ' + n(w) + ' V ' + n(h) + ' H 0 Z';
    var e = EXT * r;
    return 'M ' + n(e) + ' 0 ' +
      'L ' + n(w - e) + ' 0 ' +
      corner(w, 0, -1, 1, r, false) +
      'L ' + n(w) + ' ' + n(h - r) + ' ' +
      corner(w, h, -1, -1, r, true) +
      'L ' + n(e) + ' ' + n(h) + ' ' +
      corner(0, h, 1, -1, r, false) +
      'L 0 ' + n(r) + ' ' +
      corner(0, 0, 1, 1, r, true) + ' Z';
  }

  function draw(el) {
    var w = el.offsetWidth, h = el.offsetHeight;
    if (!w || !h) return;
    var r = parseFloat(el.getAttribute('data-cc')) || 0;
    var d = ccPath(w, h, r);
    var fill = el.getAttribute('data-cc-fill') || 'transparent';
    var stroke = el.getAttribute('data-cc-stroke');
    var sw = parseFloat(el.getAttribute('data-cc-stroke-width')) || 1;
    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'cc-bg');
    svg.setAttribute('width', w);
    svg.setAttribute('height', h);
    svg.setAttribute('viewBox', '0 0 ' + w + ' ' + h);
    svg.setAttribute('aria-hidden', 'true');
    var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', d);
    path.setAttribute('fill', fill);
    if (stroke) {
      path.setAttribute('stroke', stroke);
      path.setAttribute('stroke-width', sw);
    }
    svg.appendChild(path);
    el.insertBefore(svg, el.firstChild);
    el.style.background = 'transparent';
    el.style.border = '0';
    el.style.borderRadius = '0';
    if (el.hasAttribute('data-cc-clip')) {
      el.style.clipPath = 'path("' + d + '")';
    }
  }

  function run() {
    var els = document.querySelectorAll('[data-cc]');
    for (var i = 0; i < els.length; i++) draw(els[i]);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
  window.ccPath = ccPath;
  window.ccRedraw = run;
}());
