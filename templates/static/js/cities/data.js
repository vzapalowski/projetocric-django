import { RouteMapViewer } from "../map/RouteMapViewer.js";
import { Urls } from "../helpers/urls.js";
import { ApiClient } from "../helpers/apiClient.js";

const cityId = window.location.href.split("/")[4];
const url_api = Urls.cities + cityId;

export const map = new RouteMapViewer();
const api = new ApiClient();

try {
  const data = await api.fetch(url_api);

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
  console.error("CityAPI:", error);
}
