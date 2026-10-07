/* Ganesha's Big Race - shared graphics kit (plain script, no modules).
   Everything is deterministic and seekable: seeded PRNG only, finite GSAP tweens on the composition's own paused timeline.
   Usage inside a composition: const tl = gsap.timeline({paused:true}); Kit.pop(tl, '#num1', 4.47); ... window.__timelines['id'] = tl; */
(function () {
  const Kit = {};

  /* ---------- seeded random (mulberry32) ---------- */
  Kit.rng = function (seed) {
    let a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };

  /* ---------- inline SVG shapes (return markup strings) ---------- */
  Kit.svg = {
    petal(color, w, h) {
      return `<svg viewBox="0 0 40 64" width="${w || 40}" height="${h || 64}"><path d="M20 2 C35 14 39 40 20 62 C1 40 5 14 20 2Z" fill="${color}"/><path d="M20 8 C26 20 27 38 20 54" stroke="rgba(255,255,255,.35)" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>`;
    },
    sparkle(color, size) {
      const s = size || 40;
      return `<svg viewBox="-20 -20 40 40" width="${s}" height="${s}"><path d="M0 -19 C2 -6 6 -2 19 0 C6 2 2 6 0 19 C-2 6 -6 2 -19 0 C-6 -2 -2 -6 0 -19Z" fill="${color || '#FFD866'}"/></svg>`;
    },
    marigold(size, c1, c2) {
      const a = c1 || '#F6B21A', b = c2 || '#F28C28';
      let p = '';
      for (let ring = 0; ring < 3; ring++) {
        const n = 12 - ring * 2, r = 38 - ring * 9, rx = 13 - ring * 2.5, ry = 20 - ring * 3.5;
        for (let i = 0; i < n; i++) {
          const ang = (360 / n) * i + ring * 11;
          p += `<ellipse cx="50" cy="${50 - r}" rx="${rx}" ry="${ry}" fill="${ring % 2 ? a : b}" stroke="rgba(120,40,0,.25)" stroke-width="1" transform="rotate(${ang} 50 50)"/>`;
        }
      }
      p += `<circle cx="50" cy="50" r="9" fill="#C86A10"/>`;
      return `<svg viewBox="0 0 100 100" width="${size || 90}" height="${size || 90}">${p}</svg>`;
    },
    modak(size) {
      const s = size || 90;
      return `<svg viewBox="0 0 100 110" width="${s}" height="${s * 1.1}"><defs><radialGradient id="mk" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#F2B35A"/><stop offset="1" stop-color="#B8651B"/></radialGradient></defs><path d="M50 4 C58 18 62 24 76 34 C94 48 92 78 70 94 C58 102 42 102 30 94 C8 78 6 48 24 34 C38 24 42 18 50 4Z" fill="url(#mk)" stroke="#8A4510" stroke-width="3"/><path d="M26 62 C40 72 60 72 74 62 M30 78 C42 86 58 86 70 78 M36 44 C44 52 56 52 64 44" stroke="rgba(255,235,190,.55)" stroke-width="3" fill="none" stroke-linecap="round"/></svg>`;
    },
  };

  /* ---------- tween helpers (all on the caller's paused timeline) ---------- */
  // Soft pop-in: scales from 0.2 with an overshoot while fading in. Never faster than 0.25 s.
  Kit.pop = function (tl, target, at, o) {
    o = o || {};
    tl.fromTo(target,
      { scale: o.from == null ? 0.2 : o.from, opacity: 0, transformOrigin: o.origin || '50% 50%' },
      { scale: 1, opacity: 1, duration: o.dur || 0.55, ease: o.ease || 'back.out(2.2)' }, at);
    return tl;
  };
  Kit.fadeIn = function (tl, target, at, dur, o) {
    o = o || {};
    tl.fromTo(target, { opacity: 0, y: o.y == null ? 18 : o.y }, { opacity: 1, y: 0, duration: dur || 0.5, ease: o.ease || 'power2.out' }, at);
    return tl;
  };
  Kit.fadeOut = function (tl, target, at, dur) {
    tl.to(target, { opacity: 0, duration: Math.max(0.25, dur || 0.5), ease: 'power1.inOut' }, at);
    return tl;
  };
  // Gentle bob (finite): amplitude in px, period in seconds, from time `at` for `len` seconds.
  Kit.bob = function (tl, target, at, len, amp, period) {
    const per = period || 2.4;
    const reps = Math.max(1, Math.floor(len / (per / 2)) - 1);
    tl.to(target, { y: '-=' + (amp || 8), duration: per / 2, ease: 'sine.inOut', yoyo: true, repeat: reps }, at);
    return tl;
  };

  // Falling petals / marigold flowers: container must be position:absolute with a known size (w,h).
  // opts: {n, seed, t0, t1, w, h, colors:[..], minDur, maxDur, minSize, maxSize, flowers:0..1}
  Kit.petalFall = function (tl, container, o) {
    const rnd = Kit.rng(o.seed || 7);
    const colors = o.colors || ['#F6B21A', '#F28C28', '#F4A6B8', '#FFD866'];
    const el = typeof container === 'string' ? document.querySelector(container) : container;
    for (let i = 0; i < o.n; i++) {
      const outer = document.createElement('div');
      outer.style.cssText = 'position:absolute;left:0;top:0;opacity:0;will-change:transform';
      const inner = document.createElement('div');
      const size = (o.minSize || 26) + rnd() * ((o.maxSize || 54) - (o.minSize || 26));
      const isFlower = rnd() < (o.flowers || 0);
      inner.innerHTML = isFlower ? Kit.svg.marigold(size * 1.1) : Kit.svg.petal(colors[Math.floor(rnd() * colors.length)], size * 0.62, size);
      outer.appendChild(inner); el.appendChild(outer);
      const x0 = rnd() * o.w, dx = (rnd() - 0.5) * 260, d = (o.minDur || 5.5) + rnd() * ((o.maxDur || 9) - (o.minDur || 5.5));
      const start = o.t0 + rnd() * Math.max(0.01, (o.t1 - o.t0));
      const spin = (rnd() - 0.5) * 540, r0 = rnd() * 360;
      tl.fromTo(outer, { x: x0, y: -90, rotation: r0 }, { x: x0 + dx, y: o.h + 90, rotation: r0 + spin, duration: d, ease: 'none' }, start);
      tl.to(outer, { opacity: 0.95, duration: 0.5, ease: 'none' }, start);
      tl.to(outer, { opacity: 0, duration: 0.6, ease: 'none' }, start + d - 0.6);
      const sw = 14 + rnd() * 26, per = 1.6 + rnd() * 1.4;
      const reps = Math.max(1, Math.floor(d / (per / 2)) - 1);
      tl.fromTo(inner, { x: -sw, rotationY: -35 }, { x: sw, rotationY: 35, duration: per / 2, ease: 'sine.inOut', yoyo: true, repeat: reps }, start);
    }
    return tl;
  };

  // Soft sparkle burst (4-point stars flying out and fading). opts: {x,y,at,n,seed,r,color,size}
  Kit.sparkBurst = function (tl, container, o) {
    const rnd = Kit.rng(o.seed || 3);
    const el = typeof container === 'string' ? document.querySelector(container) : container;
    const n = o.n || 9;
    for (let i = 0; i < n; i++) {
      const s = document.createElement('div');
      const size = (o.size || 34) * (0.55 + rnd() * 0.7);
      s.style.cssText = `position:absolute;left:${o.x - size / 2}px;top:${o.y - size / 2}px;opacity:0;width:${size}px;height:${size}px`;
      s.innerHTML = Kit.svg.sparkle(o.color || '#FFD866', size);
      el.appendChild(s);
      const ang = (Math.PI * 2 * i) / n + rnd() * 0.5, dist = (o.r || 130) * (0.6 + rnd() * 0.6);
      tl.fromTo(s, { x: 0, y: 0, scale: 0.2, opacity: 0, rotation: 0 },
        { x: Math.cos(ang) * dist, y: Math.sin(ang) * dist, scale: 1, opacity: 1, rotation: 90, duration: 0.45, ease: 'power2.out' }, o.at);
      tl.to(s, { opacity: 0, scale: 0.3, duration: 0.55, ease: 'power1.in' }, o.at + 0.45);
    }
    return tl;
  };

  window.Kit = Kit;
})();
