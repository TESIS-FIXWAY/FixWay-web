document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelector('.slides');
    const slideCount = document.querySelectorAll('.slide').length;
    let index = 0;

    function showSlide(n) {
        if (n >= slideCount) index = 0;
        if (n < 0) index = slideCount - 1;
        slides.style.transform = `translateX(-${index * 100}%)`;
    }

    document.querySelector('.next').addEventListener('click', function() {
        index++;
        showSlide(index);
    });

    document.querySelector('.prev').addEventListener('click', function() {
        index--;
        showSlide(index);
    });

    // Auto slide every 5 seconds
    setInterval(function() {
        index++;
        showSlide(index);
    }, 5000);
});
