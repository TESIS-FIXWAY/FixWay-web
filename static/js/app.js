document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.side .item');
    let currentIndex = 0;

    function showItem(index) {
    items.forEach((item, i) => {
        item.classList.toggle('active', i === index);
    });
    const offset = -index * 100;
    document.querySelector('.side').style.transform = `translateX(${offset}%)`;
    }

    document.querySelector('.prev').addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : items.length - 1;
    showItem(currentIndex);
    });

    document.querySelector('.next').addEventListener('click', () => {
    currentIndex = (currentIndex < items.length - 1) ? currentIndex + 1 : 0;
    showItem(currentIndex);
    });
});
