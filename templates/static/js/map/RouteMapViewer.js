import { getEnvironmentURL } from '../helpers/urls.js';

// Constante de configuração Geral
const MAP_CONFIG = {
  tileLayer: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  attribution: '&copy; <strong>ROTACRIC</strong>',
  defaultIcon: '/static/default-icon.png',
  iconSize: [30, 40],
  iconAnchor: [5, 30],
  popupAnchor: [10, -20],
  eventIconSize: [50, 25],
  polylineStyle: {
    weight: 3,
    lineJoin: "round"
  }
};

// Models: Apenas para entender como a classe espera os modelos utilizados
class Route {
  constructor(id, name, external_strava_id, color, polyline) {
    this.id = id;
    this.name = name;
    this.external_strava_id = external_strava_id;
    this.color = color;
    this.polyline = polyline;
    this.polylineLayer = null;
  }
}

class Point {
  constructor(coordinates, name, anchorpoint_category, image, address, business_hours, phone) {
    this.coordinates = coordinates;
    this.name = name;
    this.anchorpoint_category = anchorpoint_category;
    this.image = image;
    this.address = address;
    this.business_hours = business_hours;
    this.phone = phone;
  }
}

export class RouteMapViewer {
  constructor() {
    this.map = null;
    this.bounds = null;
    this.lastValidCenter = null;
    this.pointLayerGroup = L.layerGroup();
    this.currentRoute = null;
  }

  // Map Initialization
  setMap(map, options, lat, lng, zoom, bounds = null) {
    this.map = L.map(map, options).setView([lat, lng], zoom);

    if (bounds) {
      this.bounds = bounds;
      this.map.setMaxBounds(bounds);
    }

    this.lastValidCenter = this.map.getCenter();
    this._initializeMap();
  }

  getMap() {
    return this.map;
  }

  _initializeMap() {
    L.tileLayer(MAP_CONFIG.tileLayer, {
      attribution: MAP_CONFIG.attribution
    }).addTo(this.map);

    this._setupMapBounds();
  }

  _setupMapBounds() {
    this.map.on('drag', () => {
      const currentCenter = this.map.getCenter();

      if (this.bounds && !this.bounds.contains(currentCenter)) {
        this.map.panTo(this.lastValidCenter);
        window.scrollBy(0, 190);
      }

      this.lastValidCenter = currentCenter;
    });
  }

  // Route Management
  addRoutes(routes, opacity = 1) {
    routes.forEach(route => {
      const coordinates = this._decodePolyline(route.polyline);

      L.polyline(coordinates, {
        color: route.color,
        opacity: opacity,
        ...MAP_CONFIG.polylineStyle
      }).addTo(this.map);
    });
  }

  hideAllRoutes() {
    this._forEachPolyline(layer => layer.setStyle({ opacity: 0 }));
  }

  showAllRoutes() {
    this._forEachPolyline(layer => layer.setStyle({ opacity: 1 }));
  }

  _forEachPolyline(callback) {
    this.map.eachLayer(layer => {
      if (layer instanceof L.Polyline) {
        callback(layer);
      }
    });
  }

  _decodePolyline(polyline) {
    return L.Polyline.fromEncoded(polyline).getLatLngs();
  }

  // Point Management
  addPoints(points) {
    points.forEach(point => this._createPointMarker(point));
    this.map.addLayer(this.pointLayerGroup);
  }

  _createPointMarker(point) {
    const { coordinates, name, anchorpoint_category, image, address, business_hours, phone } = point;

    const icon = this._createIcon(getEnvironmentURL(anchorpoint_category?.icon_path));
    const popupContent = this._createPopupContent(name, image, address, business_hours, phone);
    const marker = L.marker([coordinates.lat, coordinates.lng], {
      icon,
      category: anchorpoint_category?.name
    });

    marker.bindPopup(popupContent, {
      maxWidth: 150,
      keepInView: true,
      className: 'markerPopup'
    }).addTo(this.pointLayerGroup);
  }

  _createIcon(iconPath) {
    return new L.Icon({
      iconUrl: iconPath || MAP_CONFIG.defaultIcon,
      iconSize: MAP_CONFIG.iconSize,
      iconAnchor: MAP_CONFIG.iconAnchor,
      popupAnchor: MAP_CONFIG.popupAnchor
    });
  }

  _createPopupContent(name, image, address, business_hours, phone) {
    return `
      <h1>${name}</h1>
      ${image ? `<img src="${image}" alt="${name}">` : '<p>Foto não informada</p>'}
      <p>Endereço: ${address}</p>
      <p>Horário de atendimento: ${business_hours}</p>
      <p>Contato: ${phone}</p>
    `;
  }

  // Layer Visibility Control
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
    const buttons = document.querySelectorAll('.btnOpacity');

    buttons.forEach(button => {
      button.addEventListener('click', () => {
        this._handleRouteSelection(routes, button);
      });
    });
  }

  _handleRouteSelection(routes, button) {
    const routeId = button.getAttribute('data-route');
    const selectedRoute = this._getRouteById(routes, routeId);
    if (selectedRoute) {
      this._deselectCurrentRoute();
      this._selectRoute(selectedRoute, button);
    }
  }

  _deselectCurrentRoute() {
    if (this.currentRoute) {
      this._updateRouteOpacity(this.currentRoute, 0);
      this.currentRoute.button.style.backgroundColor = '';
    }
  }

  _selectRoute(route, button) {
    this._updateRouteOpacity(route, 1);
    button.style.backgroundColor = route.color;
    route.button = button;
    this.currentRoute = route;
  }

  _getRouteById(routes, routeId) {
    return routes.find(route => route.external_strava_id === routeId);
  }

  _updateRouteOpacity(route, opacity) {
    if (route.polylineLayer) {
      this.map.removeLayer(route.polylineLayer);
    }

    const coordinates = this._decodePolyline(route.polyline);
    route.polylineLayer = L.polyline(coordinates, {
      color: route.color,
      opacity: opacity,
      ...MAP_CONFIG.polylineStyle
    });

    this.map.addLayer(route.polylineLayer);
  }

  // UI Components

  createRouteCheckboxes(routes) {
    routes.forEach(route => {
      this._createRouteCheckbox(route);
    });

    this._setupCheckboxListeners(routes);
  }

  _createRouteCheckbox(route) {
    const checkboxHTML = `
      <div class="check-box-container d-block">
        <input id="route-${route.id}" type="checkbox" class="r-cb-iptn" data-route="${route.external_strava_id}">
        <span class="form-check-label fs-filter">${route.name}</span>
      </div>
    `;

    document.querySelector('#routeCheckboxes').insertAdjacentHTML('beforeend', checkboxHTML);
  }

  _setupCheckboxListeners(routes) {
    document.querySelectorAll('.r-cb-iptn').forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        const routeId = checkbox.getAttribute('data-route');
        const route = this._getRouteById(routes, routeId);

        if (route) {
          this._updateRouteOpacity(route, checkbox.checked ? 1 : 0);
        }
      });
    });
  }

  createPointCheckboxes(points) {
    const categoriesMap = new Map();

    points.forEach(point => {
      const categoryName = point.anchorpoint_category.name;
      if (!categoriesMap.has(categoryName)) {
        categoriesMap.set(categoryName, true);
        this._createPointCheckbox(point);
      }
    });

    this.filterPointsByCategory();
  }

  _createPointCheckbox(point) {
    const checkboxHTML = `
        <div class="check-box-container">
            <input type="checkbox" class="p-cb-iptn" data-category="${point.anchorpoint_category.name}" checked>
            <span>${point.anchorpoint_category.name}</span>
        </div>
    `;

    document.querySelector('#pointsCheckboxes').insertAdjacentHTML('beforeend', checkboxHTML);
  }

  filterPointsByCategory() {
    const checkboxes = document.querySelectorAll('.p-cb-iptn');

    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        this._filterPointsByCategory(checkbox);
      });
    });
  }

  _filterPointsByCategory(checkbox) {
    const category = checkbox.getAttribute('data-category');
    const markers = this.pointLayerGroup.getLayers();

    markers.forEach(marker => {
      if (marker.options.category === category) {
        if (checkbox.checked) {
          marker.addTo(this.map);
        } else {
          this.map.removeLayer(marker);
        }
      }
    });
  }
}