from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import Config


def reset_password_email():
    # Define the message to be sent
    message = Mail(
        from_email='meyerink@umich.edu',
        to_emails='meyerink@umich.edu',
        subject='Testing testing one two three',
        html_content='<h1>Testing testing one two three</h1>'
    )

    # Attempt to send the message
    try:
        sg = SendGridAPIClient(Config.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        print(e)
