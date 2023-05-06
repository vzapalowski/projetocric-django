const form = document.querySelector('#enrollment-form')
form.addEventListener('submit', (event) => {
    const inputs = form.querySelectorAll('input, select, textarea');
    let isFormValid = true;

    inputs.forEach((input) => {
      if (!input.value.trim()) {
        isFormValid = false;
        input.classList.add('is-invalid');
      } else {
        input.classList.remove('is-invalid');
      }
    });

    if (!isFormValid) {
      event.preventDefault();
      alert('Please fill out all fields!');
    }
});