import requests

# Define the URL
url = "https://us.forums.blizzard.com/en/wow/c/community/general-discussion/171/l/latest.json?ascending=false&no_definitions=true&page=1"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Access and process the data as needed
    # For example, you can print the JSON data
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
