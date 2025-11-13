import { RouteMapViewer } from "../map/RouteMapViewer.js";
import { Urls } from "../helpers/urls.js";
import { setMapFilters } from "./map_menu.js";

export const map = new RouteMapViewer();

try {
  let token = document.querySelector("#app-config").dataset.authToken;
  console.log(token);

  const response = await fetch(Urls.home_cities, {
    headers: {
      "X-Auth-Token": token
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const data = await response.json();

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

  setMapFilters(map);

} catch (error) {
  console.log("HomeAPI: " + error);
}
