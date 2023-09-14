if (window.location.href.split('/')[5]) {
    document.querySelector('#form-h2').scrollIntoView();
  }
  
  document.querySelector('#btn-clean').addEventListener('click', () => {
    document.querySelectorAll('.form-control').forEach(e => {
      e.value = "";
    });
  });

  document.querySelector('.btn-login').addEventListener('click', () => {
    window.location.href = loginUrl
  });