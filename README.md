# Suspicious Domains Monitoring

Python script designed to automate the process of updating a list of suspicious domains related to the recent CrowdStrike outage. The script periodically checks multiple sources for new domains and updates a local list to help organizations monitor and block malicious activities. Newly added domains are highlighted in green for easy identification.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Background

On July 19, 2024, a faulty software update from CrowdStrike caused a global IT outage, affecting numerous services worldwide. Malicious actors have since been exploiting this situation by using suspicious domains for phishing and other cyberattacks. This script helps in identifying and updating these domains to mitigate risks.

## Features

- **Automated Updates**: Periodically fetches and updates the list of suspicious domains from multiple sources.
- **Multiple Sources**: Checks various reliable sources for the latest information.
- **Local Storage**: Stores the updated list of domains locally in a JSON file.
- **Easy Configuration**: Simple to configure and extend with additional sources.
- **Color Differentiation**: Highlights newly added domains in green for easy identification.

## Installation

To install and set up the script, follow these steps:

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/suspicious-domains-monitoring.git
   cd suspicious-domains-monitoring
   ```
2. **Create a Virtual Environment**:

   ```sh
   python -m venv myenv
   ```
3. **Activate the Virtual Environment**:

   - **On Windows**:
     ```sh
     myenv\Scripts\activate
     ```
   - **On macOS and Linux**:
     ```sh
     source myenv/bin/activate
     ```
4. **Install Dependencies**:

   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

To run the script, execute the following command:

```sh
python main.py
```

Python script designed to automate the process of updating a list of suspicious domains related to the recent CrowdStrike outage. The script periodically checks multiple sources for new domains and updates a local list to help organizations monitor and block malicious activities. Newly added domains are highlighted in green for easy identification.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Background

On July 19, 2024, a faulty software update from CrowdStrike caused a global IT outage, affecting numerous services worldwide. Malicious actors have since been exploiting this situation by using suspicious domains for phishing and other cyberattacks. This script helps in identifying and updating these domains to mitigate risks.

## Features

- **Automated Updates**: Periodically fetches and updates the list of suspicious domains from multiple sources.
- **Multiple Sources**: Checks various reliable sources for the latest information.
- **Local Storage**: Stores the updated list of domains locally in a JSON file.
- **Easy Configuration**: Simple to configure and extend with additional sources.
- **Color Differentiation**: Highlights newly added domains in green for easy identification.

## Installation

To install and set up the script, follow these steps:

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/suspicious-domains-monitoring.git
   cd suspicious-domains-monitoring
   ```
2. **Install Dependencies**:

   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

To run the script, execute the following command:

```sh
python update_suspicious_domains.py
```
