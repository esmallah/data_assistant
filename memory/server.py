import requests

class Connect:
    def __init__(self,server,latitude,longitude):
        '''connect server ( server name ,latidure  coordinates on earch ,longitude coordinate)'''
        self.server=server
        self.latitude=latitude
        self.longitude=longitude
    def status(self):
        response=requests.get(self.server+"/iss-now.json")
        status_code=response.status_code
        print (status_code)
    def location(self):#the server location by gps coordinates 
        parameters = {"lat":self.latitude, "lon":self.longitude}
        response=requests.get(self.server,params=parameters)
        content=response.content
        print (content)
        
    def content_type(self):
        response=requests.get(self.server)
        json_data=response.json()
        first_pass_duration=json_data["response"][0]["duration"]
        print(first_pass_duration)
        #get head of server responsd
        content_type=response.headers["content_type"]
        print(content_type)
    def count_people(self):
        #get count of people in space
        response = requests.get(self.server +"/astros.json")
        json_data=response.json()
        in_space_count=json_data["number"]
        print(in_space_count)

