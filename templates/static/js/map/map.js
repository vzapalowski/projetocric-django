export class Map {

  constructor() {
    this.map = null;
    this.bounds = null; 
    this.lastValidCenter = null;
    this.pointLayerGroup = L.layerGroup();
  }

  setMap(map, options, lat, lng, zoom, bounds = null) {
    this.map = L.map(map, options).setView([lat, lng], zoom);

    if (bounds) {
      this.bounds = bounds;
      this.map.setMaxBounds(bounds);
    }

    this.lastValidCenter = this.map.getCenter();
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

    this.map.on('drag', () => {
      const currentCenter = this.map.getCenter();

      if (this.bounds && !this.bounds.contains(currentCenter)) {
        this.map.panTo(this.lastValidCenter);
        window.scrollBy(0, +190);
        this.lastValidCenter = currentCenter;
      } else {
        this.lastValidCenter = currentCenter;
      }
    });
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

  hideAllRoutes() {
    this.map.eachLayer(layer => {
      if (layer instanceof L.Polyline) {
        layer.setStyle({ opacity: 0 });
      }
    });
  }

  showAllRoutes() {
    this.map.eachLayer(layer => {
      if (layer instanceof L.Polyline) {
        layer.setStyle({ opacity: 1 });
      }
    });
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

      const marker = L.marker([coordinates.lat, coordinates.lng], { icon: newIcon });

      marker.options.category = category.name;
      
      marker.bindPopup(popupContent, {
        maxWidth: 150,
        keepInView: true,
        className: 'markerPopup'
      }).addTo(this.pointLayerGroup);
    });
    this.map.addLayer(this.pointLayerGroup);
  }

  togglePointsLayer() {
    document.querySelector('.btn-remove-points').addEventListener('click', () => {
      if (this.map.hasLayer(this.pointLayerGroup)) {
        this.hideAllPoints();
      } else {
        this.showAllPoints();
      }
    });
  }

  hideAllPoints() {
    this.map.removeLayer(this.pointLayerGroup);
  }

  showAllPoints() {
    this.map.addLayer(this.pointLayerGroup);
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
    if (route.polylineLayer) {
      this.map.removeLayer(route.polylineLayer);
    }
  
    var coordinates = L.Polyline.fromEncoded(route.polyline).getLatLngs();
    route.polylineLayer = L.polyline(coordinates, {
      color: route.color,
      weight: 3,
      opacity: opacityValue,
      lineJoin: "round"
    });

    this.map.addLayer(route.polylineLayer);
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

  createRouteCheckboxes(routes) {
    routes.forEach((route) => {
      const checkboxHTML = `
        <div class="check-box-container">
          <input type="checkbox" class="r-cb-iptn" data-route="${route.id_route}">
          <span>${route.name}</span>
        </div>
      `;
      document.querySelector('#routeCheckboxes').insertAdjacentHTML('beforeend', checkboxHTML);
    });

    document.querySelectorAll('.r-cb-iptn').forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        var routeId = checkbox.getAttribute('data-route');
        var checked = checkbox.checked;

        var route = this.getRouteById(routes, routeId);
        if (route) {
          if (checked) {
            this.updateOpacity(route, 1);
          } else {
            this.updateOpacity(route, 0);
          }
        }
      });
    });
  }

  filterPointsByCategory() {
    const checkboxes = document.querySelectorAll('.p-cb-iptn');
    
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        const category = checkbox.getAttribute('data-category');
        const markers = this.pointLayerGroup.getLayers();

        markers.forEach(marker => {
          const markerCategory = marker.options.category; 
          if (markerCategory === category) {
            if (checkbox.checked) {
              marker.addTo(this.map);
            } else {
              this.map.removeLayer(marker);
            }
          }
        });
      });
    });
  }
  
}