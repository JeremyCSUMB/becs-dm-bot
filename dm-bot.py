import gspread
from google.oauth2.service_account import Credentials
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = 'your_slack_bot_token_here'
slack_client = WebClient(token=SLACK_BOT_TOKEN)


scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(
    "credentials.json", scopes=scopes)
client = gspread.authorize(credentials)

sheet_id = "your_sheet_id_here"
sheet = client.open_by_key(sheet_id).worksheet("Sheet1")


records = sheet.get_all_records()


for row in records:
    first_name = row['First Name']
    last_name = row['Last Name']
    email = row['Personal Email']
    programming = row['PROGRAMMING']
    no_of_no_progress = row['# of No Progress']

    if int(no_of_no_progress) > 0:

        try:
            user = slack_client.users_lookupByEmail(email=email)
            user_id = user['user']['id']
        except SlackApiError as e:
            print(f"Error looking up user by email: {e.response['error']}")
            continue

        message = f"Hello <@{user_id}>,\nYou have not made any progress in programming in the past week. Please take necessary actions."

        try:
            slack_client.chat_postMessage(channel=user_id, text=message)
            slack_client.chat_postMessage(channel='#dm-bot-home', text=message)
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
