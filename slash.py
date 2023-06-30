from flask import Flask, request, jsonify
import notify # The file containing the notify_users_about_progress function

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    text = request.form.get('text')
    # Assuming text contains slack_bot_token, sheet_id and subject separated by spaces
    slack_bot_token, sheet_id, subject = text.split(' ')

    # Call your function
    notify.notify_users_about_progress(slack_bot_token, sheet_id, subject)

    # Respond back to Slack
    return jsonify(response_type='in_channel', text=f'Notifications sent for subject: {subject}')

if __name__ == "__main__":
    app.run(debug=True)
