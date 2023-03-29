from django.db import models
from django.core.exceptions import ValidationError
import requests


class Route(models.Model):
    name = models.CharField(max_length=250)
    id_route = models.CharField(max_length=50, unique=True)
    polilyne = models.CharField(max_length=5000,blank=True, null=True)


    # def clean(self):
    #     api = Api()
    #     try:
    #         print('AQUI', api.getRoute(self.id_route))
    #     except KeyError:
    #         print("AQUI DEU O ERRO")

    def get_routes(self):
        data = Route.objects.all()
        return data
    
    def get_route(self, idRoute):
        return Route.objects.get(id_route=idRoute)


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
    
    def getAccessToken(self):
        res = requests.post(self.__auth_url, data=self.__user_data, verify=False)
        access_token = res.json()['access_token']
        return access_token

    def getRoute(self, idRoute):
        header = {'Authorization': 'Bearer ' + self.getAccessToken()}
        param = {'per_page': 200, 'page': 1}
        my_dataset = requests.get(self.__route_url+idRoute, headers=header, params=param).json()
        return my_dataset['map']['summary_polyline']