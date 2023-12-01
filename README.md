# Instagram Feed Retrieval Project

## Overview

This project is a Python script that uses the Instagram Graph API to retrieve a user's media feed. The script utilizes the `requests` library to make a GET request to the Instagram API endpoint and fetches data such as media id, caption, media type, media URL, thumbnail URL, permalink, and timestamp.

## Prerequisites

Before running the script, ensure you have the following:

- Instagram Graph API Access Token: Replace `"YOUR TOKEN"` in the script with your actual Instagram Graph API access token.
- Python Environment: Make sure you have Python installed on your system.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bujosa/instagram-api-integration.git
   cd instagram-feed-retrieval
   ```
2. **Install Depedencies
   
   ```bash
   pip install requests
   ```

## Usage

Run the script by executing the following command in your terminal:

```bash
python main.py
```

The script will make a GET request to the Instagram API and print the retrieved data if the request is successful. Otherwise, it will display the error status code and message.


