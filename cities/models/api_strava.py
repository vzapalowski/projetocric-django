import requests


class Api:
    def __init__(self):
        self.__user_data = {
            'client_id': "93689",
            'client_secret': "05d5dd63dabb33ba2514308b74256983c3edb146",
            'refresh_token': "e162d2a39fe9b35a1c4f1df5bda5157bcfbfd6ea",
            'grant_type': "refresh_token",
            'f': 'json'
        }
        self.__auth_url = 'https://www.strava.com/oauth/token'
        self.__route_url = 'https://www.strava.com/api/v3/routes/'
    
    def get_access_token(self): 
        res = requests.post(self.__auth_url, data=self.__user_data, verify=False)
        access_token = res.json()['access_token']
        return access_token

    def get_route(self, id_route):
        header = {'Authorization': 'Bearer ' + self.get_access_token()}
        param = {'per_page': 200, 'page': 1}
        my_dataset = requests.get(self.__route_url+id_route, headers=header, params=param).json()
        return my_dataset['map']['summary_polyline']