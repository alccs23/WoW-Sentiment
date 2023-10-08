import requests
import json
# Define the URL
url = "https://us.forums.blizzard.com/en/wow/c/community/general-discussion/171/l/latest.json?ascending=false&no_definitions=true&page=1"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
     # Specify the output file name
    output_file = "forum_data.json"
    
    # Write the JSON data to the output file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Data saved to {output_file}")
    
    # Access and process the data as needed
    # For example, you can print the JSON data
    topics = data['topic_list']

      # Specify the output file name
    output_file = "Topics_list.json"
    
    # Write the JSON data to the output file
    with open(output_file, 'w') as json_file:
        json.dump(topics, json_file, indent=4)
    
    print(f"Data saved to {output_file}")
    
    slug = topics['topics']
    actuallySlug = slug[0]['slug']
    output_file = "slugTime"
    with open(output_file, 'w') as json_file:
        json.dump(slug, json_file, indent=4)
    print(actuallySlug)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
