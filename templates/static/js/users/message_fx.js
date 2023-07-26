const messageCard = document.querySelector('.message-container');

window.onload = () => {
    if (messageCard) {
        setTimeout(() => {
            messageCard.classList.add('hide');
        }, 5000);
    }
}