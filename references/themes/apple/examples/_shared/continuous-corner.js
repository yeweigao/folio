/* continuous-corner.js — Apple continuous corner, as a vector path.
 *
 * Native constants, symmetric about the corner's diagonal. Coordinates (u, v)
 * run inward from a corner, in units of R:
 *
 *   M 0 1.52866
 *   C 0 1.08849  0 .86841  .07491 .63149
 *   C .16906 .37282  .37282 .16906  .63149 .07491
 *   C .86841 0  1.08849 0  1.52866 0
 *
 * A side shorter than 2 x 1.52866R cannot hold two shoulders: its shoulder
 * shortens to half the side, easing toward the native saturated form
 * (half the side = R: from 0 1 through 0 .96 and 0 .82). Fill, stroke and
 * clip share one path. border-radius, rect rx and superellipses are other curves.
 *
 * Use: <div data-cc="18" data-cc-fill="#ffffff" data-cc-stroke="#e0e0e0"
 *           data-cc-stroke-width="1"> live text </div>
 *      <div data-cc="18" data-cc-clip> <img ...> </div>
 * Loaded from ../../_shared/continuous-corner.js relative to a piece folder.
 */
(function () {
  'use strict';
  var EXT = 1.52866;
  var MID = [[0.07491, 0.63149], [0.16906, 0.37282], [0.37282, 0.16906], [0.63149, 0.07491]];

  function n(v) { return Math.round(v * 1000) / 1000; }

  // The straight-edge end of a shoulder whose extent is e (in R, 1..EXT):
  // [end, control near end, control near middle].
  function end(e) {
    var s = (e - 1) / (EXT - 1);
    return [e, 0.96 + s * (1.08849 - 0.96), 0.82 + s * (0.86841 - 0.82)];
  }

  // One corner from the vertical edge (extent ev) to the horizontal edge (eh),
  // as cubic triples in (u, v); reversed when the path runs the other way.
  function corner(cx, cy, dx, dy, r, ev, eh, forward) {
    var a = end(ev), b = end(eh);
    var P = [[0, a[0]], [0, a[1]], [0, a[2]], MID[0], MID[1], MID[2], MID[3],
             [b[2], 0], [b[1], 0], [b[0], 0]];
    if (!forward) P.reverse();
    var f = function (p) { return n(cx + dx * r * p[0]) + ' ' + n(cy + dy * r * p[1]); };
    var out = [];
    for (var i = 1; i < 10; i += 3) out.push('C ' + f(P[i]) + ' ' + f(P[i + 1]) + ' ' + f(P[i + 2]));
    return out.join(' ');
  }

  function ccPath(w, h, radius) {
    var r = Math.min(radius, w / 2, h / 2);
    if (r <= 0) return 'M 0 0 H ' + n(w) + ' V ' + n(h) + ' H 0 Z';
    var eh = Math.min(EXT, w / 2 / r), ev = Math.min(EXT, h / 2 / r);
    var x = eh * r, y = ev * r;
    // A straight run is drawn only where one remains between two shoulders.
    var L = function (len, px, py) { return len > 0.001 ? 'L ' + n(px) + ' ' + n(py) + ' ' : ''; };
    return 'M ' + n(x) + ' 0 ' +
      L(w - 2 * x, w - x, 0) +
      corner(w, 0, -1, 1, r, ev, eh, false) + ' ' +
      L(h - 2 * y, w, h - y) +
      corner(w, h, -1, -1, r, ev, eh, true) + ' ' +
      L(w - 2 * x, x, h) +
      corner(0, h, 1, -1, r, ev, eh, false) + ' ' +
      L(h - 2 * y, 0, y) +
      corner(0, 0, 1, 1, r, ev, eh, true) + ' Z';
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
