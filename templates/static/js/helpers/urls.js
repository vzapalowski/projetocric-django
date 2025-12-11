export const getEnvironmentURL = (path = "") => {
    return `${window.location.protocol}//${window.location.host }/${path}`;
}

export const Urls = {
    environment: getEnvironmentURL(),
    cities: getEnvironmentURL('api/cities/'),
    home_cities: getEnvironmentURL('api/home_cities/'),
    events: getEnvironmentURL('api/events/'),
    event_list: getEnvironmentURL('api/event_list/')
}