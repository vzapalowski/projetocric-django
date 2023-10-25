import { map } from "./data.js";

const menu = document.querySelector('.map-menu');
const routeCheckboxes = document.querySelector('#routeCheckboxes');
const pointsCheckboxes = document.querySelector('#pointsCheckboxes');

document.querySelector('.btn-close-menu').addEventListener('click', () => {
    menu.classList.add('hidden');
});

document.querySelector('.btn-open-menu').addEventListener('click', () => {
    menu.classList.remove('hidden');
});

document.querySelector('.btn-open-route-filter').addEventListener('click', () => {
    if (routeCheckboxes.classList.contains('hidden')) {
        map.hideAllRoutes();
        routeCheckboxes.classList.remove('hidden');
    } else {
        map.showAllRoutes();
        routeCheckboxes.classList.add('hidden');
        document.querySelectorAll('.r-cb-iptn').forEach(e => {
            e.checked = false;
        })
    }
});

document.querySelector('.btn-open-points-filter').addEventListener('click', () => {
    if (pointsCheckboxes.classList.contains('hidden')) {
        map.hideAllPoints();
        pointsCheckboxes.classList.remove('hidden');
    } else {
        map.showAllPoints();
        pointsCheckboxes.classList.add('hidden');
        document.querySelectorAll('.p-cb-iptn').forEach(e => {
            e.checked = false;
        });
    }
});
