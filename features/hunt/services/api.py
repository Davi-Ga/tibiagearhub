import requests

class TibiaDataAPI:
    def __init__(self) -> None:
        self.url = "https://api.tibiadata.com/v4/"
    
    def get_creatures(self) -> dict:
        response = requests.get(f"{self.url}" + "creatures/")
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def get_especific_creature(self, race: str) -> dict:
        response = requests.get(f"{self.url}creatures/{race}")
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
        