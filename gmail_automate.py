import base64
import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
client_secrets_file  = "E:\\Python_Work\\Python_Exercise\\Python_Exercise\\ChatGpt\\Automation\\credentials.json"

def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def main():
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    try:
        query = "from:anushka108g@gmail.com is:unread"
        result = service.users().messages().list(userId='me', q=query).execute()
        messages = result.get('messages', [])

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
            msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
            text = msg_str.decode()

            REQUIRED_KEYWORDS = ['Python', 'Developer', 'MLOPS']
            if all(keyword.lower() in text.lower() for keyword in REQUIRED_KEYWORDS):
                AUTO_REPLY_MESSAGE = 'Thank you for reaching out to me. I am currently exploring new opportunities and would be interested in discussing the role further.'
                # Get the email address of the sender (recruiter)
                # Get the email headers
                msg_full = service.users().messages().get(userId='me', id=message['id']).execute()
                email_headers = msg_full['payload']['headers']

                # Get the email address of the sender (recruiter)
                sender_email = next(header['value'] for header in email_headers if header['name'] == 'From')

                draft = {
                    'message': {
                        'raw': base64.urlsafe_b64encode(
                            f"Subject: Automated Reply (Recruiter)\r\nTo: {sender_email}\r\n\r\n{AUTO_REPLY_MESSAGE}".encode('utf-8')
                        ).decode('utf-8'),
                        'threadId': message['threadId']
                    }
                }
                created_draft = service.users().drafts().create(userId='me', body=draft).execute()
                print(F'created draft with id: {created_draft["id"]}')
            else:
                print(F'message {msg["id"]} does not contain all required keywords')

    except HttpError as error:
        print(F'An error occurred: {error}')
        messages = []

if __name__ == '__main__':
    main()