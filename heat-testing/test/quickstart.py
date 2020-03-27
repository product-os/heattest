from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

def auth_flow():
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    global creds
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            global_creds = creds
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            global_creds = creds

def get_values():
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId='1ugnkFDmbskFz-wFcWvRGuLWvfGVXEEj2NZMBPg-Lc5U', range='Output!A1:Z50').execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    print (rows[0])
    print (rows[1])
    print (rows[5])

def set_values():
    values = [
        [
            'Yes',
            'No',
            'Yes',
            'No'
        ],

    ]
    body = {
        'values': values
    }
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().update(
        spreadsheetId='1ugnkFDmbskFz-wFcWvRGuLWvfGVXEEj2NZMBPg-Lc5U', range='Testing!A1:Z50',
        valueInputOption='RAW', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))    
    
def main():
        auth_flow()
        get_values()
        set_values()
if __name__ == '__main__':
    main()
