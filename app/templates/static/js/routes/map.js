const url_python = 'http://127.0.0.1:8000/api/routes/'
    fetch(url_python)
    .then(res => res.json())
    .then(rotas => {
        rotas.forEach(e => {
            console.log(e.id_route)
        })
    })


const setRoutesOnMap = (dataRoutes) => {
    dataRoutes.forEach(e => {
        let map = L.map(e.map, {scrollWheelZoom: false}).setView([e.view[0], e.view[1]], 12);
        const idRoutesUser = e.routes;
        const markerCoords = e.marks;

        idRoutesUser.forEach(e => {
            const route = getRoutes().find(route => route.id_str === e)

            L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
                  attribution:
                    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong>ROTACRIC</strong>',
                }).addTo(map);
    
                var coordinates = L.Polyline.fromEncoded(
                  route.map.summary_polyline
                ).getLatLngs();
        
                L.polyline(coordinates, {
                  color: "red",
                  weight: 4,
                  opacity: 1,
                  lineJoin: "round",
                }).addTo(map); 
        });

        if(markerCoords != undefined) {
        markerCoords.forEach(e => {
            const newIcon = new L.Icon({
                iconUrl: e.icon,
                iconSize: [30, 40],
                iconAnchor: [5, 30],
                popupAnchor: [10, -20]
            })

            L.marker([e.lat, e.lng],{icon: newIcon})
            .bindPopup(`
            ${bindPopupName(e.name)} 
            ${bindPopupImage(e.image)}
            ${bindPopupAddress(e.address)}
            ${bindPopupOpeningHours(e.openingHours)}
            ${bindPopupPhone(e.phone)}
            `,{
            maxWidth: 150,
            keepInView: true,
            className: "markerPopup"
            })
            .addTo(map)
        });
    }
    });
}

const bindPopupName = (name) => {
    return `<h1>${name}</h1>`;
}

const bindPopupImage = (image) => {
    if(image == null) {
        return `<p>Foto não informada</p>`
    }
    return `<img src=${image}>`;
}

const bindPopupAddress = (address) => {
    return `<p>Endereço: ${address}</p>`;
}

const bindPopupOpeningHours = (hours) => {
    return `<p>Horário de atendimento: ${hours}</p>`;
}

const bindPopupPhone = (phone) => {
    return `<p>Contato: ${phone}</p>`;
}

const getMaps = (dataRoutes) => {
    const userRoutes = [];
    dataRoutes.forEach(element => {
        userRoutes.push(element.routes);
    });
    return userRoutes;
}