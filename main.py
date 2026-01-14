import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from gmail_service import get_gmail_service
from email_parser import parse_message
from sheets_service import append_rows
from config import STATE_FILE


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"last_processed_internal_date": 0}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def main():
    # Load previous state
    state = load_state()

    # Get Gmail service
    gmail = get_gmail_service()

    # Fetch unread inbox emails
    results = gmail.users().messages().list(
        userId="me",
        q="is:unread in:inbox"
    ).execute()

    messages = results.get("messages", [])

    if not messages:
        print("No new unread emails found.")
        return

    rows = []

    for msg in messages:
        full_msg = gmail.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        internal_date = int(full_msg["internalDate"])

        # Prevent duplicates
        if internal_date <= state["last_processed_internal_date"]:
            continue

        sender, subject, date, body = parse_message(full_msg)

        rows.append([
            sender,
            subject,
            date,
            body
        ])

        # Mark email as read
        gmail.users().messages().modify(
            userId="me",
            id=msg["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        # Update state
        state["last_processed_internal_date"] = max(
            state["last_processed_internal_date"],
            internal_date
        )

    if rows:
        append_rows(gmail._http.credentials, rows)
        print(f"{len(rows)} emails appended to Google Sheet.")

    save_state(state)


if __name__ == "__main__":
    main()
