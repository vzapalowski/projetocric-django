import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";

const cityId = window.location.href.split("/")[4];
const url_api = Urls.cities + cityId;

let arr = []

export const map = new Map();
fetch(url_api)
.then(res => res.json())
.then(data => {
    map.setMap('map', {
        scrollWheelZoom: false,
        doubleClickZoom: false
    }, data.coordinates.lat, data.coordinates.lng, data.zoom);
    
    map.addRoutes(data.routes);
    map.addPoints(data.points)
    map.togglePointsLayer();
    map.createRouteCheckboxes(data.routes);
    map.filterPointsByCategory();

    data.routes.forEach(route => {
        map.addSegments(route.id_route);
    });
})