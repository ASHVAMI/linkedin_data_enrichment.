import requests
import os

API_KEY = os.getenv('LINKEDIN_API_KEY')
API_HOST = "linkedin-bulk-data-scraper.p.rapidapi.com"
API_URL = "https://linkedin-bulk-data-scraper.p.rapidapi.com/api"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

def scrape_company_data(linkedin_url: str) -> dict:
    querystring = {"companyProfileUrl": linkedin_url}
    
    response = requests.get(API_URL, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        filtered_data = {k: v for k, v in data.items() if not any(substring in k for substring in ['affiliatedOrganizations', 'locations', 'similarOrganizations'])}
        return filtered_data
    else:
        print(f"Error: {response.status_code}")
        return None