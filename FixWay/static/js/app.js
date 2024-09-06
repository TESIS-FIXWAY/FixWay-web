let next = document.querySelector('.next');
let prev = document.querySelector('.prev');
let items = document.querySelectorAll('.item');
let currentIndex = 0;

// Muestra el slide activo y oculta los demás
function showSlide(index) {
    items.forEach((item, i) => {
        item.classList.toggle('active', i === index);
    });
}

// Muestra el siguiente slide
function nextSlide() {
    currentIndex = (currentIndex + 1) % items.length; // Avanza al siguiente índice
    showSlide(currentIndex);
}

// Muestra el slide anterior
function prevSlide() {
    currentIndex = (currentIndex - 1 + items.length) % items.length; // Retrocede al índice anterior
    showSlide(currentIndex);
}

// Inicializa el primer slide
showSlide(currentIndex);

next.addEventListener('click', nextSlide);
prev.addEventListener('click', prevSlide);

// Cambia automáticamente de slide cada 10 segundos
setInterval(nextSlide, 10000);