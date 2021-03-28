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
        html_content='<h3>Running Partner Password Reset</h3><p>Follow the link to reset your Running partner password</p><a href="http://localhost:3000/profile/reset_password/123">Reset Password Here</a>'
    )

    # Attempt to send the message
    try:
        sg = SendGridAPIClient(Config.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        print(e)
