document.querySelector('#fab-button').addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
});

document.querySelector('.logo-container').addEventListener('click', () => {
    window.location = homeUrl;
});

const isHome = window.location.href.split('/')[3];

document.querySelectorAll('.page-nav-item').forEach(e => {
    e.addEventListener('click', () => {
        if (!isHome == '' || !isHome[0] == '#') {
            window.location = homeUrl + e.getAttribute('href');
        } else {
            setTimeout(() => {
                document.querySelector(e.getAttribute('href')).scrollIntoView();
            }, 500);
        }
    });
});