import requests
import json
forumTitlesSlug = []
for n in range(10):
    # Define the URL
    url = "https://us.forums.blizzard.com/en/wow/c/community/general-discussion/171/l/latest.json?ascending=false&no_definitions=true&page=" + str(n)

    # Send an HTTP GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        for i in range(30):
            slug = data['topic_list']['topics'][i]['slug']
            forumTitlesSlug.append(slug)
            
    
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
print(len(forumTitlesSlug))


