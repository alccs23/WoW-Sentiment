import requests
import json
import datetime

forumTitlesSlug = []
bins = {}

# Calculate the date 7 days ago from the current date
seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)
seven_days_ago_date = seven_days_ago.strftime("%Y-%m-%d")


for n in range(150):
    # Define the URL
    url = "https://us.forums.blizzard.com/en/wow/c/community/general-discussion/171/l/latest.json?ascending=false&no_definitions=true&page=" + str(n)

    # Send an HTTP GET request
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        for i in range(30):
            slug = data['topic_list']['topics'][i]
            date_part = slug["created_at"].split("T")[0]
            forumTitlesSlug.append(slug)
            # Check if the date_part is already a key in the dictionary
            
            # Calculate the date 7 days ago from the current date
            seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=60)
            seven_days_ago_date = seven_days_ago.strftime("%Y-%m-%d")

            #in allows forum titles that have been created in the last 7 days from when the code was run
            if date_part >= seven_days_ago_date:
                if date_part not in bins:
                    bins[date_part] = []
                
                # Append the slug to the corresponding bin
                bins[date_part].append(slug["slug"])

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


# Specify the file path where you want to save the .txt file
file_path = "dictOfTitles.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Iterate through the dictionary and write key-value pairs to the file
    for key, value in bins.items():
        file.write(f"{key}: {value}\n")