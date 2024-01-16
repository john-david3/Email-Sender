This program automates the process of sending emails.

At the moment it relies entirely on user input but can be altered with a hardcoded body and/or subject to send an automated email to any email address the user wishes.

Currently the only sender email servers supported are Outlook and Gmail.

The program uses a combination of SMTPLib to connect to the senders email and the MIMEText library to format the subject and the body of the email.

All the necessary user inputs have been appropriately sanitised and passwords are hidden using the getpass library.
