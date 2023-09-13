const bannerItem = document.querySelectorAll('.cities-container');

document.querySelector('.banner-container').addEventListener('mouseover', () => {
    bannerItem.forEach(e => {
        e.classList.add("dark-city");
    });
});

document.querySelector('.banner-container').addEventListener('mouseout', () => {
    bannerItem.forEach(e => {
        e.classList.remove("dark-city");
    });
});

bannerItem.forEach(e => {
    e.addEventListener('mouseover', () => {
        setTimeout(() => {
            e.classList.remove("dark-city");
        }, 50);
    });
});
