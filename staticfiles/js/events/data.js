import { RouteMapViewer } from "../map/RouteMapViewer.js";
import { Urls } from "../helpers/urls.js";
import { setMapFilters } from "../home/map_menu.js";

const eventId = window.location.href.split('/')[4];
const url_api = Urls.events + eventId;

var event_routes = []

var eventMap = new RouteMapViewer();

fetch(url_api)
    .then(res => res.json())
    .then(event => {

        eventMap.setMap('map',
            { scrollWheelZoom: false },
            event.coordinates.lat,
            event.coordinates.lng,
            event.zoom
        );

        event.routes.forEach((e) => {
            event_routes.push(e.route)
        })

        eventMap.addRoutes(event_routes)
        eventMap.addPoints(event.anchorpoint)

        eventMap.togglePointsLayer();
        eventMap.createRouteCheckboxes(event_routes);
        eventMap.createPointCheckboxes(event.anchorpoint);
        eventMap.filterPointsByCategory();
    })

setMapFilters(eventMap)