// ========================================
// MOBILE HAMBURGER MENU
// ========================================
const menuToggle = document.getElementById('menuToggle');
const mainMenu = document.getElementById('mainMenu');

if (menuToggle && mainMenu) {
    menuToggle.addEventListener('click', () => {
        mainMenu.classList.toggle('active');

        // Ubah ikon ☰ menjadi ✕
        menuToggle.textContent =
            mainMenu.classList.contains('active') ? '✕' : '☰';
    });
}


// ========================================
// COUNTER ANIMATION
// ========================================
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

counters.forEach(counter => observer.observe(counter));
