// Filtrar por categoría
function filterByCategory(category) {
    const products = document.querySelectorAll('.product-card');
    const selectedCategory = document.getElementById('selectedCategory');
    products.forEach(product => {
        if (!category || product.dataset.category === category) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });

    if (category) {
        selectedCategory.innerHTML = `Categoría seleccionada: ${category} <span onclick="clearCategory()">[x]</span>`;
    } else {
        selectedCategory.innerHTML = '';
    }
}

// Limpiar categoría seleccionada
function clearCategory() {
    filterByCategory('');
}
