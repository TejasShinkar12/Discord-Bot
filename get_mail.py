# This Python script connects to a Gmail account via IMAP, retrieves and processes new email messages,
# and extracts the content of messages with a sender name starting with 'TLDR'.

# Import necessary libraries.
import os
import imaplib
import email
from bs4 import BeautifulSoup

# Fetch username and password from environment variables.
username = os.environ['username']
password = os.environ['pass']


# Function to retrieve and process new email messages.
def new_mail():
  # Connect to Gmail's IMAP server using SSL.
  mail = imaplib.IMAP4_SSL("imap.gmail.com")

  # Log in to the email account using the provided username and password.
  mail.login(username, password)

  # Select the 'inbox' folder in the email account.
  mail.select("inbox")

  # Search for all email messages in the 'inbox'.
  result, data = mail.uid('search', None, "ALL")
  inbox_item_list = data[0].split()

  # Iterate through the retrieved email messages in reverse order.
  for item in inbox_item_list[::-1]:
    # Fetch the email message with its unique identifier (UID).
    result2, email_data = mail.uid('fetch', item, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)

    # Iterate through the parts of the email message.
    for part in email_message.walk():
      if part.get_content_maintype() == 'multipart':
        continue

    # Check if the email sender's name starts with 'TLDR'.
    if email_message['From'].startswith('TLDR'):
      html_ = part.get_payload()
      soup = BeautifulSoup(html_, "html.parser")

      # Extract text content from HTML and perform necessary text cleaning.
      text = soup.get_text()
      text = text.replace("=\r\n", "")  # Remove line continuation characters.
      text = text.replace("=E2=80=99", "'")  # Replace special character codes.
      text = text.split("\n\n\n")  # Split text into paragraphs.
      return text  # Return the extracted text content of the email.


# This script connects to a Gmail account, retrieves email messages, and processes the content of emails
# with sender names starting with 'TLDR'. The extracted content is cleaned and returned as a list of paragraphs.
