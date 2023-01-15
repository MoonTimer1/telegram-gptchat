import openai
import telegram
from telegram.ext import Updater, CommandHandler

# Set up OpenAI API key
openai.api_key = "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"

# Create Telegram bot
updater = Updater("5855564422:AAGSIvKVB89drRfSSLrV2GLgYjNiyrwfImc", use_context=True)

def respond_gpt(update, context):
    # Get user's message
    message = update.message.text
    # Send message to OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{message}"),
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    # Get the first response from API
    reply = response["choices"][0]["text"]
    # Send response to Telegram
    update.message.reply_text(reply)

# Add command handler for '/respond_gpt' command
dp = updater.dispatcher
dp.add_handler(CommandHandler("respond_gpt", respond_gpt))

# Start the bot
updater.start_polling()
updater.idle()
