import json
import whois
import requests
from termcolor import colored
from apscheduler.schedulers.blocking import BlockingScheduler

# API configuration
WHOISXML_API_KEY = 'YOUR_WHOISXML_API_KEY'
NEW_DOMAINS_API_URL = f'https://newly-registered-domains.whoisxmlapi.com/api/v1?apiKey={WHOISXML_API_KEY}&since=1h'

# Keywords to monitor
keywords = [
    "crowdstrike", "crowd", "falcon", "cs", "strike",
    "bsod", "fix", "update", "helpdesk", "bluescreen", "outage", 
    "recovery", "support", "claim", "bug", "fail", "oopsie", 
    "token", "falcon-immed-update", "cloudtrail", "sinkhole", 
    "recovery1", "failstrike", "winsstrike", "crowdpass",
    "phishing", "scam", "malware", "ransomware", "breach", 
    "hack", "cyberattack", "security", "incident", "compromised"
]

# File to store the results
output_file = "new_malicious_domains.json"

# Function to check domain creation date
def check_domain(domain):
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        return creation_date
    except Exception as e:
        print(f"Error checking domain {domain}: {e}")
        return None

# Function to fetch newly registered domains
def fetch_new_domains():
    try:
        response = requests.get(NEW_DOMAINS_API_URL)
        response.raise_for_status()
        data = response.json()
        new_domains = [domain['domainName'] for domain in data['domainsList']]
        return new_domains
    except Exception as e:
        print(f"Error fetching new domains: {e}")
        return []

# Function to monitor domains
def monitor_domains():
    new_domains = {}
    
    # Check newly registered domains for keywords
    recently_registered = fetch_new_domains()
    for domain in recently_registered:
        if any(keyword in domain for keyword in keywords):
            creation_date = check_domain(domain)
            if creation_date:
                new_domains[domain] = str(creation_date)
                print(colored(f"New domain with keyword detected: {domain} - Created on: {creation_date}", "yellow"))
    
    # Write results to JSON file
    with open(output_file, "w") as f:
        json.dump(new_domains, f, indent=4)

    print(colored("Monitoring completed. Results saved to new_malicious_domains.json", "green"))

# Scheduler setup
scheduler = BlockingScheduler()
scheduler.add_job(monitor_domains, 'interval', hours=1)

# Run the scheduler
if __name__ == "__main__":
    print(colored("Starting domain monitoring script...", "green"))
    monitor_domains()  # Initial run
    scheduler.start()