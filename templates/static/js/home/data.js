import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";

console.log(Urls.home_cities)

// fetch(Urls.home_cities)
//     .then(res => res.json())
//     .then(data => {
//         let map = new Map();
//         map.setMap(data[0]['coordinates'].lat, data[0]['coordinates'].lng);
//         map.addRoutes(data[0].routes);
//         map.addPoints(data[0].points);
// })