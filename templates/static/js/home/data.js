import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";

fetch(Urls.home_cities)
    .then(res => res.json())
    .then(data => {
        let map = new Map();
        map.setMap('map', {scrollWheelZoom: false}, data[0]['coordinates'].lat, data[0]['coordinates'].lng, 10);
        map.addRoutes(data[0].routes);
        map.addPoints(data[0].points);
    });

fetch(Urls.event_list)
    .then(res => res.json())
    .then(data => {
        for(let event in data) {
            let eventMap = new Map();
            eventMap.setMap(`event-map-${data[event].id}`, {
                scrollWheelZoom: false, 
                dragging: false, 
                zoomControl: false
            }, data[event]['coordinates'].lat, data[event]['coordinates'].lng, data[event].zoom);
            let routes = data[event].routes_data.map(route => route.route)
            eventMap.addRoutes(routes)
        }
    });