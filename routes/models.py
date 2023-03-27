from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import requests, json


class Route(models.Model):
    name = models.CharField(max_length=250)
    id_route = models.CharField(max_length=50)
    polilyne = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_routes(self):
        data = Route.objects.all()
        return data


class Api:
    def __init__(self):
        self.user_data = {
            'client_id': "93689",
            'client_secret': "05d5dd63dabb33ba2514308b74256983c3edb146",
            'refresh_token': "e162d2a39fe9b35a1c4f1df5bda5157bcfbfd6ea",
            'grant_type': "refresh_token",
            'f': 'json'
        }
        self.auth_url = 'https://www.strava.com/oauth/token'
        self.route_url = 'https://www.strava.com/api/v3/routes/'
    
    def getAccessToken(self):
        res = requests.post(self.auth_url, data=self.user_data, verify=False)
        access_token = res.json()['access_token']
        return access_token

    def getRoute(self, idRoute):
        header = {'Authorization': 'Bearer ' + self.getAccessToken()}
        param = {'per_page': 200, 'page': 1}
        my_dataset = requests.get(self.route_url+idRoute, headers=header, params=param).json()
        return my_dataset['id_str']


api = Api()
# print(api.getRoute('3007668662019916668'))

arr_polilyne = []

route = Route()

print(route.get_routes())

for route in route.get_routes():
    apiResult = api.getRoute(route.id_route)
    print(apiResult)
    # route.polilyne = api.getRoute(route.id_route)
    # route.save()
    # print('Salvo')