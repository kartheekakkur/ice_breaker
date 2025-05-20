import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str , mock: bool = False) -> dict:
    """
    This function retrieves LinkedIn Profile from the Scrap API.
    https://www.scraperapi.com
    It requires the scrape environment variable to be set.
    """

    if mock:
        linkedin_profile_url ="https://gist.githubusercontent.com/kartheekakkur/45239fdd9ecfb1e08b46e4e5193e7dac/raw/5767e22ca16859797ea206d88836443543187f32/vakkur-scrapin.json"
        response = requests.get(linkedin_profile_url,timeout=10)

        data =response.json().get("person")

        return data
    else:

        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "linkedInUrl": linkedin_profile_url,
            "apikey": os.environ["SCRAPIN_API_KEY"]
        }

        response = requests.get(api_endpoint, params=params, timeout=10)

        data = response.json().get("person")

        data = {
            k: v 
            for k, v in data.items() if v not in [[],"","", None]
        }

        return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile("https://www.linkedin.com/in/vkakkur",mock=False)
    )
    
