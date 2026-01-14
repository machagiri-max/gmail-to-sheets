import base64

def parse_message(message):
    """
    Extracts From, Subject, Date, and Body (plain text) from Gmail message
    """
    headers = message["payload"]["headers"]
    header_dict = {h["name"]: h["value"] for h in headers}

    # Default values if header missing
    sender = header_dict.get("From", "")
    subject = header_dict.get("Subject", "")
    date = header_dict.get("Date", "")

    # Extract plain text body
    body = ""
    parts = message["payload"].get("parts", [])
    for part in parts:
        if part["mimeType"] == "text/plain":
            body = base64.urlsafe_b64decode(part["body"]["data"]).decode()
            break

    return sender, subject, date, body
