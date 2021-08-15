import requests

class Summoner:
    def __init__(self, host):
        self.host = host.platformRouting
        self.Token = host.Token

    def byEncryptedAccountId(self, accountId):
        def makeRequest():
            url = f"https://{self.host}/lol/summoner/v4/summoners/by-account/{accountId}"
            response = requests.get(url, headers={"X-Riot-Token":self.Token})
            self.byEncryptedAccountIdJson = response.json()

        makeRequest()
        return self.byEncryptedAccountIdJson

    def bySummonerName(self, summonerName):
        def makeRequest():
            url = f"https://{self.host}/lol/summoner/v4/summoners/by-name/{summonerName}"
            response = requests.get(url, headers={"X-Riot-Token": self.Token})
            self.byNameJson = response.json()

        makeRequest()
        return self.byNameJson

    def byEncryptedPUUID(self, puuid):
        def makeRequest():
            url = f"https://{self.host}/lol/summoner/v4/summoners/by-puuid/{puuid}"
            response = requests.get(url, headers={"X-Riot-Token":self.Token})
            self.byEncryptedPUUIDJson = response.json()

        makeRequest()
        return self.byEncryptedPUUIDJson

    def byEncryptedSummonerId(self,encryptedSummonerId):
        def makeRequest():
            url = f"https://{self.host}/lol/summoner/v4/summoners/{encryptedSummonerId}"
            response = requests.get(url, headers={"X-Riot-Token":self.Token})
            self.byEncryptedSummonerId = response.json()

        makeRequest()
        return self.byEncryptedSummonerId
