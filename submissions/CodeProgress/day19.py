import requests

api_url = 'https://api.spacexdata.com/v5/launches/latest'

try:
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        print("Latest SpaceX Launch Details:")
        print("Mission Name:", data.get('name', 'N/A'))
        print("Flight Number:", data.get('flight_number', 'N/A'))
        print("Launch Date:", data.get('date_utc', 'N/A'))
        print("Rocket Name:", requests.get(f"https://api.spacexdata.com/v5/rockets/{data.get('rocket', 'N/A')}").json().get('name', 'N/A'))
        print("Launch Site:", data.get('launchpad', {}).get('name', 'N/A'))
        print("Details:", data.get('details', 'N/A'))
    else:
        print("Failed to fetch data from the SpaceX API. Response status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", str(e))
