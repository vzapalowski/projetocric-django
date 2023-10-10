const menu = document.querySelector('.map-menu');

document.querySelector('.btn-close-menu').addEventListener('click', () => {
    menu.style.display = 'none';
});

document.querySelector('.btn-map-menu').addEventListener('click', (e) => {
    menu.style.display = 'flex';
});