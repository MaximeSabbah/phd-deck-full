(function(){
  function init(){
    const deck = document.querySelector('.reveal');
    if (!deck || !window.Reveal) return;

    // Create (or reuse) the indicator bar
    let bar = deck.querySelector('.part-indicator');
    if (!bar){
      bar = document.createElement('div');
      bar.className = 'part-indicator';
      deck.appendChild(bar);
    }

    // Keep full-width layout (centered partitions)
    const FULL_WIDTH = true;

    // Fallbacks so colors/titles are always correct
    const PART_LABELS = {
      'introduction': 'Introduction',
      'part-I': 'Part I',
      'part-II': 'Part II',
      'part-III': 'Part III',
      'conclusion': 'Conclusion'
    };
    const PART_ACCENTS = {
      'introduction': 'var(--c-secondary-dark-blue)',
      'part-I': 'var(--c-laas-red)',
      'part-II': 'var(--c-secondary-blue)',
      'part-III': 'var(--c-secondary-green)',
      'conclusion': 'var(--c-secondary-dark-blue)'
      // tweak any of these to your exact palette
    };


    // Current slide's top-level part wrapper (<section data-part-group>)
    function topPartOf(slide){
      const top = slide?.closest('.slides > section');
      return (top && top.hasAttribute('data-part-group')) ? top : null;
    }

    // Return ALL bullet slides inside a part, robust to two authoring styles:
    //  (A) one wrapper per part with vertical slides inside
    //  (B) multiple top-level slides each tagged with the same data-part-group
    function slidesInPart(group){
      const wrappers = Array.from(document.querySelectorAll(`.slides > section[data-part-group="${group}"]`));
      const result   = [];
      for (const w of wrappers) {
        const directSlides = Array.from(w.children).filter(n => n.tagName === 'SECTION');
        if (directSlides.length) result.push(...directSlides); // style A
        else result.push(w);                                   // style B
      }
      return result;
    }

    // Build ordered metadata for all parts
    function partsMeta(){
      const wrappers = Array.from(document.querySelectorAll('.slides > section[data-part-group]'));
      const order = [];
      const map   = new Map();
      for (const el of wrappers) {
        const group = el.getAttribute('data-part-group');
        if (!map.has(group)) {
          // Prefer our canonical label/accent to avoid placeholders & wrong colors
          const title  = PART_LABELS[group] || (el.getAttribute('data-part-title') || group);
          const accent = PART_ACCENTS[group] || getComputedStyle(el).getPropertyValue('--part-accent').trim() || 'currentColor';
          const slides = slidesInPart(group);
          const meta = { group, title, accent, slides };
          map.set(group, meta);
          order.push(group);
        }
      }
      return order.map(g => map.get(g)).filter(p => p.slides.length);
    }

    function update(){
      const curSlide = Reveal.getCurrentSlide();
      const top      = topPartOf(curSlide);

      // Hide off-part slides (e.g., cover page)
      if (!top) { bar.style.display='none'; bar.classList.remove('pi--full'); bar.innerHTML=''; return; }

      bar.classList.toggle('pi--full', FULL_WIDTH);
      bar.style.display = FULL_WIDTH ? 'grid' : 'flex';

      const parts   = partsMeta();
      const curGp   = top.getAttribute('data-part-group');
      const gpIdx   = parts.findIndex(p => p.group === curGp);

      // index inside the current part (works for both authoring styles)
      const slidesCur = parts[gpIdx].slides;
      const idxInPart = slidesCur.includes(curSlide) ? slidesCur.indexOf(curSlide)
                                                     : slidesCur.indexOf(top);

      // Render partitions
      const html = parts.map((p, gi) => {
        const filledUpTo = (gi < gpIdx) ? p.slides.length
                          : (gi === gpIdx ? idxInPart + 1 : 0);
        const dots = p.slides.map((_, i) =>
          `<span class="pi-dot${i < filledUpTo ? ' is-filled' : ''}${(gi===gpIdx && i===idxInPart)?' is-current':''}"></span>`
        ).join('');
        return `<span class="pi-part" style="--group-accent:${p.accent}">
                  <span class="pi-title">${p.title}</span>
                  <span class="pi-dots">${dots}</span>
                </span>`;
      }).join('');

      bar.innerHTML = html;

      // Auto-compact if overflowing but keep centered
      bar.classList.remove('is-compact');
      if (bar.scrollWidth > bar.clientWidth) bar.classList.add('is-compact');
    }

    Reveal.on('ready', update);
    Reveal.on('slidechanged', update);
    Reveal.on('fragmentshown', update);
    Reveal.on('fragmenthidden', update);
    Reveal.on('resize', update);
  }

  if (document.readyState === 'complete' || document.readyState === 'interactive') init();
  else window.addEventListener('DOMContentLoaded', init);
})();