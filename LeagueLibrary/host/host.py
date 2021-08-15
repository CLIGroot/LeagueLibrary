import requests

platformID_List = ["br1","eun1","euw1","jp1","kr","la1","la2","na1","oc1","tr1","ru"]
regions_List = ["americas","asia","europe"]
url_Base = "api.riotgames.com"

class Host:
    def __init__(self, platformID, regions, token):
        self.Token = token
        self.platformID = platformID
        self.region = regions

        #PlatformID Verification
        if self.platformID.isupper():
            self.platformID = self.platformID.lower()

        if self.platformID in platformID_List:
            self.platformRouting = f"{self.platformID}.{url_Base}"

        else:
            raise Exception(f"[platformID]: '{self.platformID}' It's not on the list")

        #Regions Verification
        if self.region.isupper():
            self.region = self.region.lower()

        if self.region in regions_List:
            self.regionRouting = f"{self.region}.{url_Base}"

        else:
            raise Exception(f"[region]: '{self.region}' It's not on the list")

    def Status(self):
        def makeRequest():
            url = f"https://{self.platformRouting}/lol/status/v3/shard-data"
            response = requests.get(url, headers={"X-Riot-Token": self.Token})
            return response.json()
        statusResponse = makeRequest()

        for here in statusResponse['services']:
            if here['status'] == "online":
                print(f"[{here['name']}]: {here['status']}")
            else:
                print(f"[{here['name']}]: {here['status']}")
