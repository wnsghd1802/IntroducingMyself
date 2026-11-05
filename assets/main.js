(() => {
  const nav = document.querySelector('.nav');
  const toggle = document.querySelector('.nav-toggle');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const opened = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(opened));
      toggle.setAttribute('aria-label', opened ? '메뉴 닫기' : '메뉴 열기');
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }
  const storyBtn = document.querySelector('#story-toggle');
  const story = document.querySelector('#full-story');
  if (storyBtn && story) {
    storyBtn.addEventListener('click', () => {
      const open = !story.classList.contains('is-open');
      story.classList.toggle('is-open', open);
      storyBtn.setAttribute('aria-expanded', String(open));
      storyBtn.textContent = open ? '본문 접기 −' : '3분 자기소개 전문 읽기 ↗';
    });
  }
  const reveal = document.querySelectorAll('.animated-in, .bar-fill');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add(entry.target.classList.contains('bar-fill') ? 'ready' : 'visible');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12 });
    reveal.forEach(el => io.observe(el));
  } else reveal.forEach(el => el.classList.add(el.classList.contains('bar-fill') ? 'ready' : 'visible'));
  const progress = document.querySelector('.scroll-progress');
  const scrollTop = document.querySelector('.scroll-top');
  function updateScroll() {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = `${max > 0 ? Math.min(100, scrollY / max * 100) : 100}%`;
    if (scrollTop) scrollTop.classList.toggle('show', scrollY > 700);
  }
  window.addEventListener('scroll', updateScroll, { passive:true });
  window.addEventListener('resize', updateScroll);
  updateScroll();
  scrollTop?.addEventListener('click', () => window.scrollTo({top:0,behavior:'smooth'}));
})();