import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";

const eventId = window.location.href.match(/\/(\d+)\/?$/)[1];
const url_api = Urls.events + eventId;

fetch(url_api)
.then(res => res.json())
.then(data => {
    let map = new Map();
    map.setMap(data.coordinates.lat, data.coordinates.lng);
    map.addRoutes(data.routes);
})