from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import Config


def reset_password_email(email, user_id):
    """
    Sends an email to the passed user allowing them to reset their password.
    """
    # Define the message to be sent
    message = Mail(
        from_email='meyerink@umich.edu',
        to_emails=email,
        subject='Reset Your Running Partner Password',
        html_content='<p>Testing</p>'
    )

    # Attempt to send the message
    try:
        sg = SendGridAPIClient(Config.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        print(e)
