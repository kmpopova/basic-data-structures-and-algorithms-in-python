"""
Goal: create a script that parses a given webpage (e.g. a job board) and saves results as an overview in a text file.

"""

import requests
import math
from urllib.parse import unquote
import ast

# Ask user for the url or create initial url as a string.
initial_url = "https://karriereapi2.klinikum.uni-heidelberg.de/search/?data=%7B%22LanguageCode%22%3A%22DE%22%2C%22SearchParameters%22%3A%7B%22FirstItem%22%3A1%2C%22CountItem%22%3A10%2C%22Sort%22%3A%5B%7B%22Criterion%22%3A%22PublicationChannelStartDate%22%2C%22Direction%22%3A%22DESC%22%7D%5D%2C%22MatchedObjectDescriptor%22%3A%5B%22ID%22%2C%22PositionTitle%22%2C%22PositionURI%22%2C%22PositionShortURI%22%2C%22PositionLocation.CountryName%22%2C%22PositionLocation.CityName%22%2C%22PositionLocation.Longitude%22%2C%22PositionLocation.Latitude%22%2C%22PositionLocation.PostalCode%22%2C%22PositionLocation.StreetName%22%2C%22PositionLocation.BuildingNumber%22%2C%22PositionLocation.Distance%22%2C%22JobCategory.Name%22%2C%22PublicationStartDate%22%2C%22ParentOrganizationName%22%2C%22OrganizationName%22%2C%22OrganizationShortName%22%2C%22CareerLevel.Name%22%2C%22JobSector.Name%22%2C%22PositionIndustry.Name%22%2C%22PublicationCode%22%2C%22PublicationChannel.Id%22%2C%22PublicationChannelStartDate%22%2C%22PublicationChannel.StartDate%22%5D%7D%2C%22SearchCriteria%22%3A%5B%7B%22CriterionName%22%3A%22PublicationChannel.Code%22%2C%22CriterionValue%22%3A%5B%2212%22%5D%7D%5D%7D"


# Decode the url
decoded_url = unquote(initial_url)


# Take all the parameters and pack them into a dictionary called data
#while i in initial_url < len(initial_url) and d in decoded_url < len(decoded_url):
data = ""
base_url = ""
stopper = 0

while stopper != None:
    if initial_url[stopper] == decoded_url[stopper]:
        stopper += 1
    else:
        data += decoded_url[stopper : len(decoded_url)]
        base_url += decoded_url.split("?")[0]
        stopper = None



# Create a request with a cleaned initial url plus parameters as data dictionary.
# Consider potential errors and account for them.
response = requests.get(base_url, data=data)

if response.status_code == 200:
    # Get the response from API, turn it into json.
    # Find out the total number of search results.
    response_in_json = response.json()
    number_per_page = response_in_json.get("SearchResult").get("SearchResultCount")
    total_jobs = response_in_json.get("SearchResult").get("SearchResultCountAll")
else:
    print(f"Error: response status {response.status_code}")


# Create a list all_jobs where the jobs will be saved.
# Calculate how many requests to make (how many pages there are) to fetch all results
all_jobs = []
number_of_calls = math.ceil(total_jobs / number_per_page)

dict_data = ast.literal_eval(data)

# With a for loop, make the required number of requests.
# if the response from the request == 200:
# Take the response of each request, turn it into json.

for i in range(number_of_calls + 1):

    response = requests.post(base_url, data=dict_data)
    if response.status_code == 200:        
        dict_data["SearchParameters"]["FirstItem"] = i * number_per_page + 1
        received_json = response.json()

# From the json object extract the necessary information: Job Title, Employer, Date posted, URL - 
# - and save that as a line in a file.
        with open("heidelberg_results.txt", "a", encoding="utf-8") as hdr:
            for job in received_json.get("SearchResult").get("SearchResultItems"):
                hdr.write("Job Title: " + job.get("MatchedObjectDescriptor").get("PositionTitle") + \
                    ". Employer:  " + job.get("MatchedObjectDescriptor").get("ParentOrganizationName") + \
                        ". Link: " + job.get("MatchedObjectDescriptor").get("PositionURI") + "\n")
                
    else:
        print("Error occured, response status: " + response.status_code)


