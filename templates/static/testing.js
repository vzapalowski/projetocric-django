const url = 'http://127.0.0.1:8000/api/routes/'

const api = () => {
    fetch(url)
    .then(res => res.json())
    .then(rotas => {
        escrevendo(rotas)
    })
}

const escrevendo = (rotas) => {
    rotas.forEach(e => {
        console.log(e.id)
    });
}

api()