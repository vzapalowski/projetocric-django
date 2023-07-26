const messageCard = document.querySelector('.message-container');

function hideMessageContainer() {
    if (messageCard) {
        setTimeout(() => {
        messageCard.classList.add('hide');
        }, 5000);
    }
}

window.onload = () => {
    hideMessageContainer();
    const fadeOutDuration = 1000;
    setTimeout(() => {
        if (messageCard) {
            messageCard.remove();
        }
    }, 5000 + fadeOutDuration);
}