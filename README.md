# MailingAI
The AI to auto-respond your mails: 
Send a mail from your personal mail-account to a new AI-Response-GoogleMail Account receiving an AI-generated response-mail.

## Server-Sided: ChatGPT ([API-Key needed](https://openai.com/blog/openai-api))
Just put the mailResponseServer.php and credentials.php on your WebServer and add the code of googleAppsScript.js as new [Google Apps Script](https://script.google.com) to a new Google-Account you'd like to use for generating AI mail responses.
Having added a Trigger (Trigger > Add new Trigger) running your Google Apps Script, every minute works best for me, you only need make some small changes fitting the files for your purposes. send a mail to the Google-Account, waiting 1 min. having the trigger executed.

### credentials.php
You have to define a credentials.php (store it really safely) containing this one variable:
- api-key (your [OpenAI API-Key](https://openai.com/blog/openai-api))

### Changes to be made
Some personalizations are to be made before the first run:
- mailResponseServer.php:
  - Update the $receiverEmail and $senderEmail variables' placeholder mailadress "SenderToBeProcssed@anymail.net" to your personal mail-adress you will be sending mails for the AI to respond and
  - change the description in the $whoAmI variable to what fits best for you.
- Google Apps Script googleAppsScript.js:
  - Update the placeholder mailadress "SenderToBeProcssed@anymail.net" to your personal mail-adress you will be sending mails for the AI to respond and
  - change the url-variable to fit the path to the mailResponseServer.php-script on your webserver and 

### Test it
Having changed the few variables you're ready to send your first mail to the Google-Account, waiting 1 min. having the trigger executed and a few seconds later receiving AIs response in your response-mail-account.

## Local Machine: ChatGPT ([API-Key needed](https://openai.com/blog/openai-api)) or [GPT4All](https://gpt4all.io) (local AI)
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
