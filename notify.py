import gspread
from google.oauth2.service_account import Credentials
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from secrets import SLACK_BOT_TOKEN


def notify_users_about_progress(slack_bot_token, sheet_id, subject):
    slack_client = WebClient(token=slack_bot_token)

    scopes = ['https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(
        'credentials.json', scopes=scopes)
    client = gspread.authorize(credentials)

    sheet = client.open_by_key(sheet_id).worksheet('Sheet1')

    records = sheet.get_all_records()

    for row in records:
        email = row['Personal Email']
        no_of_no_progress = row['# of No Progress']

        if int(no_of_no_progress) > 0:
            try:
                user = slack_client.users_lookupByEmail(email=email)
                user_id = user['user']['id']
            except SlackApiError as e:
                print(f"Error looking up user by email: {e.response['error']}")
                continue

            message = f"Hello <@{user_id}>,\nYou have not made any progress in {subject} in the past week. Please take necessary actions."

            try:
                slack_client.chat_postMessage(channel=user_id, text=message)
                slack_client.chat_postMessage(channel='#dm-bot-home', text=message)
            except SlackApiError as e:
                print(f"Error sending message: {e.response['error']}")


# Usage
SHEET_ID = 'your_sheet_id'
SUBJECT = 'your_subject'

#notify_users_about_progress(SLACK_BOT_TOKEN, SHEET_ID, SUBJECT)
notify_users_about_progress(SLACK_BOT_TOKEN, '1mHOlWPpbhmEqYbiMrAUqoqP75w8Y4zW08_HvX5p_Mpg', 'programming')