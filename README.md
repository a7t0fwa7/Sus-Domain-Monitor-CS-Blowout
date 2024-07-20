# Domain Monitoring Script

This script monitors newly registered domains for any that contain specific keywords related to the CrowdStrike incident. It uses the WhoisXML API to fetch newly registered domains and checks them for malicious activity.

## Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your system.
2. **Required Libraries**: Install the necessary Python libraries using pip.

```bash
pip install python-whois termcolor apscheduler requests
```

## Getting the WhoisXML API Key

1. **Sign Up**: Go to the [WhoisXML API website](https://www.whoisxmlapi.com/) and sign up for an account.
2. **API Key**: After signing up, navigate to the API section of your account to obtain your API key.
3. **Subscription**: Ensure you have an active subscription that allows access to the Newly Registered & Just-Expired Domains Database. Note that this is a paid service, and pricing plans are available on their [pricing page](https://whois.whoisxmlapi.com/pricing).

## Configuration

1. **API Key**: Replace the placeholder `'YOUR_WHOISXML_API_KEY'` in the script with your actual API key from WhoisXML API.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

```bash
git clone https://github.com/a7t0fwa7/Sus-Domain-Monitor-CS-Blowout.git
cd Sus-Domain-Monitor-CS-Blowout
```

2. **Run the Script**: Execute the script to start monitoring domains.

```bash
python monitor_domains.py
```

The script will:

- Fetch newly registered domains every hour.
- Check if any of the domains contain specified keywords (e.g., "crowdstrike", "crowd", "bsod", "fix", etc.).
- Print any new suspicious domains to the console and save the results to a JSON file (`new_malicious_domains.json`).

## Troubleshooting

- **API Errors**: Ensure your API key is correct and you have an active subscription.
- **Library Issues**: Make sure all required libraries are installed using the provided pip command.
- **Network Issues**: Ensure your network allows outbound connections to the WhoisXML API.

## License

This project is licensed under the MIT License.

```

### Instructions for Analysts

1. **Follow the Prerequisites**: Ensure Python 3.x is installed and required libraries are set up.
2. **Obtain API Key**: Sign up on WhoisXML API, get your API key, and ensure you have the necessary subscription.
3. **Configure the Script**: Replace the placeholder with your API key.
4. **Run the Script**: Clone the repository and execute the script to start monitoring.
```
