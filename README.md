# MailingAI
The AI to auto-respond your mails

## Server-Sided: ChatGPT (API-Key needed)
Just put the mailRespondServer.php and credentials.php on your WebServer and add the Google Apps Script googleAppsScript.js to a new Google-Account you'd like to use for generating AI mail responses.
Having added a Trigger (Trigger > Add new Trigger) running your Google Apps Script, every minute works best for me, you only need to send a mail to the Google-Account, waiting 1 min. having the trigger executed.

### credentials.php
You have to define a credentials.php (store it really safely) containing this one variable:
- api-key (your openAI-API-Key - only needed if using ChatGPT instead of GPT4All)

## Local Machine: ChatGPT (API-Key needed) or GPT4All (local AI)
You can choose if you'd like using 
- ChatGPT (by calling mailRespondChatGPT.py) or
- GPT4All (by calling mailRespondGPT4All.py) if installed API configured (pre-defined model "TheBloke/Llama-2-7B-Chat-GGUF")
Whatever you've chosen: You always need credentials.py in the same folder as mailRespondChatGPT.py or mailRespondGPT4All.py.

### credentials.py
You have to define a credentials.py (store it really safely) containing the following variables:
- password (your password for reading and sending your mails)
- user (your username for reading and sending your mails)
- sender_email (your mail-adress for reading from and sending your mails as)
- receiver_email (your mail-adress for sending your mails to)
- api-key (your openAI-API-Key - only needed if using ChatGPT instead of GPT4All)
