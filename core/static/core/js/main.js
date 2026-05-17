const counters = document.querySelectorAll('.counter');
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = +el.dataset.target;
      let current = 0;
      const increment = target / 120;
      const update = () => {
        current += increment;
        if (current < target) {
          el.textContent = Math.floor(current);
          requestAnimationFrame(update);
        } else {
          el.textContent = target;
        }
      };
      update();
      observer.unobserve(el);
    }
  });
});
counters.forEach(c => observer.observe(c));
