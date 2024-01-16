import smtplib
from email.mime.text import MIMEText
from getpass import getpass

class EmailException(Exception):
    pass

class EmailBot:
    def __init__(self, platform: str, email: str, password: str, subject: str, body: str):
        """ Initialise Variables for the email bot
        
            platform: What email server you want to send the email from
            email: What email address you want to send the email from
            password: Your emails password
            subject: The Subject section of the email
            body: What you want the body of the email to contain
        """
        self._platform = platform.lower()
        self._subject = subject
        self._body = body
        
        if self._platform == "outlook":
            self._SMTP_SERVER = 'smtp.office365.com'
        elif self._platform == "gmail":
            self._SMTP_SERVER = 'smtp.gmail.com'
        else:
            raise EmailException("Invalid Email Type")
        
        self._SMTP_PORT = 587
        self._SMTP_EMAIL = email
        self._SMTP_PASSWORD = password

    def send_email(self, user: str) -> None:
        """Send an email to a specific user. Where the user parameter is the email of the receiving party"""

        # Create a MIMEText object with the email body and subject
        msg = MIMEText(self._body)
        msg["Subject"] = self._subject
        msg["From"] = self._SMTP_EMAIL
        msg["To"] = user

        # Send the email
        with smtplib.SMTP(self._SMTP_SERVER, self._SMTP_PORT) as smtp:
            smtp.starttls()                                     # Connect to the SMTP server
            smtp.login(self._SMTP_EMAIL, self._SMTP_PASSWORD)   # Login to the email address you will send the email from
            smtp.ehlo()
            smtp.send_message(msg)                              # Send the email
            response = "Email Sent Successfully"
            print(response)


if __name__ == "__main__":
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")
    email = input("Enter your email Address: ").strip()
    password = getpass("Enter your password: ")
    platform = input("Enter the email Platform you wish to use: ")

    try:
        bot = EmailBot(platform, email, password, subject, body)
    except EmailException as ex:
        print(f"Email Exception: {ex}")
        exit()
    except Exception as ex:
        print(f"Unexpected Exception {ex}")
        exit()

    user = input("Enter the Recipients Email Address: ")
    bot.send_email(user)
