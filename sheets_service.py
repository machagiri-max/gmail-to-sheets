from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from config import SPREADSHEET_ID, SHEET_NAME, SCOPES


def append_rows(creds, rows):
    sheets_service = build("sheets", "v4", credentials=creds)

    body = {
        "values": rows
    }

    sheets_service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()
