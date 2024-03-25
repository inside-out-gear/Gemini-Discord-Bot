# Gemma the Discord Gemini AI Chat Bot

This repository contains the source code for a Discord bot leveraging Google's Gemini AI for generating dynamic, context-aware responses. The bot intelligently handles long responses by splitting them into multiple messages, adhering to Discord's message length restrictions.

## Features

- **AI-Generated Responses:** Employs Google Gemini AI for crafting responses based on conversation context.
- **Contextual Memory:** Maintains conversation history to provide relevant follow-up responses.
- **Automatic Response Splitting:** Manages messages exceeding Discord's character limit by distributing the content across multiple messages.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or later installed on your machine.
- A Discord Bot Token. See [Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html) for a guide on creating a bot and obtaining your token.
- A Google API Key with access enabled for Gemini AI services. ]([https://discordpy.readthedocs.io/en/stable/discord.html](https://ai.google.dev/tutorials/web_quickstart))
- Make sure you are in a supported region (Canada isn't supported) ]([https://discordpy.readthedocs.io/en/stable/discord.html](https://ai.google.dev/available_regions))   

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```sh
git clone https://github.com/yourusername/discord-ai-chat-bot.git
cd discord-ai-chat-bot
```

Replace `https://github.com/yourusername/discord-ai-chat-bot.git` with the actual URL of your repository.

### 2. Install Dependencies

Install the required Python packages by running:

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of your project and populate it with your Discord Bot Token and Google API Key:

```plaintext
DISCORD_BOT_TOKEN=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Run the Bot

Execute the bot script with Python:

```sh
python3 bot.py
```

## Deploying with Docker

Follow these steps to containerize your Discord bot and run it using Docker.

### Create a Dockerfile

In the root directory of your project, create a `Dockerfile` with the following contents:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run bot.py when the container launches
CMD ["python3", "bot.py"]
```

### Build the Docker Image

From the directory containing your `Dockerfile`, build your Docker image:

```sh
docker build -t discord-ai-chat-bot .
```

### Run the Bot Inside a Docker Container

Launch your bot inside a Docker container:

```sh
docker run -d discord-ai-chat-bot
```

## Contributing

Contributions are welcome! For significant changes, please open an issue first to discuss what you'd like to change. Ensure to update tests as appropriate.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
