import { RouteMapViewer } from "../map/RouteMapViewer.js";
import { Urls } from "../helpers/urls.js";

const cityId = window.location.href.split("/")[4];
const url_api = Urls.cities + cityId;

let arr = [];

export const map = new RouteMapViewer();

try {
  let token = document.querySelector("#app-config").dataset.authToken;
  const response = await fetch(url_api, {
    headers: {
      "X-Auth-Token": token,
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status ${response.status}`);
  }

  const data = await response.json();

  map.setMap(
    "map",
    { scrollWheelZoom: false, doubleClickZoom: false },
    data.coordinates.lat,
    data.coordinates.lng,
    data.zoom
  );
  if (data.routes) {
    data.routes = data.routes.filter((route) => !route.is_event_route);
    map.addRoutes(data.routes);
  }
  map.addPoints(data.points);
  map.togglePointsLayer();
  map.createRouteCheckboxes(data.routes);
  map.filterPointsByCategory();
} catch (error) {
  console.log("HomeAPI: " + error);
}

// fetch(url_api)
//   .then((res) => res.json())
//   .then((data) => {
//     map.setMap(
//       "map",
//       { scrollWheelZoom: false, doubleClickZoom: false },
//       data.coordinates.lat,
//       data.coordinates.lng,
//       data.zoom
//     );
//     if (data.routes) {
//       data.routes = data.routes.filter((route) => !route.is_event_route);
//       map.addRoutes(data.routes);
//     }
//     map.addPoints(data.points);
//     map.togglePointsLayer();
//     map.createRouteCheckboxes(data.routes);
//     map.filterPointsByCategory();
//   });
