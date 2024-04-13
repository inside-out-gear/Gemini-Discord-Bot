import discord
from discord.ext import commands
import google.api_core  # Import for exception handling
import google.generativeai as genai  # Import Google Gemini AI package
from dotenv import load_dotenv  # Import load_dotenv from python-dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Use environment variables to assign your API keys
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the Google Gemini AI API
genai.configure(api_key=GOOGLE_API_KEY)

# Specify intents for message content access
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialize the bot and conversation storage
bot = commands.Bot(command_prefix='!', intents=intents)
conversations = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author == bot.user or not message.content.startswith('Gemma'):
        return

    parts = message.content.split(' ', 2)
    command = parts[1] if len(parts) > 1 else 'remember'
    query = parts[2] if len(parts) > 2 else ''
    
    channel_id = message.channel.id
    user_id = message.author.id
    key = (user_id, channel_id)
    
    if key not in conversations:
        conversations[key] = []

    if command == "remember":
        conversations[key].append(query)

    prompt = "\n".join(conversations[key] + [query]) if conversations[key] else query

    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        if command == "remember":
            conversations[key].append(f"Gemma: {response_text}")
        
        prefix = "**Gemma:** "
        max_length = 2000 - len(prefix)
        
        # Check and split the response into pages if it exceeds the max_length
        if len(response_text) <= max_length:
            await message.channel.send(f"{prefix}{response_text}")
        else:
            # Splitting the response into chunks of max_length
            for i in range(0, len(response_text), max_length):
                chunk = response_text[i:i+max_length]
                await message.channel.send(f"{prefix}{chunk}")
    except Exception as e:
        print(f"An error occurred: {e}")
        await message.channel.send("Uh Oh, there was a problem with that request, please try asking another way.")

# Start the bot
bot.run(BOT_TOKEN)
