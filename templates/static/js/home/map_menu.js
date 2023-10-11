import { map } from "./data.js";

const menu = document.querySelector('.map-menu');
const cboxContainer = document.querySelector('.check-boxes-container');

document.querySelector('.btn-close-menu').addEventListener('click', () => {
    menu.style.display = 'none';
});

document.querySelector('.btn-open-menu').addEventListener('click', () => {
    menu.style.display = 'flex';
});

document.querySelector('.btn-open-filter').addEventListener('click', () => {
    if (cboxContainer.style.display == 'none') {
        map.hideAllRoutes();
        cboxContainer.style.display = 'grid';
    } else {
        map.showAllRoutes();
        cboxContainer.style.display = 'none';
    }
});