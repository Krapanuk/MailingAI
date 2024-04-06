import imaplib
import email
from email.header import decode_header
import requests
from credentials import *

# Personalize AI responses here
whoAmI = 'You are a helpful assistant answering the mails in the role of a 40 year old software developer, married with a beautiful wife. You have 2 kids and live in Germany near Bielefeld.' 

def local_ai_call(prompt, model="TheBloke/Llama-2-7B-Chat-GGUF"):
    apiUrl = "http://127.0.0.1:4891/v1/completions"  # Local AI endpoint
    data = {
        "prompt": prompt,
        "model": model,
        "max_tokens": 50,
        "temperature": 0.28,
        "top_p": 0.95,
        "n": 1
    }
    try:
        response = requests.post(apiUrl, json=data)
        if response.ok:
            return response.json()
        else:
            print(f"Error during Local AI call: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error during Local AI call: {e}")
        return None

# Connect to the email server
mail = imaplib.IMAP4_SSL('imap.strato.de')
mail.login(user, password)
mail.select('inbox')  # Select the mailbox

# Search and fetch emails
status, messages = mail.search(None, 'ALL')
messages = messages[0].split()

for mail_id in messages:
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

            prompt = f"{whoAmI}\n{body[:100]}"  # Adjust the prompt as needed
            local_ai_response = local_ai_call(prompt)

            if local_ai_response:
                answer = local_ai_response['choices'][0]['text']
                mailSend(answer)
    
            mail.store(mail_id, '+FLAGS', '\\Deleted')

mail.expunge()
mail.close()
mail.logout()
