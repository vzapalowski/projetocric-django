window.onload = () => {
    const toastMessages = document.querySelectorAll('.toast-message');

    toastMessages.forEach(toast => {
        toast.classList.add('show');

        setTimeout(() => {
            toast.classList.add('hide');

            toast.addEventListener('transitionend', () => {
                toast.remove();
            });
        }, 3000);
    });
};
