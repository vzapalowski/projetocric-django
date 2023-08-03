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

if (!isHome == '' || !isHome[0] == '#') {
    document.querySelectorAll('.page-nav-item').forEach(e => {
        e.addEventListener('click', () => {
            window.location = homeUrl + e.getAttribute('href');
            // document.querySelector(isHome).scrollIntoView();
        });
    });
} else {
    document.querySelectorAll('.page-nav-item').forEach(e => {
        e.addEventListener('click', () => {
          setTimeout(() => {
            document.querySelector(e.getAttribute('href')).scrollIntoView();
          }, 500);
        });
    });
}