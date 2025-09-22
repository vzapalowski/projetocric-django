// -------------------------
// Data de Nascimento
// -------------------------
const dateInput = document.getElementById('datepicker');

dateInput.addEventListener('input', () => {
    let val = dateInput.value.replace(/\D/g, '');
    if(val.length > 8) val = val.slice(0,8);

    if(val.length > 4) val = val.slice(0,2) + '/' + val.slice(2,4) + '/' + val.slice(4);
    else if(val.length > 2) val = val.slice(0,2) + '/' + val.slice(2);

    dateInput.value = val;
});

dateInput.addEventListener('blur', () => {
    const value = dateInput.value;
    const regex = /^(\d{2})\/(\d{2})\/(\d{4})$/;

    if(!regex.test(value)) {
        dateInput.setCustomValidity("Data inválida. Use o formato dd/mm/aaaa.");
        return;
    }

    let [, day, month, year] = value.match(regex).map(Number);

    if(year < new Date().getFullYear() - 200) {
        dateInput.setCustomValidity("Ano muito antigo.");
        return;
    }

    if(month < 1 || month > 12) {
        dateInput.setCustomValidity("Mês inválido.");
        return;
    }

    if(day < 1 || day > 31) {
        dateInput.setCustomValidity("Dia inválido.");
        return;
    }

    const date = new Date(year, month - 1, day);
    if(date.getDate() !== day || date.getMonth() !== month - 1 || date.getFullYear() !== year) {
        dateInput.setCustomValidity("Data inválida. Verifique o dia, mês e ano.");
        return;
    }

    dateInput.setCustomValidity("");
});

dateInput.addEventListener('input', () => {
    dateInput.setCustomValidity("");
});

// -------------------------
// RG
// -------------------------
const rgInput = document.getElementById('id_rg');

rgInput.addEventListener('input', () => {
    rgInput.value = rgInput.value.replace(/\D/g,'').slice(0,10);
    rgInput.setCustomValidity("");
});

rgInput.addEventListener('blur', () => {
    const digits = rgInput.value.replace(/\D/g,'');
    if(digits.length !== 10) {
        rgInput.setCustomValidity("RG inválido: deve ter 10 números.");
    } else {
        rgInput.setCustomValidity("");
    }
});
