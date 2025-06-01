"""Gathers data from the Committee to Protect Journalists (CPJ) API
For more detailed information about individual journalists, you may need to
use the personrecord API endpoint associated with each journalist's detail page.

For example:
Standard detail page for a journalist
https://cpj.org/data/people/abadullah-hananzai/

The above page contains a unique identifier for the journalist in the HTML, which is used to pull data
from another API endpoint. The identifier is called `datamanager_salesforce_id` and can be found in the page's HTML.

The datamanager_salesforce_id can be extracted using various techniques
such as searching for the text ("datamanager_salesforce_id") and grabbing the id value or using
a regular expression.

Once you have that have ID, you can construct an API call for detailed metadata
about the person using the personrecord endpoint:
https://cpj.org/wp-json/cpj-datamanager/v1/personrecord?datamanager_salesforce_id=a07Hs00001BhlWOIAZ

USAGE: uv run python scripts/cpj_scraper.py       

"""
import json
import time
import requests
import csv

BASE_URL = "https://cpj.org/wp-json/cpj-datamanager/v1/people_list"

# ?status=Killed&motive=Confirmed&role=Journalist&year=1992,2025&sortBy=fullName&page=1"
GET_PARAMS = {
    'status': 'Killed',
    'motive': 'Confirmed',
    'role': 'Journalist',
    'year': '1992,2025',
    'sortBy': 'fullName',
    'page': 1
}

def main():
    response = requests.get(BASE_URL, params=GET_PARAMS)
    # Determine total number of pages
    response = response.json()
    page_count = int(response['pageCount'])
    data = []
    # add first page of results
    data.extend(response['data'])
    current_page = 2
    while current_page <= page_count:
        time.sleep(.5)  # Respectful delay to avoid overwhelming the server
        GET_PARAMS['page'] = current_page
        print("Gathering page:", current_page)
        response = requests.get(BASE_URL, params=GET_PARAMS)
        response = response.json()
        data.extend(response['data'])
        current_page += 1
    print("Gathered data from all pages.")
    write_data(data)

def write_data(data):
    # Write to JSON file
    with open('cpj_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data written to cpj_data.json with {len(data)} records.")

    # Write to CSV file
    with open('data/cpj_data.csv', 'w', newline='') as f:
        if data:
            # Extract headers from the first record
            headers = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data written to data/cpj_data.csv with {len(data)} records.")


if __name__ == "__main__":
    main()