export class Map {

  constructor() {
    this.map = null;
  }

  setMap(lat, lng) {
    this.map = L.map('map', {scrollWheelZoom: false}).setView([lat, lng], 12);

    this.startMap()
  }

  getMap() {
    return this.map; 
  }

  startMap(){
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
                  attribution:
                    '&copy; <strong>ROTACRIC</strong>',
    }).addTo(this.map);
  }

  addRoutes(routes) {
    routes.forEach(e => {
      var coordinates = L.Polyline.fromEncoded(
      e.polyline
    ).getLatLngs();
        
    L.polyline(coordinates, {
      color: "red",
      weight: 4,
      opacity: 1,
      lineJoin: "round",
    }).addTo(this.map);
    })
  }

  addPoints(points) {
    points.forEach(({ coordinates, name, category, image, address, business_hours, phone }) => {
      const iconUrl = category?.image ?? '/default-icon.png';

      const newIcon = new L.Icon({
        iconUrl,
        iconSize: [30, 40],
        iconAnchor: [5, 30],
        popupAnchor: [10, -20]
      });

      const popupContent = `
        <h1>${name}</h1>
        ${image ? `<img src=${image}>` : `<p>Foto não informada</p>`}
        <p>Endereço: ${address.street_name}, ${address.number}, ${address.neighborhood}</p>
        <p>Horário de atendimento: ${business_hours}</p>
        <p>Contato: ${phone}</p>
      `;

      L.marker([coordinates.lat, coordinates.lng], { icon: newIcon })
        .bindPopup(popupContent, {
          maxWidth: 150,
          keepInView: true,
          className: 'markerPopup'
        })
        .addTo(this.map);
    });
  }
}