import imaplib
import email
from email.header import decode_header
import requests
import time # for delays
from credentials import *
from mailSend import *

# Here you can personalize the AIs responses
whoAmI= 'You are a helpful assistant answering the mails in the role of a 40 year old software developer, married with a beautiful wife. You have 2 kids and live in Germany near Bielefeld.' 

def log_message(message):
    print(message)

def api_call(request_data, api_key):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    response = requests.post(url, json=request_data, headers=headers)
    if response.ok:
        return response.json()
    else:
        print(f"Error during API call: {response.status_code}")
        return None

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

processed_ids = set()

for mail_id in messages:
    # Fetch the email by ID
    if mail_id in processed_ids:
        continue  # Don't process the same mail twice
    status, data = mail.fetch(mail_id, '(RFC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding)

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition")):
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                if msg.get_content_type() == "text/plain":
                    body = msg.get_payload(decode=True).decode()

            # Send the first 100 characters of the email body to the API
            request_data = {
                "model": "gpt-4-turbo-preview",
                "messages": [{"role": "system", "content": whoAmI}, {"role": "user", "content": body[:100]}],
                "temperature": 1.0
            }
            api_response = api_call(request_data, api_key)

            if api_response:
                answer = api_response['choices'][0]['message']['content']
                mailSend(answer)
                log_message(f"Sent response for mail ID {mail_id}")
    
            # Mark the email for deletion
            mail.store(mail_id, '+FLAGS', '\\Deleted')
            processed_ids.add(mail_id)  # mark mail as processed
            time.sleep(1)  # delay, giving the server enough time to process the request

# Expunge and logout
mail.expunge()
mail.close()
mail.logout()
