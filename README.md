# MailingAI
The AI to auto-respond your mails

## ChatGPT or GPT4All (local)
You can choose if you'd like using 
- ChatGPT (by calling mailRespondChatGPT.py) or
- GPT4All (by calling mailRespondGPT4All.py) if installed API configured (pre-defined model "TheBloke/Llama-2-7B-Chat-GGUF")

## credentials.py
You have to define a credentials.py containing the following variables:
- password (your password for reading and sending your mails)
- user (your username for reading and sending your mails)
- sender_email (your mail-adress for reading from and sending your mails as)
- receiver_email (your mail-adress for sending your mails to)
- api-key (your openAI-API-Key - only needed if using ChatGPT instead of GPT4All)
