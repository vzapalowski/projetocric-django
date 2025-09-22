
const dateInput = document.getElementById('datepicker');
const rgInput = document.getElementById('id_rg');

dateInput.addEventListener('input', () => {
    let val = dateInput.value.replace(/\D/g, '');
    if(val.length > 8) val = val.slice(0,8);

    if(val.length > 4) val = val.slice(0,2) + '/' + val.slice(2,4) + '/' + val.slice(4);
    else if(val.length > 2) val = val.slice(0,2) + '/' + val.slice(2);

    dateInput.value = val;
});


rgInput.addEventListener('input', () => {
    rgInput.value = rgInput.value.replace(/\D/g,'').slice(0,10);
});

rgInput.addEventListener('blur', () => {
    const digits = rgInput.value.replace(/\D/g,'');
    if(digits.length !== 10) {
        rgInput.setCustomValidity("RG inválido: deve ter 10 números.");
    } else {
        rgInput.setCustomValidity("");
    }}
);

rgInput.addEventListener('input', () => {
    rgInput.setCustomValidity("");
});