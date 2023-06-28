# Slack Progress Notifier

This bot monitors a Google Sheet for students' progress in a particular subject and sends notifications to the students via Slack if they have not made any progress.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Google account with access to Google Sheets
- Slack Bot Token
- Flask (for executing Python code from Slack)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jeremycsumb/becs-dm-bot.git

2. Install the required packages:
    pip install gspread google-auth slack-sdk Flask

3. Setup Google Sheets API from Google Cloud Console and download the credentials.json file. Place this file in the root directory of the project.

4. Set up a Slack bot and obtain a bot token.
