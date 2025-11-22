import { RouteMapViewer } from "../map/RouteMapViewer.js";
import { Urls } from "../helpers/urls.js";
import { setMapFilters } from "./map_menu.js";
import { ApiClient } from "../helpers/apiClient.js";

export const map = new RouteMapViewer();
const api = new ApiClient();

try {
  const data = await api.fetch(Urls.home_cities);

  map.setMap(
    "map",
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
  console.error("HomeAPI:", error);
}
