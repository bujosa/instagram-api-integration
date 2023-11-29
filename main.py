
import requests

base_url = "https://graph.instagram.com"
access_token = "YOUR TOKEN"

# Endpoint to get the feed
endpoint = "/me/media"
url = f"{base_url}{endpoint}"

# Request parameters
params = {
    "fields": "id,caption,media_type,media_url,thumbnail_url,permalink,timestamp",
    "access_token": access_token
}

# Make the GET request
response = requests.get(url, params=params)

# Check the status of the response
if response.status_code == 200:
    # The request was successful, process the data
    data = response.json()
    print(data)
else:
    # The request failed, display the status code and error message
    print(f"Error: {response.status_code} - {response.text}")
