"""
Goal: create a script that parses a given webpage (e.g. a job board) and saves results as an overview in a text file.
Represent a job posting as an object.
"""

import requests
import json
import math


class JobPosting:
    """
    Represents a job posting with title, employer, and URL.
    """

    def __init__(self, title, employer, url):
        """
        Initializes a JobPosting object.

        Args:
            title: The job title.
            employer: The employer's name.
            url: The job posting's URL.
        """
        self.title = title
        self.employer = employer
        self.url = url

    def __str__(self):
        """
        Returns a string representation of the job posting.
        """
        return f"Job Title: {self.title}. Employer: {self.employer}. Link: {self.url}\n"


def fetch_job_postings(api_url, data_encoded):
    """
    Fetches job postings from the API and returns a list of JobPosting objects.
    """
    all_jobs = []
    try:
        response = requests.post(api_url, data=data_encoded)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        response_in_json = response.json()
        total_jobs = response_in_json.get("SearchResult", {}).get("SearchResultCountAll", 0)
        number_per_page = response_in_json.get("SearchResult", {}).get("SearchResultCount", 10)
        number_of_calls = math.ceil(total_jobs / number_per_page)
        print(f"Number of calls {number_of_calls}")

        for i in range(number_of_calls):
            first_item = i * number_per_page + 1
            data = {
                "data": {
                    "LanguageCode": "DE",
                    "SearchParameters": {
                        "FirstItem": first_item,
                        "CountItem": 10,
                        "Sort": [
                            {"Criterion": "PublicationChannelStartDate", "Direction": "DESC"}
                        ],
                        "MatchedObjectDescriptor": [
                            "ID",
                            "PositionTitle",
                            "PositionURI",
                            "PositionShortURI",
                            "PositionLocation.CountryName",
                            "PositionLocation.CityName",
                            "PositionLocation.Longitude",
                            "PositionLocation.Latitude",
                            "PositionLocation.PostalCode",
                            "PositionLocation.StreetName",
                            "PositionLocation.BuildingNumber",
                            "PositionLocation.Distance",
                            "JobCategory.Name",
                            "PublicationStartDate",
                            "ParentOrganizationName",
                            "OrganizationName",
                            "OrganizationShortName",
                            "CareerLevel.Name",
                            "JobSector.Name",
                            "PositionIndustry.Name",
                            "PublicationCode",
                            "PublicationChannel.Id",
                            "PublicationChannelStartDate",
                            "PublicationChannel.StartDate",
                        ],
                    },
                    "SearchCriteria": [
                        {"CriterionName": "PublicationChannel.Code", "CriterionValue": ["12"]}
                    ],
                }
            }
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                try:
                    received_json = response.json()
                    result_items = received_json.get("SearchResult", {}).get(
                        "SearchResultItems", []
                    )
                    for job in result_items:
                        job_title = job.get(
                            "MatchedObjectDescriptor", {}
                        ).get("PositionTitle", "N/A")
                        employer = job.get(
                            "MatchedObjectDescriptor", {}
                        ).get("ParentOrganizationName", "N/A")
                        job_url = job.get(
                            "MatchedObjectDescriptor", {}
                        ).get("PositionURI", "N/A")
                        job_posting = JobPosting(job_title, employer, job_url)
                        all_jobs.append(job_posting)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
            else:
                print("Error occured, response status: " + str(response.status_code))
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    return all_jobs


def save_job_postings_to_file(job_postings, filename="heidelberg_results_OOP.txt"):
    """
    Saves a list of JobPosting objects to a text file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as hdr: 
            for job_posting in job_postings:
                hdr.write(str(job_posting))  
        print(f"Job postings saved to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    api_url = "https://karriereapi2.klinikum.uni-heidelberg.de/search/"
    data_encoded = "%7B%22LanguageCode%22%3A%22DE%22%2C%22SearchParameters%22%3A%7B%22FirstItem%22%3A1%2C%22CountItem%22%3A10%2C%22Sort%22%3A%5B%7B%22Criterion%22%3A%22PublicationChannelStartDate%22%2C%22Direction%22%3A%22DESC%22%7D%5D%2C%22MatchedObjectDescriptor%22%3A%5B%22ID%22%2C%22PositionTitle%22%2C%22PositionURI%22%2C%22PositionShortURI%22%2C%22PositionLocation.CountryName%22%2C%22PositionLocation.CityName%22%2C%22PositionLocation.Longitude%22%2C%22PositionLocation.Latitude%22%2C%22PositionLocation.PostalCode%22%2C%22PositionLocation.StreetName%22%2C%22PositionLocation.BuildingNumber%22%2C%22PositionLocation.Distance%22%2C%22JobCategory.Name%22%2C%22PublicationStartDate%22%2C%22ParentOrganizationName%22%2C%22OrganizationName%22%2C%22OrganizationShortName%22%2C%22CareerLevel.Name%22%2C%22JobSector.Name%22%2C%22PositionIndustry.Name%22%2C%22PublicationCode%22%2C%22PublicationChannel.Id%22%2C%22PublicationChannelStartDate%22%2C%22PublicationChannel.StartDate%22%5D%7D%2C%22SearchCriteria%22%3A%5B%7B%22CriterionName%22%3A%22PublicationChannel.Code%22%2C%22CriterionValue%22%3A%5B%2212%22%5D%7D%5D%7D"
    #Fetch the job postings.
    job_postings = fetch_job_postings(api_url, data_encoded)
    #Save the job postings to file
    save_job_postings_to_file(job_postings)