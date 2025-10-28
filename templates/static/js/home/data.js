import { RouteMapViewer } from "../map/RouteMapViewer.js";
import { Urls } from "../helpers/urls.js";
import { setMapFilters } from "./map_menu.js";

export const map = new RouteMapViewer();

try {
  fetch(Urls.home_cities)
    .then(res => res.json())
    .then(data => {

      map.setMap(
        'map',
        { scrollWheelZoom: false, doubleClickZoom: false },
        data.latitude,
        data.longitude,
        data.zoom
      );

      map.addRoutes(data.routes);
      map.addPoints(data.points);

      map.togglePointsLayer();
      map.createRouteCheckboxes(data.routes);
      map.createPointCheckboxes(data.points);
      map.filterPointsByCategory();
    });
} catch (error) {
  console.log("HomeAPI: " + error)
}

setMapFilters(map)
// Código Inutilizado

// try {
//   fetch(Urls.event_list)
//     .then(res => res.json())
//     .then(data => {
//       data.forEach(event => {
//         var eventMap = new Map();
//         eventMap.setMap(
//           `event-map-${event.id}`,
//           { scrollWheelZoom: false, dragging: false, zoomControl: false, doubleClickZoom: false },
//           event.coordinates.lat,
//           event.coordinates.lng,
//           event.zoom
//         )
//         let routes = data[event].routes_data.map(route => route.route)
//         eventMap.addRoutes(routes)
//       });

//     });
// } catch (error) {
//   console.log("EventAPI: " + error)
// }