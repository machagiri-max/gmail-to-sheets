# Gmail to Sheets Automation

## Overview
This project automates the process of reading emails from a Gmail account and logging the relevant data into a Google Sheet.  
It uses the **Gmail API** to fetch emails and the **Google Sheets API** to write data in real-time.

---

## Features
- Connects securely to Gmail using OAuth2 authentication.
- Reads incoming emails in real-time.
- Extracts sender, subject, date, and content.
- Appends the data to a Google Sheet automatically.
- Designed for easy customization and extension.

---

## Folder Structure

gmail-to-sheets/
├── pycache/ # Python cache files
├── src/ # Python source files
│ ├── email_parser.py # Parses Gmail messages
│ ├── gmail_service.py # Handles Gmail API service
│ ├── sheets_service.py # Handles Google Sheets API service
│ └── main.py # Main script to run the automation
├── config.py # Configuration file
├── requirements.txt # Python dependencies
├── .gitignore # Ignore secrets and cache files
└── gmail-to-sheets-secrets/ # Contains credentials.json & token.json (not pushed to Git)

yaml
Copy code

---

## Technologies Used
- Python 3
- Gmail API
- Google Sheets API
- OAuth2 Authentication
- pip packages: `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`

---

## Setup & Run
1. Install dependencies:
```bash
pip install -r requirements.txt
Add your credentials.json and token.json to gmail-to-sheets-secrets/.

Run the script:

bash
Copy code
python src/main.py

