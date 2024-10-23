# This Python script sets up a Discord bot using the discord.py library and defines functions for handling user messages.

# Import necessary libraries and modules.
import os
import discord
import responses  # Importing custom responses module.
from get_mail import new_mail  # Importing new_mail function from get_mail module.
from keep_alive import keep_alive  # Importing keep_alive function from keep_alive module.

# Fetch new mail data and store it in the 'news' variable.
news = new_mail()


# Function to send messages to users.
async def send_message(message, user_message, is_private):
  try:
    response = responses.handle_response(
      user_message)  # Generate a response based on user's message.

    if user_message == 'news':
      # If the user requested news, send multiple messages in a loop.
      for i in new_mail():
        if is_private:
          await message.author.send(response)
        else:
          await message.channel.send("```" + next(response) + "```")
    else:
      # Send the response message.
      if is_private:
        await message.author.send(response)
      else:
        await message.channel.send(next(response))

  except Exception as e:
    print(e)


# Function to run the Discord bot.
def run_discord_bot():
  TOKEN = os.environ[
    'TOKEN']  # Fetch the bot's token from environment variables.

  # Create a Discord client instance with specified intents.
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    # When the bot is ready, print a message to indicate its status.
    print(f'{client.user} is now running!')

  @client.event
  async def on_message(message):
    # Make sure the bot doesn't respond to its own messages.
    if message.author == client.user:
      return

    # Get user information and message content.
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Print user messages for debugging purposes.
    print(f"{username} said: '{user_message}' ({channel})")

    # If a user's message starts with '?', it's treated as a private message to the bot.
    if user_message[0] == '?':
      user_message = user_message[1:]  # Remove the '?' from the message.
      await send_message(message, user_message, is_private=True)
    else:
      await send_message(message, user_message, is_private=False)

  # Start the bot, keeping it alive using the 'keep_alive' function.
  keep_alive()
  client.run(TOKEN)  # Run the bot with the specified TOKEN.


# This script sets up a Discord bot, listens for messages, and responds based on user input.
