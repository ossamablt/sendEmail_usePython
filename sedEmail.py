import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(message):
    try:
        # Create the email message
        email_message = Mail(
            from_email='tkutchl_k151z@deypo.com',  # Replace with your verified SendGrid email
            to_emails='tkutchl_k151z@deypo.com',  # Replace with recipient's email
            subject='Alerte message negatif',
            html_content=f'<strong>{message}</strong>'
        )

        # Get the API key from the environment variables
        sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        if not sendgrid_api_key:
            raise ValueError("SendGrid API key is not set in environment variables.")

        print(f"Using SendGrid API key: {sendgrid_api_key[:6]}...")  # Print part of the key for debugging

        # Initialize SendGrid client and send the email
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(email_message)

        # Print response details
        print(f"Email sent successfully. Status Code: {response.status_code}")
        print(f"Response Body: {response.body}")
        print(f"Response Headers: {response.headers}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    message_content = "This is a test message for SendGrid."
    send_mail(message_content)
