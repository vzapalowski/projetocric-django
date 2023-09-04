import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";

const cityId = window.location.href.split("/")[4];
const url_api = Urls.cities + cityId;

let arr = []

fetch(url_api)
.then(res => res.json())
.then(data => {

    let map = new Map();
    map.setMap(data.coordinates.lat, data.coordinates.lng, data.zoom);
    data.routes.forEach((e) => {
        arr.push(e)
    })

    map.addRoutes(arr, 0)
    map.addPoints(data.points)
    map.writeRoutes(arr);
})