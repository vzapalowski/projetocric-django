import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";


export const map = new Map();
try {
  fetch(Urls.home_cities)
    .then(res => res.json())
    .then(data => {
      // let southWest = L.latLng(-30.140440, -51.493143);
      // let northEast = L.latLng(-29.769673, -52.224405);
      // let bounds = L.latLngBounds(southWest, northEast);

      const CARBO_REGION_POSITION = {
        latitude: -29.9949289,
        longitude: -51.8243548
      }

      // map.setMap(
      //   'map',
      //   { scrollWheelZoom: false, doubleClickZoom: false },
      //   data[0]['coordinates'].lat,
      //   data[0]['coordinates'].lng,
      //   10
      // );

      map.setMap(
        'map',
        { scrollWheelZoom: false, doubleClickZoom: false },
        CARBO_REGION_POSITION.latitude,
        CARBO_REGION_POSITION.longitude,
        10
      );

      map.addRoutes(data.routes);
      map.addPoints(data.points);
      map.togglePointsLayer();
      map.createRouteCheckboxes(data.routes);
      map.filterPointsByCategory();
    });


  fetch(Urls.event_list)
    .then(res => res.json())
    .then(data => {
      for (let event in data) {
        let eventMap = new Map();
        eventMap.setMap(`event-map-${data[event].id}`, {
          scrollWheelZoom: false,
          dragging: false,
          zoomControl: false,
          doubleClickZoom: false
        }, data[event]['coordinates'].lat, data[event]['coordinates'].lng, data[event].zoom);
        let routes = data[event].routes_data.map(route => route.route)
        eventMap.addRoutes(routes)
      }
    });
} catch (error) {
  console.log(error)
}