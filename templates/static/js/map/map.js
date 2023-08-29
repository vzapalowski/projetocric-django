export class Map {

  constructor() {
    this.map = null;
  }

  setMap(map, options, lat, lng, zoom) {
    this.map = L.map(map, options).setView([lat, lng], zoom);

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

  addRoutes(routes, opacity=1) {
    routes.forEach(e => {
      var coordinates = L.Polyline.fromEncoded(
      e.polyline
    ).getLatLngs();

    L.polyline(coordinates, {
      color: e.color,
      weight: 3,
      opacity: opacity,
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

  writeRoutes(routes) {
    var btns = document.querySelectorAll('.btnOpacity');
    var currentRoute = null;
  
    btns.forEach((button) => {
      button.addEventListener('click', () => {
        var routeId = button.getAttribute('data-route');
        var selectedRoute = this.getRouteById(routes, routeId);
  
        if (selectedRoute) {
          if (currentRoute) {
            this.updateOpacity(currentRoute, 0);
            currentRoute.button.style.backgroundColor = '';
          }
  
          this.updateOpacity(selectedRoute, 1);
          currentRoute = selectedRoute;
          button.style.backgroundColor = selectedRoute.color; 
          currentRoute.button = button; 
        }
      });
    });
  }
  
  getRouteById(routes, routeId) {
    return routes.find((route) => route.id_route === routeId);
  }
  
  updateOpacity(route, opacityValue) {
    if (route.polylineLayer && this.map.hasLayer(route.polylineLayer)) {
      this.map.removeLayer(route.polylineLayer);
    }
  
    var coordinates = L.Polyline.fromEncoded(route.polyline).getLatLngs();
    route.polylineLayer = L.polyline(coordinates, {
      color: route.color,
      weight: 3,
      opacity: opacityValue,
      lineJoin: "round"
    }).addTo(this.map);
  }
  
  
  addPointsEvent(points) {
    points.forEach(({ coordinates, title, iconUrl}) => {

      const newIcon = new L.Icon({
        iconUrl,
        iconSize: [50, 25],
        iconAnchor: [5, 30],
        popupAnchor: [10, -20]
      });

      const popupContent = `
        <h1>${title}</h1>
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