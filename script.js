
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const progressBar = document.getElementById('progressBar');
const slidePager = document.getElementById('slidePager');

function updateState() {
    // Update slides
    slides.forEach((slide, i) => {
        slide.classList.remove('active', 'prev', 'next');
        if (i === currentSlide) {
            slide.classList.add('active');
        } else if (i < currentSlide) {
            slide.classList.add('prev');
        } else {
            slide.classList.add('next');
        }
    });

    // Update Progress Bar
    const progress = ((currentSlide + 1) / totalSlides) * 100;
    progressBar.style.width = `${progress}%`;

    // Update Pager
    slidePager.innerText = `${(currentSlide + 1).toString().padStart(2, '0')} / ${totalSlides.toString().padStart(2, '0')}`;
}

function nextSlide() {
    if (currentSlide < totalSlides - 1) {
        currentSlide++;
        updateState();
    }
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        updateState();
    }
}

function goToSlide(index) {
    currentSlide = index;
    updateState();
}

// Keyboard Listeners
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
        nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        prevSlide();
    }
});

// Subtle Wheel Interaction (Throttled)
let lastScroll = 0;
document.addEventListener('wheel', (e) => {
    const now = Date.now();
    if (now - lastScroll < 1200) return;
    
    if (Math.abs(e.deltaY) > 10) {
        if (e.deltaY > 0) nextSlide();
        else prevSlide();
        lastScroll = now;
    }
}, { passive: true });

// Initial call
updateState();
