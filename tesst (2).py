import openai

# replace YOUR_API_KEY with your actual API key for the ChatGPT service
openai.api_key = "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"

# Use the OpenAI API to generate a response from ChatGPT
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

# Handle incoming messages
def handle_message(bot, update):
    message = update.message.text
    response = generate_response(message)
    bot.send_message(chat_id=update.message.chat_id, text=response)

# Use python-telegram-bot to set up the Telegram bot
from telegram.ext import Updater, CommandHandler

token = "5855564422:AAGSIvKVB89drRfSSLrV2GLgYjNiyrwfImc"
updater = Updater(token=token)
dispatcher = updater.dispatcher

message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()