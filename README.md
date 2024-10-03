# Telegram bot with neural network
Very small code to implement a telegram bot with neural network
Created by ITL_Was, with support from ATOG

Command in telegram bot (to clear context)

```/cont''`

# Installation
Go to any folder, open cmd from it and enter the following commands:

```git clone https://github.com/ITL-Was/Telegram-bot-with-neural-network```

```cd Telegram-bot-with-neural-network```

# API keys
API keys are needed for the neural network itself, and for telegram bot operation
For the telegram api you need to get the token itself in the bot, the bot itself is called @BotFather (telegram)

Here's his link: ```https://t.me/BotFather```

 For api groq, you need to go to the site and register on it, then you need to get the api groq key yourself

Here's the link:```https://console.groq.com/keys```

# Where do I put the keys?

Keys are necessary for telegram bot and neural network in it, when you have already received all 2 keys, they should be inserted into the .env file,

Against the letter G insert your api key groq (It should be without quotation marks, here is an example: “G=12345”, Instead of 12345 your api key).

For api telegram everything is the same (without quotation marks), but you insert the key not against the letter G, but against the letter T.

Here is an example of how it should look like

![image](https://github.com/user-attachments/assets/d8a8e721-e87e-4b37-8a8c-0135b5a25160)

# What's an “S”?

This is the system message, in short it is the text that the neural network will always remember (you can write the name of the neural network, how to send answers to it, any information in English), By default the system message will be like this: ```Your name is Llama 3.1, write small, informative posts.```, the system message should be written in quotation marks, unlike other messages, here is an example: ```S=“Your name is Llama 3.1, write small, informative posts.”```

# How to start a telegram bot?

When you have already completed the steps in “Installation”, write

``.\venv\Scripts\activate``.

Then write the command to install the required libraries

``pip install -r requirements.txt``.

And the final command (To run the telegram bot)

``py app.py``.

After that your bot (for which you made api key) will be launched










