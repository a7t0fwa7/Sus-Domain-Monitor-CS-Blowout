import requests
from bs4 import BeautifulSoup
import json
import os
import time

# List of source URLs containing suspicious domains
SOURCE_URLS = [
    "https://socradar.io/suspicious-domains-exploiting-the-recent-crowdstrike-outage/",
    "https://www.crowdstrike.com/blog/technical-details-on-todays-outage/",
    "https://www.cisa.gov/",
    "https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/widespread-outages-relating-crowdstrike-software-update",
    "https://krebsonsecurity.com/2024/07/global-microsoft-meltdown-tied-to-bad-crowstrike-update/",
    "https://www.reddit.com/r/sysadmin/comments/1e76lqw/be_careful_with_responding_to_crowdstrike_outage/",
    "https://techcrunch.com/2024/07/19/us-cyber-agency-cisa-says-malicious-hackers-are-taking-advantage-of-crowdstrike-outage/"
]

# Local file to store the list of suspicious domains
LOCAL_FILE = "suspicious_domains.json"

def fetch_suspicious_domains():
    domain_list = []
    for url in SOURCE_URLS:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Adjust the selector based on the actual HTML structure of each source
                domains = soup.find_all('li')  # Example selector
                domain_list.extend([domain.text.strip() for domain in domains if domain.text])
            else:
                print(f"Failed to fetch data from {url}")
        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
    return domain_list

def load_local_domains():
    try:
        with open(LOCAL_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_local_domains(domains):
    with open(LOCAL_FILE, 'w') as file:
        json.dump(domains, file, indent=4)

def update_domains():
    new_domains = fetch_suspicious_domains()
    if new_domains:
        local_domains = load_local_domains()
        updated_domains = list(set(local_domains + new_domains))
        save_local_domains(updated_domains)
        print(f"Updated domains list with {len(new_domains)} new entries.")
        print_formatted_domains(local_domains, new_domains)
    else:
        print("No new domains found.")

def print_formatted_domains(existing_domains, new_domains):
    # Create a colored output
    formatted_domains = []
    for domain in existing_domains:
        if domain in new_domains:
            # Format new domains with a green color
            formatted_domains.append(f'\033[92m{domain}\033[0m')  # Green
        else:
            formatted_domains.append(domain)

    # Print formatted domains list
    for domain in formatted_domains:
        print(domain)

if __name__ == "__main__":
    while True:
        update_domains()
        # Run the update every hour (3600 seconds)
        time.sleep(3600)