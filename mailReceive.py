import imaplib
import email
from email.header import decode_header
from credentials import *  

# Connect to the email server
mail = imaplib.IMAP4_SSL('imap.strato.de')
mail.login(user, password)

# Select the mailbox you want to check (INBOX, for example)
mail.select('inbox')

# Search for specific emails. Use 'ALL' to get all emails.
# Other criteria can be used (e.g., UNSEEN for unread emails).
status, messages = mail.search(None, 'ALL')

# Convert the result to a list of email IDs
messages = messages[0].split()

for mail_id in messages:
    # Fetch the email by ID
    status, data = mail.fetch(mail_id, '(RFC822)')

    # The content data at the '(RFC822)' part comes in a tuple
    for response_part in data:
        if isinstance(response_part, tuple):
            # Parse the raw email content
            msg = email.message_from_bytes(response_part[1])
            # Decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # If it's a bytes type, decode to str
                subject = subject.decode(encoding)
            # Print email subject
            print("Subject:", subject)
            
            # If the email message is multipart
            if msg.is_multipart():
                # Iterate over email parts
                for part in msg.walk():
                    # Extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    # Get the email body
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        print(body)
            else:
                # Extract content type of email
                content_type = msg.get_content_type()
                # Get the email body
                if content_type == "text/plain":
                    body = msg.get_payload(decode=True).decode()
                    print(body)

# Close the connection and logout
mail.close()
mail.logout()
